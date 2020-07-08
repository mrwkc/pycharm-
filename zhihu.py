import requests
from bs4 import BeautifulSoup
import time

headers={
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36 Edg/84.0.522.20',
'cookie':'_zap=12f9d542-7983-46d5-ba2a-5f6e99cb9df3; d_c0="APDTN9smLRGPTqzmZxyKB6d7LZynO0m7BEw=|1587867860"; _ga=GA1.2.1377828477.1587867861; q_c1=0485d82bccc1444d8142b6fc64e93c4e|1590562187000|1587882475000; _xsrf=8bXzXOJQ5JLfIW2IBNZ6QAeV67n0Wmiw; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1592315925,1592448120,1592709763,1592891553; _gid=GA1.2.1511016741.1592891554; tst=h; tshl=; SESSIONID=1VyR5fiuOs2wsoZAyT9vA80Rw5xCAxowEMeJu6pyT9P; JOID=Vl4dCkxT4gy07IL5dF4TVvRLsYBpYLp06NrmngAfkzDCke6hO1478uftjvZ71xQCc5nEPs959R3yABp7poKRnu8=; osd=W10VBUJe4QS74o_6fFEdW_dDvo5kY7J75tfllg8RnjPKnuCsOFY0_Oruhvl12hcKfJfJPcd2-xDxCBV1q4GZkeE=; capsion_ticket="2|1:0|10:1592961223|14:capsion_ticket|44:NGJmZDEzMmUwZWIzNDUwMTgxODkxMjM5MDg0OWU5OGU=|9ed2449db421a4fc841377022b6d405c6e59446ef4d176003395992844368ae8"; z_c0="2|1:0|10:1592961251|4:z_c0|92:Mi4xaUxLQ0FnQUFBQUFBOE5NMzJ5WXRFU1lBQUFCZ0FsVk40X2JmWHdCNUJuVnhydFh3NnBlSmg4cTloLWtFZUxOSmFn|3819c596638f3d091309a1ecf5e053e0c6a6d5203f6c1b7f84f80a202c67bf9e"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1592961253; KLBRSID=b33d76655747159914ef8c32323d16fd|1592961253|1592961223; _gat_gtag_UA_149949619_1=1'
}

hot_list=['https://www.zhihu.com/hot','https://www.zhihu.com/hot?list=science','https://www.zhihu.com/hot?list=digital']

for i in range(0,3):
    r = requests.get(hot_list[i],headers=headers)
    r.encoding = r.apparent_encoding
    print(r.status_code)

    bs = BeautifulSoup(r.text,'lxml')
    count = 1
    for b in bs.find('div',class_="HotList-list"):
        print(str(count)+' '+b.a.get('title')+'\n'+b.a.get('href'))
        count +=1

    end = time.time()
