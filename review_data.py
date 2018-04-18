# -*- coding: utf-8 -*-

from lxml import html
from csv import writer
from csv import reader
import requests
import lxml

with open('webrate.csv', 'rb') as f:
    reader = reader(f)
    links = list(reader)



for website in links:
    link = website[1]
    file_name = 'Data/'+website[0].replace('.','_').replace('/','')+'.csv'
    with open(file_name, 'wb') as reviewfile:
        csv = writer(reviewfile)
        with requests.session() as s:
            page = s.get(link)
            tree = html.fromstring(page.content)

            site_name = tree.xpath('//*[@id="prodTitle1"]/a/text()')
            total_pages = tree.xpath('//*[@id="spnPaging"]/li[last()]/a/text()')

            cookies = requests.utils.dict_from_cookiejar(s.cookies)
            asp_id = cookies['ASP.NET_SessionId']
            imp_cookies = 'G_ENABLED_IDPS=google; ASP.NET_SessionId='+asp_id+'; _ga=GA1.2.1769419155.1521903843; _gid=GA1.2.1585595577.1523110523; _gat=1; CookieRecentVistedProducts=925899269,925903197,925917784,925028487,925076148,925000495,925038892,925054035; CookieBadge=1'
            headers = {'Cookie':imp_cookies}
            print(asp_id)

            for review_no in range(20):
                review_title = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lnkTitle"]/text()'%review_no)
                #review_name = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[1]/a/text()'%review_no)
                #place = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[2]/text()'%review_no)
                
                data = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/a/@onclick'%review_no)

                try:
                    form = data[0].split('(')
                except IndexError:
                    review = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/text()'%review_no)

                    try:
                        review_data = [site_name[0],review_title[0].encode('utf-8'),review[0].encode('utf-8').strip()]
                        csv.writerow(review_data)
                    except IndexError:
                        continue
                    continue
                
                f = form[1].split(',')
                payload ={  'reviewid':f[0].replace("'",''),
                            'corp':f[2],
                            'catid':f[4],
                            'catname':f[8].replace("'",''),
                            'type':'review'}
                
                r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data=payload, headers=headers)

                try:
                    wood = html.fromstring(r.content)
                except lxml.etree.ParserError:
                    continue

                full_review = wood.xpath('//p/text()')

                try:
                    review_data = [site_name[0],review_title[0].encode('utf-8')," ".join(full_review).encode('utf-8')]
                except IndexError:
                    continue

                csv.writerow(review_data)

                print(site_name,'1,'+total_pages[0],review_no)


        for review_page_no in range(2,int(total_pages[0])+1):
            page = s.get(link+'-page-%s'%review_page_no)
            tree = html.fromstring(page.content)
            
            for review_no in range(20):
                review_title = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lnkTitle"]/text()'%review_no)
                #review_name = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[1]/a/text()'%review_no)
                #place = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[2]/text()'%review_no)

                data = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/a/@onclick'%review_no)

                try:
                    form = data[0].split('(')
                except IndexError:
                    review = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/text()'%review_no)

                    try:
                        review_data = [site_name[0],review_title[0].encode('utf-8'),review[0].encode('utf-8').strip()]
                        csv.writerow(review_data)
                    except IndexError:
                        continue
                    continue

                f = form[1].split(',')

                payload ={  'reviewid':f[0].replace("'",''),
                            'corp':f[2],
                            'catid':f[4],
                            'catname':f[8].replace("'",''),
                            'type':'review'}
                
                r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data=payload, headers=headers)

                try:
                    wood = html.fromstring(r.content)
                except lxml.etree.ParserError:
                    continue

                full_review = wood.xpath('//p/text()')

                try:
                    review_data = [site_name[0],review_title[0].encode('utf-8')," ".join(full_review).encode('utf-8')]
                except IndexError:
                    continue

                csv.writerow(review_data)

                print(site_name,review_page_no,total_pages[0],review_no)