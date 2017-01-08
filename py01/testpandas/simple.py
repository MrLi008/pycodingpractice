# coding=utf8

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import time

# Series


# print pd
# print Series
# print DataFrame


obj = Series([1, 2, 3, 4, 5, 6])
print obj
print obj.values
print obj.index

length_obj = 10
index_obj = [chr(x+ord('a')) for x in range(10)]
print index_obj

obj = Series(np.random.random(length_obj), index=index_obj)
print obj
print obj*obj
# print obj[obj > 0]
print obj*obj+obj


obj1 = Series(['Bob', 'Tom', 'Jarry'], index=[1, 2, 3])
obj2 = Series(['Bob', 'Tom', 'Jarry'], index=[3, 2, 1])
print obj1+obj2


# DataFrame
# 取值当时: 按照数据源的keys取值
# 长度指: 通过keys取得的values的长度
data = {'Tom': ['a', 'b', 'c'],
        'Bob': ['d', 'e', 'f']}
data_frame = DataFrame(data, index=[1, 2, 3])
print 'data source: \n', data_frame
print 'data index by keys: \n', data_frame[data_frame.keys().append(data_frame.keys())]
print 'DataFrame change to Series: \n', Series(data_frame['Tom'])

print 'data source length: ', len(data_frame)

data = {'Tom': Series(['a', 'b', 'c'], index=[1, 2, 3]),
        'Bob': ['d', 'e', 'f', 'g']}
data_frame = DataFrame(data, index=[1, 2, 3, 4], columns=['tom', 'Bob', 'haha', 'Tom'])
# print 'data source: \n', data_frame
# data = {'Tom': ['a', 'b', 'c'],
#         'Bob': ['d', 'e', 'f', 'g']}
# time.sleep(1)
# data_frame = DataFrame(data, index=[1, 2, 3, 4], columns=['tom', 'Bob', 'haha', 'Tom'])
print 'data source: \n', data_frame



data = {1:2, 3:{4:5,6:7}}
data_frame = DataFrame(data)
print 'data source: \n', data_frame
print 'T: \n', data_frame.T
data_frame.index.name = 'indexname'
data_frame.columns.name = 'state'
data_frame.get(1).name = 'name of 4'
print data_frame
print data_frame[1].name

print 'data source: \n', data_frame

print data_frame.columns
print data_frame.index


# Series reindex(重建索引)

index_obj = ['a', 'b', 'c', 'd']
obj = Series([10, 20, 30, 40], index=index_obj)

print obj
obj2 = obj.reindex(index_obj[::-1])
print obj2

obj3 = obj.reindex(index_obj[::-1]+['f'], fill_value=0)
print obj3
print 'object 4:'
obj4 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj4 = obj4.reindex(range(6), method='ffill')
print obj4

data = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['o', 't', 'c'])
print data

data2 = data.reindex(['a', 'b', 'c', 'd'], method='ffill')
print data2

# Series
obj5 = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print obj5
obj5 = obj5.drop('c')
print obj5

# DataFrame
data3 = DataFrame(np.arange(16).reshape((4,4)),
                  index=['O', 'C', 'U', 'N'],
                  columns=['one', 'two', 'four', 'three'])
print data3.drop(['C', 'N'])

print data3

print data3.drop('two', axis=1)
print data3.drop(['two', 'four'], axis=1)






















