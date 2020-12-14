from datetime import datetime
import sys, getopt
from sys import exit
from modules import loggingScrape
from modules import request
from modules import database

try:
     #MAKE MAN PAGE FOR YOUR SCRIPT
     if(getopt.getopt(sys.argv,"h")[1][1] == '-h'):
          with open("man/man_page.txt") as man:
               print(man.read())
          exit(0)

     #tag = request.parseHtml('https://lyrastyle.rs/category/elektricne-gitare?brands=fender')
     tag = request.parse_html(sys.argv[1])
     rows = []
     for item in tag:
          # find all vraca niz a find ne
          single = item.find('div',{'class':'product-details'})  

          #moze da vrati none ako nije nasao price class
          if single.find('div',{'class':'price'}) is not None:
               sritp_price = single.find('div',{'class':'price'}).text[:-8] 
               casted_price = int(sritp_price.replace('.',''))
               # NEMA ZNAKOVA U BROJEVIMA 
               rows.append((single.h3.a.text,casted_price,datetime.now()))

     database.execute_query(rows)
     
except IndexError:
     loggingScrape.logging.error('User did not pass link as arugment.')
     print('Pass link.')
     exit(0)

