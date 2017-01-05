# coding=utf8
'''
读取文本
为70*3的二维数据

'''

import numpy as np
with open('data.txt', 'r+') as f:

    l = list()
    for data in f.readlines():
        print data
        l.append(data.split())

    print l
    res = np.array(l)
    np.save('data', res)
f = np.load('data.npy')
print f