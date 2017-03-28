# coding=utf8



import requests as req
from requests.utils import cookiejar_from_dict
from func import confirmencoding, savedata, geturloflogin,getformofpost
import pickle


url = 'http://11.2.8.45'

s = req.session()

urldata = s.post(url)
# print s.json()
headers = {'Host': '11.2.8.45',
        'Proxy-Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': 'http://11.2.8.45/Home/IndexA?ticket=ST-32303-CJRaezr1OsectYlSufDP-cas01.sxmt.org',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        }
cookies = {'JSESSIONID':'B1A8E066743220268F8439CD79452019',
           'cookiesEnabled':'true'}

s.headers.update(headers)
cookies = cookiejar_from_dict(cookies)

with open('cookie.text', 'w') as f:
    p = pickle.Pickler(file=f)
    p.dump(cookies)



s.cookies.update(cookies)
data = getformofpost(urldata.text)


urldata = req.post(url=url, data=data, json=[{'cookies':cookies,'headers':headers}],)

print urldata.headers
print urldata.cookies

urldata.encoding = confirmencoding(urldata.content)
# print urldata.text
savedata('csdn/login.html',urldata.text, urldata.encoding)