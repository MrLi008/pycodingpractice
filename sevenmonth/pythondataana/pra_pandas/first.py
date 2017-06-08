# coding=utf8

from pandas import Series, DataFrame, Index
import numpy as np


# Series: 一组数据和与之对应的索引组成


arr = range(0, 30, 3)
print arr

obj = Series(arr)
print obj



multiplication_table = np.zeros((10, 10))
multiplication_table[0] = range(0, 10)
# multiplication_table[:, 0] = range(0, 10)
multiplication_table = multiplication_table+multiplication_table.T


multiplication_table[1:, 1:] = multiplication_table[1:, 0]*multiplication_table[0, 1:]

res = [ x*y for x in range(0, 10) for y in range(x, 10) ]
res = np.reshape(np.array(res), (10,10))
print res

print multiplication_table
#
# a1 = np.array(range(0, 10, 1))
# a2 = np.array(range(0, 10, 1))
#
# print np.diff(a1, a2)


