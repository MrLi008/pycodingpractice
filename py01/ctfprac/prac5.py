#coding=utf-8
'''
    :author mrli
    :date  
    :funcname
'''
import requests
from prac3 import showresultofresponse


sess = requests.session()


url = 'http://ctf5.shiyanbar.com/web/PHP/index.php'

response = sess.get(url)


headers = sess.headers
cookies = sess.cookies
showresultofresponse(headers,cookies, response.content,response)







if __name__ == '__main__':
    pass