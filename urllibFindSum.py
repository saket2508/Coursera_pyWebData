from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def findSum():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'http://py4e-data.dr-chuck.net/comments_240638.html'
    html = urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # retrieve data from the table
    arr = list()
    tags = soup('span')
    for tag in tags:
        num = tag.contents[0]
        arr.append(num)

    arr = list(map(int,arr))
    print(sum(arr))

if __name__ == "__main__":
    findSum()


