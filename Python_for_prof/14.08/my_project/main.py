from urllib.request import Request, urlopen
from urllib.error import HTTPError

url = "https://www.zara.com/tr/tr/kadin-l1000.html?v1=1576910"

try:
    request_site = Request(url)
    webpage = urlopen(request_site).read()
    print(webpage[:500])
except HTTPError as e:
    print("Error occured!")
    print(e)
