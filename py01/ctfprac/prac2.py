#coding=utf-8
'''
    :author mrli
    :date  
    :funcname
'''
import requests
sess = requests.session()
url = 'http://ctf5.shiyanbar.com/423/web/?id='
response = sess.post(url)

headers = sess.headers
cookies = sess.cookies
print (response)
print (response.content)
print (headers)
print (cookies)


response = sess.get(url+'\'%00')

headers = sess.headers
cookies = sess.cookies
print (response)
print (response.content)
print (headers)
print (cookies)
data = {
    'id':1
}

if __name__ == '__main__':
    pass