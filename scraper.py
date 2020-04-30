from modules import request
from modules import database
from sys import exit
from datetime import datetime

tag = request.parseHtml('http://web.mta.info/developers/turnstile.html')
rows = []
for item in tag:

     # find all vraca niz a find ne
     single = item.find('div',{'class':'product-details'})  

     #moze da vrati none ako nije nasao price class
     if single.find('div',{'class':'price'}) is not None:
          sritpPrice = single.find('div',{'class':'price'}).text[:-8] 
          castedPrice = int(sritpPrice.replace('.',''))
          # NEMA ZNAKOVA U BROJEVIMA 
          rows.append((single.h3.a.text,castedPrice,datetime.now()))

database.executeQuery(rows)

