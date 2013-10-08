'''
Created on 05/10/2013

@author: antonio
'''


import objects.LossOfHeterocigosity_region as loh_r
import objects.LossOfHeterocigosity_variant as loh_v

#region=loh_r.loh_region("1",3972105,8800105,[1,2,4,6])
#region.cellbase_annotation()
#print region
#print len(region)

variant=loh_v.loh_variant(12,2,"A","T","AAAAAAAAA")
variant2=loh_v.loh_variant(11,3,"A","T","BBBBBBBB")

if variant<variant2:
    print "True"
else:
    print "False"
    
print variant-variant2

s=[variant,variant2]
print s
print sorted(s)