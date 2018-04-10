from lxml import html
from csv import writer
import requests

page = requests.get('https://www.mouthshut.com/online-shopping')
tree = html.fromstring(page.content)

with open('webrate.csv', 'wb') as csvfile:
    csv = writer(csvfile)
    for site_row in range(1,2):
        website = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/text()'%site_row)
        weblink = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/@href'%site_row)
        no_review = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[3]/a/text()'%site_row)
        heart = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[2]/text()'%site_row)
        star = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[1]/span/text()'%site_row)
        
        try:
            data = [website[0],weblink[0],no_review[0].split(' ')[0],heart[1].replace('%\r\n','').replace(' ',''),star[0].encode('utf-8').replace('\xc2\xa0','')]
        except IndexError:
            continue

        csv.writerow(data)



    for page_no in range(2,27):
        page = requests.get('https://www.mouthshut.com/online-shopping?page=%d'%page_no)
        tree = html.fromstring(page.content)

        for site_row in range(1,42):
            website = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/text()'%site_row)
            weblink = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/@href'%site_row)
            no_review = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[3]/a/text()'%site_row)
            heart = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[2]/text()'%site_row)
            star = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[1]/span/text()'%site_row)
            
            try:
                data = [website[0],weblink[0],no_review[0].split(' ')[0],heart[1].replace('%\r\n','').replace(' ',''),star[0].encode('utf-8').replace('\xc2\xa0','')]
            except IndexError:
                continue

            csv.writerow(data)
