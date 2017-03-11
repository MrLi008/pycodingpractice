# coding=utf8


import requests as req




def savedata(filename, filedata):
    with open(filename, 'w') as f:
        f.write(filedata)



url = "http://127.0.0.1:5000/auth/login"
data={'email':'952934650@qq.com',
      'password':'123456'}

urldata = req.post(url, data=data)

encoding = req.utils.get_encodings_from_content(urldata.content)

print encoding

if encoding in (None, []):
    encoding = 'utf-8'
else:
    encoding = encoding[0]

urldata.encoding = encoding

savedata(filename='logindata.html', filedata=urldata.text)