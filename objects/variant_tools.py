'''
Created on 29/10/2013

@author: antonior
'''
import os
import optparse
import sys
import utils
import json
'''
annotate_ofields={'refGene':[['refGene.name','refGeneID'],['refGene.name2','refGeneName']],
                  'dbSNP':[['dbSNP.name','dbSNPID'],['dbSNP.COMMON','isACommonSNP'],['dbSNP.CLNSIG','Clinical_Significance'],['dbSNP.CLNDBN','Disease']],
                  'dbNSFP':[['dbNSFP.aaref','refAA'],['dbNSFP.aaalt','altAA'],['dbNSFP.SIFT_score','SIFT_Score'],['dbNSFP.Polyphen2_HDIV_score_max','Polyphen2_Score'],['dbNSFP.MutationTaster_score','MutationTaster_score'],['dbNSFP.GERP_RS','Conservation_Grep'],['dbNSFP.PhyloP_score','Conservation_PhyloP']],
                  'evs-6500':[['evs.AllMaf','ESP_Minor_allele_Frequency']],
                  'thousandGenomesEBI':[['thousandGenomesEBI.AF_INFO','ThousandGenomes_Allele_Frequency']],
                  'CosmicCodingMuts':[['CosmicCodingMuts.COSMIC_ID','CosmicID']],
                 
                 
                 }
'''

class varaint_tools:
    '''
    This class use variant tools to annotate a variant file (chr pos ref alt), could be a vcf file, bed file, pipelup file...
    '''


    def __init__(self, _dirname, name='project', qsub=False):
        '''
        Constructor
        '''
        self.dir=_dirname
        self.name=name
        self.qsub=qsub
        self.annotationlist=[]
        self.wait=''
        os.system("mkdir "+_dirname)
        if self.qsub:
            os.system("qsub -N init_"+self.name+" vt_init.sh "+self.dir+" "+self.name)
            self.wait=self.wait+" init_"+self.name
        else:
            os.system("cd "+self.dir+"; vtools init "+self.name)
    
    def add_file(self, _filename, samplename):
        '''
        Add file to annotate
        '''
        if self.qsub:
            os.system("qsub -N import_"+self.name+" -hold_jid "+self.wait+"  vt_import.sh "+self.dir+" "+samplename+" "+_filename)
            self.wait=self.wait+",import_"+self.name
        else:
            os.system("cd "+self.dir+"; vtools import "+_filename+" --build hg19 --sample_name "+samplename)
    
    
    def consequence_annotation(self, annovarPath='/usr/local/annovar/', annovarDB='~/humandb/'):
        
        if self.qsub:
            os.system("qsub -N conseq_"+self.name+" -hold_jid "+self.wait+"  vt_conseq.sh "+self.dir+' '+annovarDB)
            self.wait=self.wait+",conseq_"+self.name
        else:
            os.system("cd "+self.dir+"; vtools export variant --output ANNOVAR.input --format ANNOVAR")
            os.system("cd "+self.dir+"; "+annovarPath+"annotate_variation.pl -geneanno ANNOVAR.input -buildver hg19 "+annovarDB)
            os.system("cd "+self.dir+"; vtools update variant --format ANNOVAR_exonic_variant_function --from_file ANNOVAR.input.exonic_variant_function --var_info mut_type")
            os.system("cd "+self.dir+"; vtools update variant --format ANNOVAR_variant_function --from_file ANNOVAR.input.variant_function --var_info region_type")
        
    
    def annotation (self, database):
        '''
        Annotate file with a database (i.e dbSNP,1000g...)
        '''
        annotation_av=[]
        a=os.popen("cd "+self.dir+"; vtools show annotations")
        for line in a:
            if line.split(" ")[0]!='':
                annotation_av.append(line.split(" ")[0])

        if database in annotation_av:
            self.annotationlist.append(database)
            if self.qsub:
                os.system("qsub -N annot_"+self.name+" -hold_jid "+self.wait+" vt_annotation.sh "+self.dir+" "+database)
                self.wait=self.wait+",annot_"+self.name
            else:
                os.system("cd "+self.dir+"; vtools use "+database)
            return "Annotation Done"
        else:
            return "DataBase not available"
    
    def output (self, _filename, annotate_ofields, spitbytype=False, where=''):
        '''
        write annotation in tab format
        '''
        fields=["chr","pos","ref","alt","region_type","mut_type"]
        names=["chr","pos","ref","alt","region_type","mutation_type"]
        for annot in self.annotationlist:
            if annot in annotate_ofields:
                for ref in annotate_ofields[annot]:
                    fields.append(ref[0])
                    names.append(ref[1])
            else:
                print "Annotation Skipped, please check available annotations in this script"
        strfields=" ".join(fields)
        strnames=" ".join(names)
        print "INFO: Exporting annotation to table"    
        
        if spitbytype:
            if self.qsub:
                os.system("qsub -N split_"+self.name+" -hold_jid "+self.wait+" split.sh "+self.dir)
                self.wait=self.wait+",annot_"+self.name
            else:
                os.system("cd "+self.dir+"""; vtools select variant '(region_type like "%splicing%"  or region_type like "%UTR3%" or region_type like "%UTR5%" ) or (region_type like "%exonic%" and mut_type!="synonymous SNV")"""+where+"""' -t exonic""")
                os.system("cd "+self.dir+"; vtools compare variant exonic --difference 'intronic'  --mode variant")
                os.system("cd "+self.dir+"; vtools output intronic "+strfields+" -d '\t' --na - --header "+strnames+" >"+_filename+"_intronic.txt")
                os.system("cd "+self.dir+";  vtools output exonic "+strfields+" -d '\t' --na -  --header "+strnames+" >"+_filename+"_exonic.txt")
        else:
            os.system("cd "+self.dir+"; vtools output variant "+strfields+" -d '\t' --header "+strnames+" >"+_filename+"_all.txt")
            
                 
          
    
    def annotate_vcf (self,dirname,_filename,samplename, database_list):
        '''
        Annotate a vcf using a list of databases
        '''
        pass




