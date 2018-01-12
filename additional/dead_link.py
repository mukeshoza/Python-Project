import httplib2
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('https://dev.conversionsondemand.com:7443/')

for link in BeautifulSoup(response, parse_Only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])