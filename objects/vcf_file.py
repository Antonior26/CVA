'''
Created on 13/10/2013

@author: antonio
'''
import objects.variant as variant

class vcf_file:
    """***********************************************************************************************************************************************
    Class to model and manage vcf files
    ***********************************************************************************************************************************************"""
    
    def __init__(self, _filename):
        """*******************************************************************************************************************************************
        Task: to initialize object variables
        Inputs:
            _filename: string containing the name of the vcf file
        *******************************************************************************************************************************************"""
        self.filename = _filename
        self.sample = None
        self.status = None
    
    
    def nvariants(self):
        fd = file(self.filename)
        self.skip_header(fd)      
        header = fd.readline()
        variants = 0
        for line in fd:
            parts = line.split('\t')

            if(parts[4]<>'.'): 
                variants += 1
                                    
        fd.close()
        
        return variants
    
    def load_sample(self):
        fd = file(self.filename)
        self.skip_header(fd)      
        self.sample = fd.readline()[:-1].split('\t')[-1]
        fd.close()
        
        
        
    def skip_header(self, fd):
        """*******************************************************************************************************************************************
        Task: skips all those lines in the vcf starting with ##
        Inputs:
            fd: file descriptor.
        Outputs: 
            fd: the file descriptor pointing to the first character of the actual table (>>>to the header of the table<<<)
        *******************************************************************************************************************************************"""
        
        # Lines starting with ## are skipped. The file descriptor is left pointing to the first character of the first line that does not start with ##
        line = fd.readline()
        while(line.startswith('##')): line=fd.readline()
        fd.seek(-len(line), 1)
        
        return fd 
        
        
        
        
    def skip_and_write_header(self, fdin, fdout):
        line = fdin.readline()
        while(line.startswith('##')):
            fdout.write(line) 
            line=fdin.readline()
        fdin.seek(-len(line), 1)
        
        return fdin
    
    def get_variants (self, type='Normal'):
        fd=file(self.filename)
        fd=self.skip_header(fd)
        result=[]
        header=fd.readline()
        for line in fd:
            a_line=line.split("\t")
            if type=='Normal':
                aux_variant=variant.variant(a_line[0],a_line[1],a_line[3],a_line[4],a_line[7],line)       
            if type=='loh':
                aux_variant=variant.loh_variant(a_line[0],a_line[1],a_line[3],a_line[4],a_line[7],line)
            result.append(aux_variant)
        return result