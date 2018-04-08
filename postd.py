from lxml import html
import requests

link = 'https://www.mouthshut.com/product-reviews/Gingercrush-com-reviews-925899269'



with requests.session() as s:
    page = s.get(link)
    tree = html.fromstring(page.content)

    for i in range(20):
        data = tree.xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%02d_lireviewdetails"]/div[2]/a/@onclick'%i)
        #print(data[0])
        form = data[0].split('(')
        #print(form)
        f = form[1].split(',')
        print(f[0].replace("'",''),f[2],f[4],f[8].replace("'",''))

        # cookies = page.cookies
        cookies = requests.utils.dict_from_cookiejar(s.cookies)
    # print(page.status_code)
        #print(cookies)
        asp_id = cookies['ASP.NET_SessionId']
        #asp_id = '4htiugzpnscxu2cmwxaemwhj'
        payload ={  'reviewid':f[0].replace("'",''),
                    'corp':f[2],
                    'catid':f[4],
                    'catname':f[8].replace("'",''),
                    'type':'review'}
        print(payload)
        # payload ={  'catid':'925899269',
        #         'catname':'Gingercrush.com',
        #         'corp':'false',
        #         'reviewid':'2328573',
        #         'type':'review'}
        
        #print(asp_id)
        cook = 'G_ENABLED_IDPS=google; ASP.NET_SessionId='+asp_id+'; _ga=GA1.2.1769419155.1521903843; _gid=GA1.2.1585595577.1523110523; _gat=1; CookieRecentVistedProducts=925899269,925903197,925917784,925028487,925076148,925000495,925038892,925054035; CookieBadge=1'
        #print(str(cook))
        headers = {'Cookie':cook}
        #print(headers)
        r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data=payload, headers=headers)

        print(r.status_code)
        print(r.text)
        #print(r.content)


        with open('somefile.html', 'a') as the_file:
            the_file.write(r.content)

