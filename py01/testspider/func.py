# coding=utf8

import codecs
import requests as req
import BeautifulSoup as BS



def savedata(filename, filedata, encoding):
    with codecs.open(filename=filename, mode='w', encoding=encoding) as f:
        f.write(filedata)

def confirmencoding(content):
    encoding = req.utils.get_encodings_from_content(content)
    if encoding in (None, []):
        return 'utf-8'
    return encoding[0]


# 疑似表示登录
tuplelogin = (u'登录', 'logon', 'sign in', 'submit')
# 由于获取的是url, 还没有访问网站, session可在下一次访问时获取

def geturloflogin(mainpage):
    urldata = req.get(mainpage)

    urldata.encoding = confirmencoding(urldata.content)

    print urldata.text

    bs = BS.BeautifulSoup(urldata.text)


    # 页面上有登录连接

    url = bs.findAll(name='a')

    # print url

    # bs = BS.BeautifulSoup(str(url))
    # url = bs.findAll(name='a')

    # print url
    for u in url:
        print u
        if u.text in tuplelogin:
            return u['href']


    # 页面上有登录按钮
    url = bs.findAll(name='input')

    for u in url:
        print u, u['value']
        if u['value'] in tuplelogin:
            return mainpage


    return None

def getdomain(url):
    u = url.split('/')

    if u[0] in ('http', 'https'):
        return u[2]
    else:

        return u[0]

def getformofpost(urldatacontent):
    formdata = dict()
    bs = BS.BeautifulSoup(urldatacontent)

    taginput = bs.findAll(name='input')


    for tag in taginput:
        try:
            print tag
            formdata[tag['name']] = tag['value']

        except Exception, e:
            print 'something wrong.....', e
            formdata[tag['name']] = None
    return formdata