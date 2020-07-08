import requests
import bs4
from bs4 import BeautifulSoup

url = "https://s.weibo.com/top/summary?cate=realtimehot"
try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
        # print(tds[1].a)
            print("{}\t{}\t{}\thttps://s.weibo.com/{}\n".format(tds[0].string, tds[1].a.string, tds[2].string,
                                                            tds[1].a.get('href')))
except:
    print("wrong")
