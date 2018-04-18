# -*- coding: utf-8 -*-

from table_name import table_name
from dbconn import connection
from website_sentiment_db import sentiment
from csv import reader
from csv import writer
import gc
import os

file_name = 'webrate.csv'

with open('webrate.csv', 'rb') as f:
    reader = reader(f)
    datas = list(reader)

with open('all_data.csv', 'wb') as csvfile:
    csv = writer(csvfile)
    csv.writerow(['Website Name','review_no','actual review_no','total_Sentiment','avg_senti','Heart','Star'])
    for data in datas:
        senti = sentiment(data[0])
        try:
            avg = senti[0]/senti[1]
        except TypeError :
            avg = 0
        csv.writerow([data[0],data[2],senti[1],senti[0],avg,data[3],data[4]])