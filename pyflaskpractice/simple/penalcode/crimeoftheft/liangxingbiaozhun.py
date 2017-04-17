# coding=utf8

import os
import docx
import re

filepath = u'F:/software/日常工具/微信/微信缓存文件'
parttern_ = re.compile(u'.*量刑标准')

res_standard = dict()


for f in os.listdir(filepath):
    res = parttern_.findall(f)
    if res not in (None, []):
        document = docx.Document(filepath+'/'+f)

        l = [ paragraphs.text for paragraphs in document.paragraphs]
        state = 1# 1 读取情节, 2 读取基准刑

        zuiming = ''
        action = ''
        for L in l:
            L = L.replace('\r\n', '')
            print L
            if len(L) == 0:
                continue
            r = parttern_.findall(L)
            if r not in (None, []):
                zuiming = r[0][:-4]
                res_standard[zuiming] = dict()

            else:
                if state == 1:
                    state = 2
                    action = L
                    res_standard[zuiming][action] = list()
                elif state == 2:
                    state = 1
                    res_standard[zuiming][action] = [float(v) for v in re.compile(u'\d+').findall(L)]



if __name__ == '__main__':
    for r in res_standard.keys():
        print r
        for rv in res_standard.get(r).keys():
            print '\t', rv, '=', res_standard.get(r).get(rv)