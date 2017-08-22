# coding=utf8

import re
# partterns
a_href = re.compile('href=".*?"')

partterns = [
    a_href,
]

def loaddata(filefullpath):
    data = ''
    with open(filefullpath) as f:
        data = f.read()

    return data


def convert_to_url_from(href, **kwargs):
    if href[0] == '/':
        return kwargs['domain']+href

    if href[0:7] in ('http://', 'https:/'):
        return href

def anadata(text, domain):

    with open('temp_', 'w') as f:

        for parttern in partterns:
            print 'in parttern:', parttern
            res = parttern.findall(text)
            if res not in (None, []):
                for r in res:
                    print r,
                    # 转换成完整的url
                    fullurl = convert_to_url_from(r[6:-1], domain=domain)
                    if fullurl not in (None, ) and '/dev/peps/pep-' in fullurl:
                        f.write(fullurl + '\n')




if __name__ == '__main__':
    filefullpath = 'www.python.org/dev_peps_'
    data = loaddata(filefullpath)
    anadata(data, domain='https://'+filefullpath.split('/')[0])



