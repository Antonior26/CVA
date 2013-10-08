'''
Created on 08/10/2013

@author: antonior
'''
class loh_variant:
    '''****************
    This class has methods Loh Variants
    ***************'''
    
    def __init__(self,chrom,pos,ref,alt,line):
        '''****************
        Constructor
        ****************'''
        self.chrom=chrom
        self.pos=pos
        self.ref=ref
        self.alt=alt
        self.line=line
        
###############~Comparison Methods~###############

    
    def __eq__(self, other):
        return other and self.chrom == other.chrom and self.pos == other.pos
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self,other):
        if self.chrom!=other.chrom:
            raise Exception("Dfferent chromosomes")
        elif self.chrom == other.chrom and self.pos < other.pos:
            return True
        else:
            return False
    
    def __le__(self,other):
        if self.chrom!=other.chrom:
            raise Exception("Dfferent chromosomes")
        elif self.chrom == other.chrom and self.pos <= other.pos:
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.chrom!=other.chrom:
            raise Exception("Dfferent chromosomes")
        elif self.chrom == other.chrom and self.pos > other.pos:
            return True
        else:
            return False
    
    def __ge__(self,other):
        if self.chrom!=other.chrom:
            raise Exception("Dfferent chromosomes")
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

            
        
  
    
    