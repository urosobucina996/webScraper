from modules import request
from modules import database
from sys import exit
from datetime import datetime
import sys, getopt

try:
     #MAKE MAN PAGE FOR YOUR SCRIPT
     if(getopt.getopt(sys.argv,"h")[1][1] == '-h'):
          print("Man page for scraper script")
          exit(0)
     
     #tag = request.parseHtml('https://lyrastyle.rs/category/elektricne-gitare?brands=fender')
     tag = request.parseHtml(sys.argv[1])
     rows = []
     for item in tag:
          print(tag)
          # find all vraca niz a find ne
          single = item.find('div',{'class':'product-details'})  

          #moze da vrati none ako nije nasao price class
          if single.find('div',{'class':'price'}) is not None:
               sritpPrice = single.find('div',{'class':'price'}).text[:-8] 
               castedPrice = int(sritpPrice.replace('.',''))
               # NEMA ZNAKOVA U BROJEVIMA 
               rows.append((single.h3.a.text,castedPrice,datetime.now()))

     database.executeQuery(rows)
     
except IndexError:
     print('Pass link.')
     exit(0)

