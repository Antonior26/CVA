'''
Created on 28/10/2013

@author: antonior
'''
import os

class annovar_file():
    '''
    classdocs
    '''


    def __init__(self, _filename, _db='/data/reference_genomes/human/annotation/'):
        '''
        Constructor
        '''
        self.filename = _filename
        self.db=_db
        
    def gene_anno(self, prefix, qsub=False):
        if qsub:
            os.system("qsub -N GeneAnno run_annovar.sh gene "+self.filename+" "+prefix)
        else:
            os.system("annotate_variation.pl -buildver hg19 -geneanno --outfile "+prefix+" "+self.filename+" "+self.db)
    
    def filter_annot(self, dbtype, prefix, qsub=False):
        if qsub:
            os.system("qsub -N FilterAnno run_annovar.sh filter "+self.filename+" "+prefix+" "+dbtype)
        else:
            os.system("annotate_variation.pl -buildver hg19 -filter --outfile "+prefix+" --dbtype "+dbtype+" "+self.filename+" "+self.db)
        