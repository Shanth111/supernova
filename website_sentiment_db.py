# -*- coding: utf-8 -*-

from textblob import TextBlob
from table_name import table_name
from dbconn import connection
import gc

def sentiment(site='Amazon.com'):
    table = table_name(str(site))
    print table
    
    # For Fabmart.com (old)
    if not table.__contains__('('):
        c, conn = connection()

        count_row = """SELECT COUNT(total_senti) FROM %s"""%table
        c.execute(count_row)
        row = c.fetchone()[0]
        
        senti_sum = """SELECT SUM(total_senti) FROM %s"""%table
        c.execute(senti_sum)
        senti = c.fetchone()[0]

        try:
            avg = senti/row    
        except TypeError:
            avg = 0
        
        c.close()
        conn.close()
        gc.collect()

        return(row,avg)

def review_sentiment_update(review):

    review_head = TextBlob(review[2].decode('utf-8'))
    review_data = TextBlob(review[3].decode('utf-8'))

    review_head_senti = review_head.sentiment.polarity*100
    review_data_senti = review_data.sentiment.polarity*100

    total_senti = review_head_senti + review_data_senti

    c, conn = connection()
    
    c.execute("INSERT INTO %s"%review[0]+" (webname,review_head,review_data,review_head_senti,review_data_senti,total_senti) VALUES (%s,%s,%s,%s,%s,%s)",(str(review[1]),str(review[2]),str(review[3]),review_head_senti,review_data_senti,total_senti))
    conn.commit()

    c.close()
    conn.close()
    gc.collect()




