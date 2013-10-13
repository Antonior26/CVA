'''
Created on 05/10/2013

@author: antonio
'''

import objects.cancer_varaint as cv
import objects.LossOfHeterocigosity_region as loh_r
import objects.variant as variant
import objects.vcf_file as vcf_file

def Loss_of_heterocigosity_analysis(loh_name,v_name):
    loh_file=vcf_file.vcf_file(loh_name)
    v_file=vcf_file.vcf_file(v_name)
    loh_variants=loh_file.get_variants('loh')
    all_variants=v_file.get_variants()
    
    loh_variants=sorted(loh_variants)
    all_variants=sorted(all_variants)
    loh_regions=[]
    
    cluster=False
    for i,loh in  enumerate(loh_variants):
        
        if cluster==False and loh.check_cluster(loh_variants[i+1]):
            aux_region=loh.get_interval(loh_variants[i+1])
            cluster=True
        
        elif cluster and aux_region.check_variant_cluster(variant):
            aux_region.add_varinat(variant)
        
        else:
            cluster==False
            loh_regions.append(aux_region)      
        
        
    
    
            