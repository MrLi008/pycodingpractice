# coding=utf8


import requests as req
import BeautifulSoup as bs
import codecs




def savedata(filename, filedata, encoding):
    with codecs.open(filename=filename, mode='w', encoding=encoding) as f:
        f.write(filedata)

def confirmencoding(content):
    encoding = req.utils.get_encodings_from_content(content)
    if encoding in (None, []):
        return 'utf-8'
    return encoding[0]



url = "http://192.168.1.106:801/auth/login"
# data={'email':'952934650@qq.com',
#       'password':'123456'}

# urldata = req.post(url, data=data)
s = req.session()
urldata = s.get(url)
print '....'
print '....'
encoding = req.utils.get_encodings_from_content(urldata.content)

urldata.encoding = confirmencoding(urldata.content)

# savedata(filename='logindata.html', filedata=urldata.text)
# print urldata.text



urlbs = bs.BeautifulSoup(urldata.text)

postdata = dict()

csrf_token = urlbs.find('input', {'id':'csrf_token','name':'csrf_token'})

postdata['csrf_token'] = csrf_token['value']
postdata['email'] = '952934650@qq.com'
postdata['password'] = '123456'

print postdata

urldata = s.post(url, data=postdata)


urldata.encoding = confirmencoding(urldata.content)

savedata(filename='logindatawithcsrf.html', filedata=urldata.text, encoding=urldata.encoding)


