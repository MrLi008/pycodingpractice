# coding=utf8


import requests
from BeautifulSoup import BeautifulSoup



# url = 'http://www.baidu.com/'
url= 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&isadv=0&sg=4c3a8272bbd046e99594b322e7704142&p=9'
data = requests.get(url)

encoding = requests.utils.get_encodings_from_content(data.content)[0]
data.encoding = encoding

# print data.text

b = BeautifulSoup(data.text)

data = b.findAll('a', recursive=True,)
#
for d in data:
    try:
        if d['href'] not in (None, '#', r'^javascript')\
                and d.string not in (None,):
            print d['href'], '------->>>>>>>', d.string
    except KeyError, e:
        print e, ' ;;;'


print len(data)
