'''
Created on 05/10/2013

@author: antonio
'''

class conf_file:
    '''
    This class has methods to handle configure file
    '''


    def __init__(self, filepath=None):
        '''***************************
        Constructor
        ***************************'''
        self.ifile=filepath
        self.format='vcf'
        self.params={}
        self.samples={}
        
    def read(self):
        '''***************************
        Task: Read Configure File
        ***************************'''
        fd=file(self.ifile)
        for line in fd:
            if line[0]!='#':
                aline=line[:-1].split('\t')
                if aline[0]=='FORMAT':
                    self.format=aline[1]
                    samples=list(aline[2:])
                    for i,s in enumerate(samples):
                        try:
                            self.samples[s].append(i)     
                        except:
                            self.samples[s]=[i]
                else:
                    try:
                        if len(aline)==3:
                            aux=(aline[1],aline[2])
                            self.params[aline[0]]=aux
                    except:
                        continue



                            
                        
        
    
    
                
            
        
        