'''
Created on 05/10/2013

@author: antonio
'''

import conf_file

class variant:
    '''****************
    This class has methods Cancer Variants
    ***************'''
    
    def __init__(self,chrom,pos,ref,alt,line,feat,conf):
        '''****************
        Constructor
        ****************'''
        self.chrom=chrom
        self.pos=pos
        self.ref=ref
        self.alt=alt
        self.feats=feat
        self.features={}
        self.line=line
        self.conf=conf
        
    
    def __eq__(self, other):
        return other and self.chrom == other.chrom and self.pos == other.pos and self.ref == other.ref and self.alt == other.alt
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.chrom, self.pos, self.ref, self.alt))
    
    def filter(self):
        for f in self.conf.params:
            
            if f[2][0]=='=':
                if self.feats[f[1]]==self.feats[f[1]]:
                    self.features[f[0]]=self.feats[f[1]]
                else:
                    return False
                    
            if f[2][0]=='>':
                if self.feats[f[1]]>self.feats[f[1]]:
                    self.features[f[0]]=self.feats[f[1]]
                else:
                    return False
                    
            if f[2][0]=='<':
                if self.feats[f[1]]<self.feats[f[1]]:
                    self.features[f[0]]=self.feats[f[1]]
                else:
                    return False
        return True
    
    
    
    