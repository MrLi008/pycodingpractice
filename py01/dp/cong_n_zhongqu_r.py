# coding=utf8

'''
u'从n中取r个元素
输出可能的取法
输出所有组合'
使用递归时, 随着n的增加, r的取值为[n-r+1, r>n?n:r]
不使用递归实现时, 会穷举n与r的所有可能
随着n的增加, r的取值为[0,r]
'''
import numpy as np

max_n = 10
max_r = 6
result = np.zeros((max_n+1, max_r+1))


def takefrom(n, r, s=''):
    if r == 0:
        print s
        return 1
    if r == 1:
        result[n, r] = n
        return n
    if n == 0:
        return 0
    if result[n, r] > 0:
        return result[n, r]
    result[n, r] = takefrom(n-1, r-1, s+str(n-1)+str(1)+' ') + takefrom(n-1, r, s+str(n-1)+str(0) + ' ')
    return result[n, r]


def init_result(n, r):
    return np.zeros((n, r))


def takefrom_not_recursion(n, r, result):
    result[0, 0] = 0

    for n1 in range(n):
        for r1 in range(r):
            if n1 == 0 or r1 == 0:
                result[n1, r1] = 0
            elif n1 >= 1 and r1 == 1:
                result[n1, r1] = n1
            else:
                result[n1, r1] = result[n1-1, r1-1] + result[n1-1, r1]

if __name__ == '__main__':
    takefrom(max_n, max_r)
    print result.astype(dtype=np.int)
    result = init_result(max_n+1, max_r+1)
    takefrom_not_recursion(max_n+1, max_r+1, result)
    print result






