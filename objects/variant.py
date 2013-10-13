'''
Created on 13/10/2013

@author: antonio
'''
import LossOfHeterocigosity_region as loh_r
class variant:
    '''
    classdocs
    '''
    def __init__(self,chrom,pos,ref,alt,filter,line):
        '''****************
        Constructor
        ****************'''
        self.chrom=chrom
        self.pos=pos
        self.ref=ref
        self.alt=alt
        self.filter=filter
        self.line=line
        
###############~Comparison Methods~###############

    
    def __eq__(self, other):
        return other and self.chrom == other.chrom and self.pos == other.pos
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self,other):
        if self.chrom!=other.chrom:
            try:
                if int(self.chrom)<int(other.chrom):
                    return True
                else:
                    return False
            except:
                if self.chrom<other.chrom:
                    return True
                else:
                    return False
        elif self.chrom == other.chrom and self.pos < other.pos:
            return True
        else:
            return False
    
    def __le__(self,other):
        if self.chrom!=other.chrom:
            try:
                if int(self.chrom)<int(other.chrom):
                    return True
                else:
                    return False
            except:
                if self.chrom<other.chrom:
                    return True
                else:
                    return False
        elif self.chrom == other.chrom and self.pos <= other.pos:
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.chrom!=other.chrom:
            try:
                if int(self.chrom)>int(other.chrom):
                    return True
                else:
                    return False
            except:
                if self.chrom>other.chrom:
                    return True
                else:
                    return False
        elif self.chrom == other.chrom and self.pos > other.pos:
            return True
        else:
            return False
    
    def __ge__(self,other):
        if self.chrom!=other.chrom:
            try:
                if int(self.chrom)>int(other.chrom):
                    return True
                else:
                    return False
            except:
                if self.chrom>other.chrom:
                    return True
                else:
                    return False
        elif self.chrom == other.chrom and self.pos >= other.pos:
            return True
        else:
            return False

##################################################
    
    def __hash__(self):
        return hash((self.chrom, self.pos, self.ref, self.alt))
    
    def __str__(self):
        return self.line
    
    def __sub__(self,other):
        if self.chrom==other.chrom:
            return self.pos-other.pos
        else:
            raise Exception("Dfferent chromosomes")
        
        
        
        
class loh_variant(variant):
    '''****************
    This class has methods Loh Variants
    ***************'''
        
    def check_cluster(self,other,limit=1000):
        if self.chrom==other.chrom:
            if abs(self-other)<=limit:
                return True
            else:
                return False
        else:
            return False




    def get_interval(self,other):
        if self.chrom!=other.chrom:
            raise Exception("Dfferent chromosomes")
        else:
            if self<=other:
                region=loh_r.loh_region(self.chrom,self.pos,other.pos,[self,other])
            else:
                region=loh_r.loh_region(self.chrom,other.pos,self.pos,[self,other])
            return region
        