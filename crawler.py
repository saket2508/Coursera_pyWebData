import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
def getLinks():
    #ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'https://en.wikipedia.org/wiki/Israel%E2%80%93United_States_relations'
    html = urllib.request.urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        print(tag.get('href',None))

if __name__ == "__main__":
    getLinks()






