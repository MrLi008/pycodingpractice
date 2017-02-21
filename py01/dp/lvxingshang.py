# coding=utf8


'''
一个商人不重复访问n个城市,
从任意城市出发
到任意城市结束
已知任意俩城市之间的道路长度

求商人走过的最短路程
'''


import random
import numpy as np



n = 3
arr_length = np.random.randint(1, 5, size=(n,n))

visit = np.zeros(n).astype(dtype=np.bool)

arr_length = arr_length+arr_length.T
for i in range(n):
    arr_length[i, i] = 0
print 'array length: '
print arr_length


def solve(city_from, count, city_length):

    if count >= n:
        return 0

    print visit

    length_min = 1000000000
    for i in range(n):
        if visit[i] == False:
            visit[i] = True
            another = solve(i, count+1, city_length) + city_length[city_from, i]
            if another < length_min:
                length_min = another
            visit[i] = False

    return length_min

def solve_removce_redundance(city_from, count, city_length):

    if count >= n:
        return 0

    print visit

    length_min = 1000000000
    for i in range(n):
        if visit[i] == False:
            visit[i] = True
            another = solve_removce_redundance(i, count+1, city_length) + city_length[city_from, i]
            if another < length_min:
                length_min = another
            visit[i] = False

    return length_min


if __name__ == '__main__':


    print solve(0, 0, arr_length)
    print solve_remove_redundance(0, 0, arr_length, visit)