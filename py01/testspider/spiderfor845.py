# coding=utf8


import requests as req

import BeautifulSoup as BS

import codecs


def savedata(filename, filedata, encoding):
    with codecs.open(filename=filename, mode='w', encoding=encoding) as f:
        f.write(filedata)

def confirmencoding(content):
    encoding = req.utils.get_encodings_from_content(content)
    if encoding in (None, []):
        return 'utf-8'
    return encoding[0]



url = 'http://11.2.9.11:8085/cas/login?service=http://11.2.8.45/Home/IndexA#'


s = req.session()


urldata = s.get(url)

print s.cookies

urldata.encoding = confirmencoding(urldata.content)


# print urldata.text

bs = BS.BeautifulSoup(urldata.text)

tagurlsubmit = bs.find('form')
# print tagurlsubmit
urlsubmit = tagurlsubmit['action'].split('?')[-1].split('=')[-1]

# 构建提交数据
data = dict()

taginputdata = bs.findAll('input')

for tag in taginputdata:
    data[tag['name']] = tag['value']


data['username'] = 'sxs'
data['password'] = '1'
data['_eventId'] = 'submit'


print data

# print urlsubmit



urldata = s.post(urlsubmit,data=data, cookies=s.cookies)

urldata.encoding = confirmencoding(urldata.content)

# print urldata.text
savedata('logindata845.html', urldata.text, encoding=urldata.encoding)

