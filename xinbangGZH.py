import requests
from bs4 import BeautifulSoup
import time
import json
from selenium import webdriver

'''headers={
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36 Edg/84.0.522.20',
'cookie':'UM_distinctid=171b6bf4ba02cf-0f13991b97ce6c-1b47301a-1aeaa0-171b6bf4ba1337; __root_domain_v=.newrank.cn; _qddaz=QD.xvsd3q.hjvnuo.k9h3z2ct; token=9A33BD684E70403CBEDBD51A781E0842; CNZZDATA1253878005=1243807222-1587903763-https%253A%252F%252Fwww.baidu.com%252F%7C1592985788; Hm_lvt_a19fd7224d30e3c8a6558dcb38c4beed=1592986425; _qdda=3-1.e13vn; _qddab=3-fjr4ya.kbt2zkgf; _qddamta_2852150610=3-0; Hm_lpvt_a19fd7224d30e3c8a6558dcb38c4beed=1592986891'
}
'''
url='https://www.newrank.cn/public/info/list.html?period=day&type=data'
driver = webdriver.Safari()
driver.get(url)
source=driver.page_source
time.sleep(5)
driver.quit()

bs=BeautifulSoup(source,'lxml')
for x in bs.find_all('a',class_="copyright_title"):
    b=x.get('href').split('detail.html?account=')
    print(x.get('title')+' '+b[1])
