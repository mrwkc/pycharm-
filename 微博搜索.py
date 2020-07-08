import urllib3
import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook

#标签批量搜索
def tag_search(text):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        'Cookie: SINAGLOBAL=5671536165295.199.1576468457320; UOR=,,login.sina.com.cn; _s_tentry=login.sina.com.cn; Apache=7826497085699.521.1593999590505; ULV=1593999590519:9:2:1:7826497085699.521.1593999590505:1593739314638; login_sid_t=b5b8d03cf96a46915054eaea6866e619; cross_origin_proto=SSL; SCF=AnPtvZqpp2CTe0EZN4Kx4HSoTW9K-0LErdJKafODj7-rRN7K7uh56k9h7ibSCdqP1NNuFAxa6c9iNHU8MrNpeYk.; SUB=_2A25yBvE1DeRhGeBG7FIW-SnEwz-IHXVRcmX9rDV8PUNbmtAKLVSgkW9NQekj6l98lr4p_RMuNFg7pFGa7JD0UvgH; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5s-JhbyUNj2_0URbNskXe65JpX5KzhUgL.FoqRS05N1KMR1he2dJLoI05pehnLxK-L12qLBoMLxKqLBo5LBoBLxK-L1hqL1-zLxKqL12qL1K5LxKML1-BLBKet; SUHB=0wnFB544UwTlr4; ALF=1625535716; SSOLoginState=1593999717; wvr=6; webim_unReadCount=%7B%22time%22%3A1594001058815%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
    }
    count = 0 #定义总数量
    for x in range(50):
        url = 'https://s.weibo.com/user/&tag=' + text + '&page=' + str(x)  # 标签
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'lxml')
        weibo_card = bs.find_all('div', class_='card card-user-b s-pg16 s-brt1')
        num = len(weibo_card)  # 一页的账号数量

        for i in range(0,num):
            print('序号：'+str(count+i+1))
            print(weibo_card[i].find('div',class_='info').find('a').get_text()) #名称
            print('https:'+weibo_card[i].find('div',class_='info').find('a')['href'])    #链接

            for y in range(len(weibo_card[i].find_all('p'))):
                print(weibo_card[i].find_all('p')[y].get_text().strip())

            print('=================================')

        count +=num

#昵称相关搜索
def name_search(text):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                      'Cookie: SINAGLOBAL=5671536165295.199.1576468457320; UOR=,,login.sina.com.cn; _s_tentry=login.sina.com.cn; Apache=7826497085699.521.1593999590505; ULV=1593999590519:9:2:1:7826497085699.521.1593999590505:1593739314638; login_sid_t=b5b8d03cf96a46915054eaea6866e619; cross_origin_proto=SSL; SCF=AnPtvZqpp2CTe0EZN4Kx4HSoTW9K-0LErdJKafODj7-rRN7K7uh56k9h7ibSCdqP1NNuFAxa6c9iNHU8MrNpeYk.; SUB=_2A25yBvE1DeRhGeBG7FIW-SnEwz-IHXVRcmX9rDV8PUNbmtAKLVSgkW9NQekj6l98lr4p_RMuNFg7pFGa7JD0UvgH; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5s-JhbyUNj2_0URbNskXe65JpX5KzhUgL.FoqRS05N1KMR1he2dJLoI05pehnLxK-L12qLBoMLxKqLBo5LBoBLxK-L1hqL1-zLxKqL12qL1K5LxKML1-BLBKet; SUHB=0wnFB544UwTlr4; ALF=1625535716; SSOLoginState=1593999717; wvr=6; webim_unReadCount=%7B%22time%22%3A1594001058815%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
    }
    count = 0  # 定义总数量
    for x in range(50):
        url = 'https://s.weibo.com/user?q=' + text + '&Refer=weibo_user&page=' + str(x)  # 找人
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'lxml')
        weibo_card = bs.find_all('div', class_='card card-user-b s-pg16 s-brt1')
        num = len(weibo_card)  # 一页的账号数量

        for i in range(0, num):
            print('序号：' + str(count + i + 1))
            print(weibo_card[i].find('div', class_='info').find('a').get_text())  # 名称
            print('https:' + weibo_card[i].find('div', class_='info').find('a')['href'])  # 链接

            for y in range(len(weibo_card[i].find_all('p'))):
                print(weibo_card[i].find_all('p')[y].get_text().strip())

            print('=================================')

        count += num

if __name__ == '__main__':
    text = input("输入搜索内容：")
    tag_search(text)
    name_search(text)