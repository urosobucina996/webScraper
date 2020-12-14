import requests as req
from modules import loggingScrape
from bs4 import BeautifulSoup as soup
# regex import
import re

#for stoping execution of scrip
from sys import exit


#my_url = 'http://web.mta.info/developers/turnstile.html'

#fake python request to be browser request HEADERS is constant

HEADERS = {'User-Agent': '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) 
                            AppleWebKit/537.36 (KHTML, like Gecko) 
                            Chrome/35.0.1916.47 Safari/537.36'''}


def parse_html(url):


    # open connection and grab pages content
    #uClient = uReq.Request(url,HEADERS)
    #url = ''
    # regex for url in test progress ^(https|http):\/\/((www)\.([a-z]+)|([a-z]+))\.([a-z]*)(\/[a-z-?=]*)*$

    if re.findall("^(http(s)?):\/\/(www\.)?((?!www)[a-z]{3,}\.[a-z]{2,})(\/[a-z-?=]*)*$",url) == []:
        print('You must enter valid url')
        loggingScrape.logging.error('Regex for url address failed.')
        exit(0)
    
    u_client = req.get(url,HEADERS)
    page_html = u_client.content

    # 301 is redirection, may couse trouble
    if u_client.status_code != 200:
        loggingScrape.logging.error(f'Invalid url address {url}.')
        print(f"Web site in not responding, server error {u_client.status_code}.")
        exit(0) 

#html parsing
# Connect to the URL
    parsed_page = soup(page_html,"html.parser")
    tag = parsed_page.body
    return tag.findAll('div',{'class':'product-inner'})