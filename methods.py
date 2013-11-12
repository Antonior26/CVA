'''
Created on 05/10/2013

@author: antonio
'''

import objects.cancer_varaint as cv
import objects.LossOfHeterocigosity_region as loh_r
import objects.variant as variant
import objects.vcf_file as vcf_file
import objects.utils as utils

def Loss_of_heterocigosity_analysis(loh_name,v_name,prefix,sample):
    '''**************************************
    Perform a Loss of  function analisis
    **************************************'''
    #initialize loh_file
    loh_file=vcf_file.vcf_file(loh_name)
    #initialize vcf_file(gatk)
    v_file=vcf_file.vcf_file(v_name)
    
    #get variants
    loh_variants=loh_file.get_variants('loh')
    all_variants=v_file.get_variants()
    #sorted varints
    loh_variants=sorted(loh_variants)
    all_variants=sorted(all_variants)
    
    selected_variant=[]
    selected_loh_region=[]
    loh_regions=[]
    #aux_region=''
    cluster=False
    
    #look for clusters
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
        
    #select pass and ht variants
    for site in all_variants:
        if site.check_filter('PASS') and site.line.find('0/1'):
            selected_variant.append(site)
    
    #select final regions 
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
    
    fdw=file(prefix+'.txt','w')    
    fdw.write("chromosome\tstart\tend\tlength\tnumber_of_loh_sites\tGenID\tGene_Name\tDescription\n")
    for region in selected_loh_region:
        fdw.write(str(region)+'\n')
    fdw.close()
    
    listoftyoes=['TEXT','INT','INT','INT','INT','TEXT','TEXT','TEXT']
    table=utils.table(prefix+'.txt')
    table.tabletoxls(prefix,sample)
    table.tabletosqlite(prefix,sample,listoftyoes)
    
    
    

     
    
    
            