# -*- coding: utf-8 -*-

def table_name(site):
    table_name = site.replace('.','_').replace('-','').replace(' ','').replace('/','').replace('.csv','')
    return table_name.lower()
