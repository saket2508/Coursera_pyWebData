from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def FindName():

    url = 'http://py4e-data.dr-chuck.net/known_by_Martin.html'
    html = urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    #retrieves names by following the steps below
    tags = soup('a')
    j = 0
    for j in range(7):
        c = 0
        for tag in tags:
            c+= 1
            if(c == 18):
                url= tag.get('href',None)
                html= urlopen(url,context= ctx).read()
                soup= BeautifulSoup(html,'html.parser')
                tags = soup('a')
                break
    print(tag.contents[0])






if __name__ == "__main__":
    FindName()


