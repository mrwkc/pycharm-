import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36 Edg/84.0.522.20',
    'host':'movie.douban.com'
}


movie_list=[]
for i in range(0,10):
    link = 'https://movie.douban.com/top250?start=' + str(i * 25)
    r = requests.get(link,headers=headers,timeout=10)
    #print(str(i+1),"状态码",r.status_code)

    soup =  BeautifulSoup(r.text,'lxml')
    div_list = soup.find_all('div',class_ = 'hd')

    for each in div_list:
        movie = each.a.span.text.strip()
        movie_list.append(movie)


for a in range(0,250):
    print(str(a+1)+':'+movie_list[a])
    
