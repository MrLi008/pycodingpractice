# coding=utf8



# 扫描 11.2.8.0-255:0-65535
# 查找能接受http请求的结果
# 并将结果保存



import requests as req

import codecs

import threading

from func import savedata, confirmencoding

def geturldata(url, ip, port):
    flag = False
    try:

        urldata = req.get(url, timeout=1)

        urldata.encoding = confirmencoding(urldata.content)

        savedata(str(ip) + '_' + str(port) + '.html', urldata.text, urldata.encoding)
        flag = True
    except Exception, e:
        print '.',

    return flag


def geturlport(ip):
    for port in range(1, 65535):

        url = 'http://11.2.8.' + str(ip) + ':' + str(port) + '/'

        # print url
        t = threading.Thread(target=geturldata, args=(url,ip, port))
        t.setDaemon(False)

        t.start()

    print '.',port,ip



for i in range(1,255):
    print '______'
    t2 = threading.Thread(target=geturlport,args=(i,))
    t2.setDaemon(False)

    t2.start()





print 'all over!'





