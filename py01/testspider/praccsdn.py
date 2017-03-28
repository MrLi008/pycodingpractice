# coding=utf8


# spider csdn


import requests as req
import BeautifulSoup as BS
from func import confirmencoding, savedata, geturloflogin, getdomain, getformofpost

# url = 'http://11.2.8.45'
# url = 'http://www.baidu.com'
# url = 'https://www.julyedu.com/'
# url = 'https://help.aliyun.com/knowledge_detail/37557.html'
# url = 'http://www.2cto.com/article/201312/261794.html'
url = 'http://www.tuicool.com/articles/RNFVrm'
urllogin = geturloflogin(url)
print 'login url: ', urllogin

s = req.session()

urldata = s.get(urllogin)

urldata.encoding = confirmencoding(urldata.content)

# print urldata.text

savedata(filename='csdn/logintuicool.html', filedata=urldata.text, encoding=urldata.encoding)

# 获取表单以及表单中需要提交的信息



loginformdata = getformofpost(urldata.text)

for k in loginformdata.keys():
    print k,':', loginformdata.get(k)






























































# urldata = req.get(url)
#
# urldata.encoding = confirmencoding(urldata.content)
#
# savedata(filename='csdn/index.html', filedata=urldata.text, encoding=urldata.encoding)
#
#
#
# bs = BS.BeautifulSoup(urldata.text)
#
# url = bs.find(attrs={'id':'login'})
#
# print url
#
# bs = BS.BeautifulSoup(str(url))
# url = bs.findAll(name='a', )
#
# print url
# #
# # marklogin = u'登录'
# # partten = re.compile(marklogin)
#
#
#
# for u in url:
#     # print u, type(u)
#     #
#     # print partten.findall(u)
#     if u.text in (u'登录',):
#         print u['href']





