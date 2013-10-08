'''
Created on 08/10/2013

@author: antonior
'''

import requests
import json

class loh_region:
    '''****************************
    This class has methods Loh Variants
    *****************************'''


    def __init__(self,chrom,start,end,loh_sites):
        '''******************
        Constructor:
            chrom: Chromosome [string]
            start: Start possition 0-based [int]
            end: End possition 0-based [int]
            nloh_sites: LOH sites in region [list] 
        *******************'''
        self.chrom=chrom
        self.start=start
        self.end=end
        self.loh_sites=loh_sites
        self.length=self.end-self.start #Length of the region
        self.ids=[] #ENSBL ids of genes overlapping with this region
        self.names=[] #Common name of genes overlapping with this region
    
    def __str__(self):
        
        ids=",".join(self.ids)
        names=",".join(self.names)
        return self.chrom+'\t'+str(self.start)+'\t'+str(self.end)+'\t'+str(self.end-self.start)+'\t'+str(len(self.loh_sites))+"\t"+ids+"\t"+names
    
    def __len__(self):
        return self.end-self.start
    
    
    def cellbase_annotation(self,type="gene"):
        '''**********************************
        Annotation by region ussing cellbase
            type: type of feature to annotate, i.e: gene,snp...
        **********************************'''
        
        url="http://ws.bioinfo.cipf.es/cellbase/rest/latest/hsa/genomic/region/"+str(self.chrom)+":"+str(self.start)+"-"+str(self.end)+"/"+type+"?of=json"
        query=requests.get(url)
        annotation=json.loads(query.content)
        
        for row in annotation[0]:
            try:
                self.ids.append(row["stableId"])
            except:
                print "Found feature without id" 
            try:
                self.names.append(row["externalName"])
            except:
                print "Found feature without external Name" 
    
    def get_variants(self):
        return self.loh_sites
    
    def add_varinat(self,variant):
        if self.chrom!=variant.chrom:
            raise Exception("Dfferent chromosomes")
        elif self.start<=variant.pos and self.end>=variant.pos:
            self.loh_sites.append(variant)
        elif self.start>variant.pos:
            self.loh_sites.append(variant)
            self.start=variant.pos
        elif self.end<variant.pos:
            self.loh_sites.append(variant)
            self.end=variant.pos
        
        
        
        
        
        
        
        
        
        