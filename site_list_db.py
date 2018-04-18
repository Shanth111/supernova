# -*- coding: utf-8 -*-

from dbconn import connection
from csv import reader
import gc
import os

# Creating Table in Database


file_name = 'webrate.csv'
table_name = 'webrate'
c, conn = connection()
c.execute("DROP TABLE IF EXISTS "+table_name)

sql = """CREATE TABLE """+table_name+\
        """(website_name VARCHAR(80) NOT NULL,\
            website_link VARCHAR(10000),\
            review_no INT,\
            heart INT,\
            star FLOAT)"""
c.execute(sql)
conn.commit()

#Importing File in Database

data =  """LOAD DATA  LOCAL INFILE '%s'"""%file_name+ """ INTO TABLE %s"""%table_name+\
        """ FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'\
        LINES TERMINATED BY '\r\n'"""
c.execute(data)
conn.commit()


c.close()
conn.close()
gc.collect()

