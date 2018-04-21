# -*- coding: utf-8 -*-
from table_name import table_name_csv
from dbconn import connection
from csv import reader
import gc
import os

# Creating Tables in Database

files = os.listdir('Data/Sentiment/')

for senti_file in files:
    file_name = 'Data/Sentiment/'+senti_file
    table_name = table_name_csv(senti_file)
    print(table_name)
    c, conn = connection()
    c.execute("DROP TABLE IF EXISTS "+table_name)

    sql = """CREATE TABLE """+table_name+\
          """(webname VARCHAR(80) NOT NULL,\
              review_head VARCHAR(500),\
              review_data VARCHAR(20000),\
              review_head_senti DOUBLE,\
              review_data_senti DOUBLE,\
              total_senti DOUBLE)"""
    c.execute(sql)
    conn.commit()

#Importing Files in Database

    data =  """LOAD DATA  LOCAL INFILE '%s'"""%file_name+ """ INTO TABLE %s"""%table_name+\
            """ FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'\
            LINES TERMINATED BY '\r\n'"""
    c.execute(data)
    conn.commit()
    
    
    c.close()
    conn.close()
    gc.collect()

