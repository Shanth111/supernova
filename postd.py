from lxml import html
import requests


payload ={'catid':'925899269','catname':'Gingercrush.com','corp':'false','fbmessage':'I+found+this+review+of+Gingercrush.com+pretty+useful','isvideo':'false','prodimg':'.jpg','rating_str':'+1/5','reviewid':'2531646','twitterlnk':'https://www.mouthshut.com/review/Gingercrush-com-review-nmnorprmoqn','twittermsg':'I+found+this+review+of+Gingercrush.com+pretty+useful+%23WriteShareWin','type':'review','usession':'0'}
r = requests.post("https://www.mouthshut.com/review/CorporateResponse.ashx", data=payload)
data = r.content
print(data)

# with open('somefile.html', 'a') as the_file:
#     the_file.write(data)