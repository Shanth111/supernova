# -*- coding: utf-8 -*-

from table_name import table_name
from dbconn import connection
import gc

def sentiment(site='Amazon.com'):
    table = table_name(str(site))
    print table

    c, conn = connection()

    count_row = """SELECT COUNT(total_senti) FROM %s"""%table
    c.execute(count_row)
    row = c.fetchone()[0]
    
    senti_sum = """SELECT SUM(total_senti) FROM %s"""%table
    c.execute(senti_sum)
    senti = c.fetchone()[0]

    avg = senti/row    
    print(avg)

    c.close()
    conn.close()
    gc.collect()

    return(avg)

sentiment('Bookmyshow.com')

