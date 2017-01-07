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


max_value = 1000000

def solve(num, left_money, array_money, result):
    if left_money == 0:
        return 0
    if left_money < 0:
        return max_value
    if num >= len(array_money):
        return max_value
    if result[num, left_money] > 0:
        return result[num, left_money]

    result[num, left_money] = min(solve(num, left_money - array_money[num], array_money, result)+1,
               solve(num+1, left_money, array_money, result))
    return result[num, left_money]

    # return [solve(num+1, left_money - money, array_money)  for money in array_money]

def solve_not_recursion(total_money, array_money, result):
    result[0,0] = 0

    for i in range(len(array_money)):
        result[i,0] = 0
        j=1
        while j <= total_money:
            result[i, j] = result[i-1, j]
            if j >= array_money[i]:
                result[i, j] = min(result[i, j-array_money[i]] + 1,
                                   result[i + 1, j])
            j += 1
        print result
        i += 1

    return result[i-1, total_money]


def find_true_from_list(l):
    if isinstance(l, list):
        print 'list'
        for v in l:
            find_true_from_list(v)
    elif isinstance(l, dict):
        print 'dict', l
        if True in l.keys():
            return l.get(True)
    else:
        print 'other type'



def solve_my(values, total_money, result):
    for i in sorted(values, reverse=True):
        n = int(total_money / i)
        result.append(n)
        total_money -= n*i

    if total_money is not 0:
        return -1

    return result




if __name__ == '__main__':
    value = [ 1,2, 5]
    total_money = 130
    result = np.zeros((len(value)+1, total_money+1), dtype=np.int)
    print u'金币的个数: ', solve(0, total_money, value, result)
    print result
    # issuccess = find_true_from_list(result)
    # if issuccess is None:
    #     print -1
    # else:
    #     print issuccess
    result = list()
    print solve_my(value, total_money, result)

    result = np.zeros((len(value)+1, total_money+1), dtype=np.int)
    result[:] = max_value
    print solve_not_recursion(total_money, value, result)
