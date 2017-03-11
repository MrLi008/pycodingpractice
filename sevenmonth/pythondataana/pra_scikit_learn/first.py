# coding=utf8


import numpy as np
from pandas import DataFrame, Series
from matplotlib import pyplot as plt


# svd

strs = ['I like deep learning',
        'I like NLP',
        'I enjoy flying']



# 获取数据中所有出现的单词
def get_all_words_from(data):
    words = set()

    if isinstance(data, list) or isinstance(data, tuple):
        for l in data:
            strl = l.split()
            for s in strl:
                words.add(s)
    elif isinstance(data, str):
        for s in data.split():
            words.add(s)
    return [w for w in words]


# 统计某个单词俩边出现的单词的个数
def get_count_between(data, words):
    countofwords = len(words)
    X = np.zeros((countofwords, countofwords))

    series = Series(range(countofwords), index=words)
    print series

    for d in data:
        strs = d.split()
        for idx in range(len(strs)):
            try:
                X[series.get(strs[idx]), series.get(strs[idx - 1])] += 1
                X[series.get(strs[idx]), series.get(strs[idx + 1])] += 1
            except Exception,e:
                print e,'........'

    return X


# 做svd
def process(X, words):
    la = np.linalg
    U, s, Vh = la.svd(X, full_matrices=False)

    print 'U:\n', U
    print 's:\n', s
    print 'vh: \n',Vh


    plt.xlim(xmin=min(U[:,0])*1.5, xmax=max(U[:,0])*2)
    plt.ylim(ymin=min(U[:,1])*1.5, ymax=max(U[:,1])*2)


    for i in xrange(len(words)):
        print U[i,0], ' ', U[i, 1], ' ', words[i]
        plt.text(U[i, 0], U[i,1], str(words[i]))


    plt.show()




if __name__ == '__main__':
    words = get_all_words_from(strs)

    X = get_count_between(strs, words)


    print X

    process(X, words)

