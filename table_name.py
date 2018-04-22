# -*- coding: utf-8 -*-

from csv import reader

def table_name(site):
    table_name = site.replace('.','_').replace('-','').replace(' ','').replace('/','').replace('.csv','')
    return table_name.lower()

def website_list():
    website_list = []
    with open('webrate.csv', 'rb') as f:
        r = reader(f)
        links = list(r)
        for website in links:
            website_list.append(website[0].lower())
    return(website_list)

