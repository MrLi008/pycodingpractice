# coding=utf8

import requests
import re
import os
import codecs

ses = requests.session()
# proxies
proxies = {
    'http':'http://localhost:55312/?utm_campaign=show-lantern&utm_content=&utm_medium=tray&utm_source=windows#/'
}
def getpicfrom(url):

    # request get data
    try:
        res = ses.get(url, proxies=proxies)
    except Exception as e:
        print e

    # confirm encoding
    try:
        encoding = requests.utils.get_encodings_from_content(res.content)[0]

    except Exception as e:
        print e, 'in get pic from....encoding'


        encoding = 'utf-8'


    res.encoding = encoding
    print 'status: ', res
    # print 'head: ', res.headers
    # print 'content: ', res.content


    # print 'request get result: ', res.text




    return res.text, encoding


def confirm_exist_(direction):
    if not os.path.exists(direction):
        os.mkdir(direction)


def loadurl(filefullpath):
    data = ''
    with open(filefullpath, 'r') as f:
        data = f.read().split()
    print data
    return data




parttern = re.compile('://.*?/')
link_a = re.compile('<a href=.*?>')
def con_filename(url):
    # 1
    direction = parttern.findall(url)
    if direction not in (None, []):
        direction = direction[0][3:-1]
    confirm_exist_(direction)
    # print 'direction: ', direction

    filename = '_'.join(url.split('/')[3:])
    # print 'filename: ', filename

    return direction,filename

def saveresult(text, filepath, encoding):
    with codecs.open(filepath, 'wb', encoding) as f:
        f.write(text)




def split_operator():
    import platform
    if platform.system() == 'Windows':
        return '\\'
    else :

        return '/'

if __name__ == '__main__':

    # url = 'http://wenshu.court.gov.cn/ValiCode/CreateCode/'
    # url = 'https://www.python.org/dev/peps/'
    urls = loadurl('temp_')
    for url in urls:
        text, encoding = getpicfrom(url)
        url_direction, url_filename = con_filename(url)
        sp = split_operator()

        saveresult(text, filepath=url_direction+sp+url_filename, encoding=encoding)


