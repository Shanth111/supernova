from lxml import html
import requests

link = 'https://www.mouthshut.com/product-reviews/Gingercrush-com-reviews-925899269'

#r=requests.session()
page = requests.get(link)
print(page.status_code)


payload ={  'catid':'925899269',
            'catname':'Gingercrush.com',
            'corp':'false',
            'reviewid':'2328573',
            'type':'review'}

headers = {'Cookie':'G_ENABLED_IDPS=google; ASP.NET_SessionId=a1llcnozkhfbulf2i5sfhnhe; CookieRecentVistedProducts=925899269,925903197,925917784,925028487,925076148,925000495,925038892,925054035; _ga=GA1.2.1769419155.1521903843; _gid=GA1.2.1585595577.1523110523; CookieBadge=1'}

r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data=payload, headers=headers)

print(r.status_code)
print(r.text)
#print(r.content)


with open('somefile.html', 'a') as the_file:
    the_file.write(r.content)