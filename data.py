from lxml import html
from csv import writer
import requests

page = requests.get('https://www.mouthshut.com/online-shopping')
tree = html.fromstring(page.content)

# sites = []
# links = []
links = ['https://www.mouthshut.com/product-reviews/Gingercrush-com-reviews-925899269']
# with open('webrate.csv', 'wb') as csvfile:
#     csv = writer(csvfile)
#     for i in range(1,42):
#         website = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/text()'%i)
#         weblink = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/@href'%i)
#         no_review = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[2]/div[3]/a/text()'%i)
#         try:
#             data = [website[0],weblink[0],no_review[0]]
#             sites.append(website[0])
#             links.append(weblink[0])
#         except IndexError:
#             continue

#         csv.writerow(data)




        #print(website)
    #print(links)



    # for page_no in range(2,27):
    #     page = requests.get('https://www.mouthshut.com/online-shopping?page=%d'%page_no)
    #     tree = html.fromstring(page.content)

    #     for i in range(1,42):
    #         website = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/text()'%i)
    #         weblink = tree.xpath('//*[@id="categorierightpanel"]/div/div[3]/div[1]/div[%d]/div[2]/div[1]/a/@href'%i)
    #         try:
    #             data = [website[0],weblink[0]]
    #             sites.append(website[0])
    #             links.append(weblink[0])
    #         except IndexError:
    #             continue

    #         csv.writerow(data)
    #         #print(website)

with open('review.csv', 'wb') as reviewfile:
    csv = writer(reviewfile)
    for link in links:
        page = requests.get(link)
        tree = html.fromstring(page.content)

        site_name = tree.xpath('//*[@id="prodTitle1"]/a/text()')
        page = tree.xpath('//*[@id="spnPaging"]/li[last()]/a/text()')


        # for k in range(20):
        #     #review_name = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_divProfile"]/p[1]/a/text()'%k)
        #     review_title = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lnkTitle"]/text()'%k)
        #     review = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/text()'%k)
            
            
        #     #print(page)
        #     print(site_name)
        #     # #print(review_name)
        #     # print(review_title)
        #     # print(review)

        #     try:
        #         review_data = [site_name[0],review_title[0].encode('utf-8'),review[0].encode('utf-8')]
        #     except IndexError:
        #         continue

        #     csv.writerow(review_data)
        
        
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
                    