'''
Created on 05/10/2013

@author: antonio
'''


import objects.cancer_varaint
import objects.conf_file as cf

cf1=cf.conf_file("data/conf1.txt")
print cf1.read()
print cf1.samples
print cf1.format
print cf1.params


