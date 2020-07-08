import requests
import time

link_list=[]
with open('alexa.txt','r') as file:
    file_list=file.readlines()
    for eachone in file_list:
        link = eachone.split('\t',)[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()

for eachone in link_list:
    try:
        r =requests.get(eachone,timeout=3)
        print(r.status_code,eachone)
    except Exception as e:
        print('Error；',e)

end = time.time()

print('总时间为',end-start)