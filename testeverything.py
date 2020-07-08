import requests
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',

}
count=0
for x in range(0,100000000):
    url='https://space.bilibili.com/'+str(x)
    r=requests.get(url,headers=headers)
    if r.status_code == 200:
        count+=1

print (count)