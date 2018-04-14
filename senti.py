# -*- coding: utf-8 -*-

from textblob import TextBlob
from csv import reader
from csv import writer
import os


files = os.listdir('Data/review_data')

for page in files:
    file_name = 'Data/Sentiment/'+page
    with open(file_name,'wb') as final:
        csv = writer(final)
        
        print(file_name)
        with open('Data/review_data/'+page,'rb') as reviewfile:
            read_f = reader(reviewfile)
            data = list(read_f)



            for d in data:
                review = TextBlob(d[2].decode('utf-8'))
                review_head = TextBlob(d[1].decode('utf-8'))
                #lang = review.detect_language()
                
                header_senti = review_head.sentiment.polarity*100
                review_senti = review.sentiment.polarity*100
                total_senti = header_senti+review_senti
                

                csv.writerow([d[0],d[1],d[2],round(header_senti,2),round(review_senti,2),round(total_senti,2)])
