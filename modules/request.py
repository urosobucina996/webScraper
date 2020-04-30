import requests as req
from bs4 import BeautifulSoup as soup

#for stoping execution of scrip
from sys import exit


#my_url = 'http://web.mta.info/developers/turnstile.html'

#fake python request to be browser request HEADERS is constant

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def parseHtml(url):

# open connection and grab pages content
    #uClient = uReq.Request(url,HEADERS)
    url = 'https://lyrastyle.rs/category/elektricne-gitare?brands=fender'
    uClient = req.get(url,HEADERS)
    pageHtml = uClient.content

#html parsing
# Connect to the URL
    parsedPage = soup(pageHtml,"html.parser")
    tag = parsedPage.body
    return tag.findAll('div',{'class':'product-inner'})