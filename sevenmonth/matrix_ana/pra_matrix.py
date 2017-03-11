# coding=utf8


import numpy as np

a = np.array([1, 2, 3, 4]).reshape((2, 2))

print 'a:\n',a

b = np.array([5, 6, 7, 8]).reshape((2, 2))

print 'b:\n',b

print 'a*b:\n',a*b

print 'a**b:\n', a**b