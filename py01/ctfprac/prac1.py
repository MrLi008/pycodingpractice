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
headers = response.headers
cookies = response.cookies

data = {
    'id':'id','submit':'submit'
}

response = sess.post(url,data=data,headers=headers,cookies=cookies)
print (response)
print (response.text)
print (response.headers)
print (response.cookies)


if __name__ == '__main__':
    pass