def main():
    ################################################

    #### Options and arguments #####################

    ################################################  
            
    usage=""" 
    ************************************************************************************************************************************************************
    Task: 
    ************************************************************************************************************************************************************
    """
    parser = optparse.OptionParser(usage)
    parser.add_option("-d", dest="dirname", help="""Directory name (directory name)""")
    parser.add_option("-j", dest="project_name", help="""Project_name""")
    parser.add_option("-f", dest="filename", help="""Variant file to annotate (variant file)""")
    parser.add_option("-p", dest="prefix", help="""prefix (results prefix)""")
    parser.add_option("-n", dest="sampleName",default="Sample", help="""[Optional] Use a sample name (default sample)""")
    parser.add_option("--filter_conf", dest="confilter", help="""Configuration file for filters in json format (conf file)""")
    parser.add_option("--conf", dest="confile", help="""Configuration file for annotation in json format (conf file)""")
    parser.add_option("-s", dest="split", action="store_true", default=False, help="""[Optional] If argument is present the output will be split by consequence type""")
    parser.add_option("--skip annot", dest="skip", action="store_true", default=False, help="""[Optional] If argument is present only consequence type will be annotate""")

    
    (options, args) = parser.parse_args()

    # Check number of arguments    
    if options.dirname==None or options.filename==None or options.prefix==None:
        parser.print_help()
        sys.exit(1)
        

    #Load Conf_annotation
    conf=file(options.confile)
    annotate_ofields=json.loads(conf.read())
    if options.skip==False:
        listDB=annotate_ofields.keys()
    
    #Load Conf_filter
    filters_str='and ('
    afilters=[]
    filtersfile=file(options.confilter)
    filters=json.loads(filtersfile.read())
    for f in filters:
        filter_str='('
        filter_str=filter_str+filters[f]
        filter_str=filter_str+')'
        afilters.append(filter_str)
    filters_str=filters_str+' and '.join(afilters)
    filters_str=filters_str+')'
    print filters_str
    
   
   

    pro=varaint_tools(options.dirname, options.project_name)
    pro.add_file(options.filename, options.sampleName)
    pro.consequence_annotation()
    
    if options.skip==False:
        for DB in listDB:
            pro.annotation(DB)
    
    pro.output(options.prefix,annotate_ofields, options.split, filters_str)
    
    
    listoftyoes=['TEXT','INT','TEXT','TEXT','TEXT','TEXT']
    
    for key in annotate_ofields:
        listoftyoes.append(annotate_ofields[key])
    
    if options.split:
        
        tableExonic=utils.table(options.dirname+'/'+options.prefix+"_exonic.txt")
        tableIntronic=utils.table(options.dirname+'/'+options.prefix+"_intronic.txt")
        tableExonic.tabletosqlite(options.dirname+'/'+options.prefix+"_exonic", options.sampleName,listoftyoes)
        tableIntronic.tabletosqlite(options.dirname+'/'+options.prefix+"_intronic",options.sampleName, listoftyoes)
        tableExonic.tabletoxls(options.dirname+'/'+options.prefix+"_exonic", options.sampleName)
        tableIntronic.tabletoxls(options.dirname+'/'+options.prefix+"_intronic", options.sampleName)
    else:
        tableAll=utils.table(options.dirname+'/'+options.prefix+"_all.txt")
        tableAll.tabletosqlite(options.dirname+'/'+options.prefix+"_all",options.sampleName, listoftyoes)
        tableAll.tabletoxls(options.dirname+'/'+options.prefix+"_all", options.sampleName)
if __name__=='__main__':
    main() 
        

