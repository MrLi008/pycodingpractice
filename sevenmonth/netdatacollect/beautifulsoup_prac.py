# coding=utf8


import requests
from BeautifulSoup import BeautifulSoup



# url = 'http://www.baidu.com/'
url= 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&isadv=0&sg=4c3a8272bbd046e99594b322e7704142&p=9'
data = requests.get(url)

encoding = requests.utils.get_encodings_from_content(data.content)[0]
data.encoding = encoding

print data.text

b = BeautifulSoup(data.text)

data = b.find('div', {'class':'db_nav'})

for d in data.a.next_siblings:
    print d, '..........'


    b2 = BeautifulSoup(d)
    data2 = b2.findAll('a')
    for d2 in data2:
        print d2

print len(data)