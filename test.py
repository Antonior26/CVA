'''
Created on 05/10/2013

@author: antonio
'''

import objects.variant as variant
import objects.LossOfHeterocigosity_region as loh_r




variant1=variant.loh_variant("13",20001000,"A","T","AAAAAAAAA")
variant2=variant.loh_variant("13",20000000,"A","T","BBBBBBBB")
variant3=variant.loh_variant("13",19900000,"A","T","BBBBBBBB")
if variant1<variant2:
    print "True"
else:
    print "False"
    
#print variant-variant2

s=[variant1,variant2]
print s
print sorted(s)
if variant1.check_cluster(variant2):
    print "True"
else:
    print "False"
    
region=variant1.get_interval(variant2)

region.add_varinat(variant3)
region.cellbase_annotation()
print region