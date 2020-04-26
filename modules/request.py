from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#my_url = 'http://web.mta.info/developers/turnstile.html'
def parseHtml(url):

# open connection and grab pages content
    uClient = uReq(url)
    pageHtml = uClient.read()
    uClient.close()

#html parsing
# Connect to the URL
    parsedPage = soup(pageHtml,"html.parser")
    tag = parsedPage.findAll('a')
    return tag