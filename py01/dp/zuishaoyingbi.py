# coding=utf8

'''
u'
提供给定面额不限数量的硬币
凑成给出的数值

input:
1 2 5
11
output:
5 5 2
'
'''

import numpy as np


def solve(num, left_money, array_money, result):
    if left_money == 0:
        return num
    if left_money < 0:
        return 1000000000

    return min([solve(num + 1, left_money - money, array_money, result)  for money in array_money])




def solve_my(values, total_money, result):
    for i in sorted(values, reverse=True):
        n = int(total_money / i)
        result.append(n)
        total_money -= n*i

    if total_money is not 0:
        return -1

    return result




if __name__ == '__main__':
    value = [ 2, 5]
    total_money = 11
    print solve(0, total_money, value, None)
    result = list()
    print solve_my(value, total_money, result)
