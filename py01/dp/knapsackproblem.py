# coding=utf8

'''
u'
在容量为W的背包中
装入许多质量为w1, 价值为v1的物品
求价值最大值

'
u'
思路总结:
    1, 寻找边界值 index<0 or left_weight< array_weight(index)
    2, 处理当前即index处的物品---> 选或者不选
'

'''
import numpy as np


def solve(index, left_weight, array_weight, array_value, result):
    # print index, '\\', left_weight, '\\', array_weight[index]
    if index < 0:
        return 0
    if array_weight[index] > left_weight:
        return solve(index - 1, left_weight, array_weight, array_value, result)
    if result[index, left_weight] > 0:
        return result[index, left_weight]

    result[index, left_weight] = max(solve(index - 1, left_weight, array_weight, array_value, result),
                        solve(index - 1, left_weight - array_weight[index], array_weight, array_value, result) + array_value[index])

    # print result, '\n'

    # print 'value: ', result[index]
    return result[index][left_weight]



def solve_not_recursion(total_weight, array_weight, array_value, result):


    # if only one stone
    result[0][0] = 0
    # if only two or more stones
    i = 0
    while i < len(array_weight):
        result[i][0] = 0
        j=1
        while j <= total_weight:
            result[i, j] = result[i-1, j]
            if j >= array_weight[i]:
                result[i, j] = max(result[i, j],
                                   result[i-1, j - array_weight[i]] + array_value[i])

            j += 1
        i += 1

    return result[i-1, total_weight]



if __name__ == '__main__':
    total_weight = 5000
    length_stone = 50
    array_weight = np.random.randint(1, total_weight, length_stone, np.int)
    array_value = np.random.randint(1, 100, length_stone, np.int)
    # array_weight = [2, 3, 2, 2, 1]
    # array_value = [8, 5, 7, 4, 7]
    result = np.zeros((len(array_weight)+1,total_weight+1))
    print 'recursion: \n', solve(len(array_weight)-1, total_weight, array_weight, array_value, result)
    print 'total weight: ', total_weight
    print 'length_stone: ', length_stone
    print 'array weight: ', array_weight
    print 'array_value:  ', array_value
    print 'result: \n', result


    result = np.zeros((len(array_weight)+1, total_weight+1))
    print 'not recursion: \n', solve_not_recursion(total_weight, array_weight, array_value, result)
    print 'total weight: ', total_weight
    print 'length_stone: ', length_stone
    print 'array weight: ', array_weight
    print 'array_value: ', array_value
    print 'result: \n', result

