# coding=utf8

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

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
data_frame = DataFrame(data, index=['a', 'b', 'c'])
print 'data source: \n', data_frame
print 'data index by keys: \n', data_frame[data_frame.keys().append(data_frame.keys())]
print 'DataFrame change to Series: \n', Series(data_frame['Tom'])

print 'data source length: ', len(data_frame)



