'''
Created on 05/10/2013

@author: antonio
'''


import objects.LossOfHeterocigosity_region as loh_r
import objects.LossOfHeterocigosity_variant as loh_v



variant=loh_v.loh_variant("13",20001000,"A","T","AAAAAAAAA")
variant2=loh_v.loh_variant("13",20000000,"A","T","BBBBBBBB")
variant3=loh_v.loh_variant("13",19900000,"A","T","BBBBBBBB")
if variant<variant2:
    print "True"
else:
    print "False"
    
#print variant-variant2

s=[variant,variant2]
print s
print sorted(s)
if variant.check_cluster(variant2):
    print "True"
else:
    print "False"
    
region=variant.get_interval(variant2)

region.add_varinat(variant3)
region.cellbase_annotation()
print region