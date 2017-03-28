# coding=utf8
'''
lambda
lambda in:out
map
map(function, value_list)
filter
filter(True or False, value_list)
reduce
reduce(function, value_list, default_value)
'''



# lambda
g = lambda x : x * 2
print g(5)


# map
name_len = map(len, ['afaf', 'fasdfasfa', 'asdfasdfasdfasdfa'])
print name_len

# filter
number_list = range(-5, 5)
print filter(lambda x:x<0, number_list)

# reduce
def testreduce(x,y):
    return x+y

print reduce(testreduce, range(1, 5))
print reduce(testreduce, range(1,100), 10)



# 计算平均数
import random

num = [random.randint(-100, 100) for i in range(1000)]
nums = filter(lambda x :x>=0, num)
print reduce(lambda x,y:x+y, nums)/len(nums)
sum = 0
counter = 0
for n in num:
    if(n>=0):
        sum += n
        counter += 1

print sum/counter