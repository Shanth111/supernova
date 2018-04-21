# -*- coding: utf-8 -*-

def table_name(site):
    table_name = site.replace('.','_').replace('-','').replace(' ','').replace('/','')
    return table_name

# For data_import_db
def table_name_csv(site):
    table_name = site.replace('.csv','').replace(' ','').replace('-','')
    return table_name.lower()