'''
Created on 05/10/2013

@author: antonio
'''

import objects.cancer_varaint as cv
import objects.LossOfHeterocigosity_region as loh_r
import objects.variant as variant
import objects.vcf_file as vcf_file

def Loss_of_heterocigosity_analysis(loh_name,v_name,outfile):
    '''**************************************
    Perform a Loss of  
    **************************************'''
    loh_file=vcf_file.vcf_file(loh_name)
    v_file=vcf_file.vcf_file(v_name)
    loh_variants=loh_file.get_variants('loh')
    all_variants=v_file.get_variants()
    
    loh_variants=sorted(loh_variants)
    all_variants=sorted(all_variants)
    selected_variant=[]
    selected_loh_region=[]
    loh_regions=[]
    #aux_region=''
    cluster=False
    
    for i,loh in enumerate(loh_variants):
        
        if cluster==False and loh.check_cluster(loh_variants[i+1]):
            aux_region=loh.get_interval(loh_variants[i+1])
            cluster=True
        
        elif cluster==True:
            if aux_region.check_variant_cluster(loh):
                aux_region.add_varinat(loh)
        
            else:
                cluster=False
                loh_regions.append(aux_region)
    
    if cluster==True:
        cluster=False
        loh_regions.append(aux_region)
    
    for site in all_variants:
        if site.check_filter('PASS') and site.line.find('0/1'):
            selected_variant.append(site)
    
    for region in loh_regions:
        flag=True
        limit=len(selected_variant)
        i=0
        while i<limit and flag==True:
            if region.check_variant_cluster(selected_variant[i]):
                flag=False
            i=i+1
        if flag==True:
            region.cellbase_annotation()
            selected_loh_region.append(region)
    
    fdw=file(outfile,'w')    
    fdw.write("chromosome\tstart\tend\tlength\tnumber_of_loh_sites\tGenID\tGene_Name\tDescription\n")
    for region in selected_loh_region:
        fdw.write(str(region)+'\n')
        
        
    
    
            