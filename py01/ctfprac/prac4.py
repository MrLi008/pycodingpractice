#coding=utf-8
'''
    :author mrli
    :date  
    :funcname
'''
from prac3 import showresultofresponse

import requests

url = 'http://ctf5.shiyanbar.com/web/earnest/index.php'
sess = requests.session()

response = sess.get(url)
showresultofresponse(sess.headers,sess.cookies,response.content,response)

headers = sess.headers
cookies = sess.cookies
data = {
    'id':'1\'',
    'submit':'submit\'',
}
response = sess.post(url,data=data,headers=headers,cookies=cookies)
showresultofresponse(sess.headers,sess.cookies,response.content,response)




if __name__ == '__main__':
    pass