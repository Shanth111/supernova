from lxml import html
from csv import writer
import requests

page = requests.get('https://www.mouthshut.com/online-shopping')
tree = html.fromstring(page.content)

sites = []
links = []

with open('webrate.csv', 'wb') as csvfile:
    csv = writer(csvfile)
    for i in range(1,42):
        website = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/text()'%i)
        weblink = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/@href'%i)
        no_review = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[3]/a/text()'%i)
        try:
            data = [website[0],weblink[0],no_review[0]]
            sites.append(website[0])
            links.append(weblink[0])
        except IndexError:
            continue

        csv.writerow(data)




        #print(website)
    #print(links)



    for page_no in range(2,27):
        page = requests.get('https://www.mouthshut.com/online-shopping?page=%d'%page_no)
        tree = html.fromstring(page.content)

        for i in range(1,42):
            website = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/text()'%i)
            weblink = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/@href'%i)
            try:
                data = [website[0],weblink[0]]
                sites.append(website[0])
                links.append(weblink[0])
            except IndexError:
                continue

            csv.writerow(data)
    #         #print(website)

with open('review.csv', 'wb') as reviewfile:
    csv = writer(reviewfile)
    for link in links:
        with requests.session() as s:
            page = s.get(link)
            tree = html.fromstring(page.content)

            site_name = tree.xpath('//*[@id="prodTitle1"]/a/text()')
            page = tree.xpath('//*[@id="spnPaging"]/li[last()]/a/text()')

            for k in range(20):
                #review_name = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[1]/a/text()'%k)
                review_title = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lnkTitle"]/text()'%k)
                #review = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/text()'%k)
                
                data = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/a/@onclick'%k)
                try:
                    form = data[0].split('(')
                except IndexError:
                    review = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/text()'%k)
                    try:
                        review_data = [site_name[0],review_title[0].encode('utf-8'),review[0].encode('utf-8')]
                        csv.writerow(review_data)
                    except IndexError:
                        continue
                    continue
                
                f = form[1].split(',')
                cookies = requests.utils.dict_from_cookiejar(s.cookies)
                asp_id = cookies['ASP.NET_SessionId']
                print(asp_id)
                payload ={  'reviewid':f[0].replace("'",''),
                            'corp':f[2],
                            'catid':f[4],
                            'catname':f[8].replace("'",''),
                            'type':'review'}
                
                imp_cookies = 'G_ENABLED_IDPS=google; ASP.NET_SessionId='+asp_id+'; _ga=GA1.2.1769419155.1521903843; _gid=GA1.2.1585595577.1523110523; _gat=1; CookieRecentVistedProducts=925899269,925903197,925917784,925028487,925076148,925000495,925038892,925054035; CookieBadge=1'
                headers = {'Cookie':imp_cookies}
                r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data=payload, headers=headers)

                wood = html.fromstring(r.content)
                full_review = wood.xpath('//p/text()')

                #print(page)
                print(site_name)
                # #print(review_name)
                # print(review_title)
                # print(review)

                try:
                    review_data = [site_name[0],review_title[0].encode('utf-8'),full_review[0].encode('utf-8')]
                except IndexError:
                    continue

                csv.writerow(review_data)
        
        
        # for k in range(2,int(page[0])+1):
        #     page = requests.get(link+'-page-%s'%k)
        #     tree = html.fromstring(page.content)
        #     for k in range(20):
        #         #review_name = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[1]/a/text()'%k)
        #         review_title = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lnkTitle"]/text()'%k)
        #         review = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/text()'%k)
        #         # print(site_name)
        #         # #print(review_name)
        #         # print(review_title)
        #         # print(review)

        #         try:
        #             review_data = [site_name[0],review_title[0].encode('utf-8'),review[0].encode('utf-8')]
        #         except IndexError:
        #             continue

        #         csv.writerow(review_data)
                    