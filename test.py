'''
Created on 05/10/2013

@author: antonio
'''

import objects.variant_tools as vt
import methods
import optparse
import sys
import objects.utilis as utilis

loh=sys.argv[1]
vcf=sys.argv[2]
prefix=sys.argv[3]
name=sys.argv[4]

methods.Loss_of_heterocigosity_analysis(loh,vcf,prefix,name)






#pro=vt.varaint_tools("/home/antonior/vtools_projects/test3")
#pro.add_file('/home/antonior/python/Scripts/Cancer_Variant_Annotation/data/Melanoma2_1.filtered.vcf', "M1")
#pro.consequence_annotation()
#pro.annotation("dbSNP")
#pro.annotation("refGene")
#pro.annotation("evs-6500")
#pro.annotation("thousandGenomesEBI")
#pro.annotation("CosmicCodingMuts")
#pro.output("annotation", True)
#pro.output("annotation", False)
#listoftyoes=['TEXT','INT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','REAL','TEXT','REAL','REAL','REAL','REAL','REAL','REAL']


#a=utilis.sqlite('/home/antonior/tmp/prueba_exonic')
#a.connect()
#print a.tabtosqlite("sample",'/home/antonior/tmp/vtools/result_exonic.txt', listoftyoes)
#a.conn.close()



#tableExonic=utilis.table('/home/antonior/tmp/vtools/result_exonic.txt')
#tableExonic.tabletosqlite('/home/antonior/tmp/prueba_exonic', "sample",listoftyoes)
