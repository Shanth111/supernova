from lxml import html
import requests



r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data={'reviewid': '2531646'})
data = r.content
print(r.response)

with open('somefile.html', 'a') as the_file:
    the_file.write(data)