# coding=utf8

'''

question:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were
broken into on the same night.

Given a list of non-negative integers representing the amount
of money of each house, determine the maximum amount of money
you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and
creating all test cases. Also thanks to @ts for adding additional test cases.

Subscribe to see which companies asked this question
'''


u'''
大体意思:
作为一个专业的小偷
只能隔一家抢
不能抢相邻的两家
为获取最多的钱,
给出一个抢钱的策略
'''

import numpy as np
import random as seed

numbers = list()
for i in range(1000):
    numbers.append(seed.randint(0, 100))
print numbers
# numbers = [49, 39, 57, 64, 23, 61, 5, 75, 58, 91, 34, 12, 14, 79, 19, 50, 68, 74, 50, 1, 10, 46, 92, 45, 11, 63, 52, 94, 86, 29, 36, 99, 33, 62, 17, 90, 43, 43, 39, 49, 35, 43, 65, 80, 83, 27, 5, 2, 80, 77, 3, 44, 70, 52, 80, 15, 76, 97, 71, 90, 77, 32, 50, 42, 62, 32, 28, 12, 93, 70, 83, 11, 84, 3, 19, 23, 38, 65, 63, 100, 3, 38, 6, 72, 59, 8, 63, 14, 64, 35, 0, 63, 26, 14, 0, 35, 3, 39, 47, 41, 61, 6, 48, 37, 37, 41, 74, 14, 89, 88, 22, 64, 46, 12, 8, 84, 88, 12, 60, 30, 29, 0, 40, 49, 9, 2, 90, 70, 91, 66, 75, 84, 12, 99, 85, 20, 46, 42, 92, 11, 28, 96, 82, 86, 52, 94, 50, 48, 92, 26, 88, 60, 50, 55, 22, 57, 63, 9, 63, 11, 19, 2, 100, 81, 33, 29, 46, 91, 70, 10, 12, 17, 50, 6, 54, 62, 53, 3, 84, 62, 67, 69, 47, 85, 25, 79, 76, 87, 54, 41, 33, 26, 75, 54, 93, 69, 98, 28, 74, 6, 62, 51, 12, 68, 94, 16, 5, 7, 24, 97, 6, 17, 7, 91, 42, 64, 33, 53, 87, 15, 6, 39, 77, 79, 20, 67, 56, 6, 95, 18, 80, 90, 90, 79, 8, 23, 46, 26, 87, 33, 20, 27, 42, 55, 26, 0, 49, 84, 6, 64, 22, 8, 41, 69, 89, 28, 24, 41, 68, 71, 40, 34, 18, 38, 15, 72, 9, 4, 9, 91, 19, 74, 33, 66, 10, 29, 28, 79, 12, 93, 54, 9, 63, 56, 23, 24, 97, 57, 52, 77, 17, 62, 56, 84, 8, 75, 91, 46, 57, 96, 8, 57, 39, 27, 57, 58, 38, 47, 69, 82, 85, 10, 63, 93, 39, 8, 17, 38, 2, 76, 26, 2, 34, 19, 8, 38, 5, 53, 80, 86, 27, 3, 90, 80, 20, 12, 40, 56, 51, 11, 1, 17, 51, 5, 27, 50, 32, 59, 78, 17, 44, 94, 94, 93, 2, 13, 64, 2, 13, 28, 68, 36, 69, 12, 11, 92, 60, 68, 42, 85, 28, 63, 60, 92, 48, 98, 47, 26, 1, 30, 25, 4, 73, 85, 34, 85, 13, 79, 99, 90, 87, 66, 48, 27, 63, 83, 6, 85, 77, 43, 22, 21, 47, 36, 26, 29, 97, 98, 18, 82, 28, 92, 58, 36, 31, 43, 74, 0, 75, 53, 96, 14, 92, 82, 12, 78, 82, 59, 16, 5, 25, 25, 9, 98, 75, 13, 40, 97, 23, 66, 26, 10, 8, 50, 50, 9, 90, 22, 33, 50, 91, 79, 55, 3, 8, 76, 17, 54, 78, 87, 57, 61, 29, 8, 100, 60, 14, 34, 36, 16, 47, 49, 8, 3, 0, 33, 35, 38, 43, 14, 71, 77, 52, 26, 74, 35, 85, 0, 57, 18, 27, 90, 15, 22, 41, 8, 29, 93, 61, 91, 81, 49, 31, 50, 75, 85, 59, 7, 14, 29, 67, 61, 79, 50, 41, 73, 21, 85, 81, 52, 35, 22, 19, 9, 66, 4, 88, 10, 3, 22, 76, 81, 16, 65, 67, 93, 10, 21, 4, 100, 35, 0, 19, 52, 29, 78, 77, 58, 83, 44, 69, 15, 81, 61, 71, 52, 53, 71, 97, 12, 64, 57, 34, 50, 38, 5, 68, 75, 38, 16, 13, 71, 95, 20, 44, 92, 58, 70, 89, 49, 29, 98, 24, 9, 16, 42, 0, 46, 83, 90, 15, 50, 86, 96, 99, 68, 87, 89, 47, 64, 38, 77, 60, 65, 53, 95, 97, 10, 39, 64, 71, 68, 69, 59, 66, 10, 81, 52, 35, 71, 71, 13, 93, 31, 67, 66, 59, 93, 86, 93, 49, 83, 49, 54, 57, 40, 66, 13, 21, 29, 93, 74, 82, 51, 53, 65, 22, 92, 58, 92, 54, 14, 46, 41, 85, 92, 91, 26, 4, 47, 73, 89, 36, 68, 65, 57, 85, 91, 68, 11, 15, 47, 87, 43, 30, 83, 87, 17, 74, 11, 53, 45, 95, 55, 21, 84, 28, 36, 36, 86, 95, 32, 18, 45, 99, 58, 67, 44, 22, 94, 86, 95, 32, 99, 95, 35, 71, 87, 73, 24, 19, 95, 55, 30, 72, 51, 13, 74, 65, 20, 75, 47, 17, 31, 41, 12, 77, 40, 7, 95, 48, 54, 49, 10, 55, 70, 72, 98, 46, 36, 10, 40, 86, 29, 30, 79, 81, 30, 51, 40, 61, 53, 64, 84, 50, 5, 3, 13, 76, 12, 14, 72, 82, 3, 0, 22, 90, 66, 86, 78, 27, 72, 7, 27, 23, 54, 99, 28, 50, 73, 36, 76, 91, 17, 76, 71, 65, 45, 83, 7, 29, 13, 85, 89, 2, 95, 10, 35, 3, 33, 23, 57, 87, 46, 46, 41, 40, 44, 32, 17, 98, 50, 3, 93, 50, 27, 58, 58, 24, 93, 70, 40, 42, 35, 57, 86, 12, 63, 87, 2, 78, 49, 97, 83, 68, 80, 43, 4, 76, 48, 91, 53, 89, 41, 21, 6, 99, 34, 99, 5, 97, 5, 9, 32, 35, 66, 44, 31, 71, 14, 10, 96, 89, 0, 33, 10, 17, 100, 5, 25, 20, 95, 3, 19, 93, 26, 20, 67, 59, 78, 15, 90, 56, 87, 82, 50, 23, 17, 40, 77, 96, 73, 84, 7, 98, 99, 17, 36, 21, 88, 45, 8, 41, 88, 67, 87, 80, 21, 51, 58, 99, 69, 7, 54, 43, 44, 41, 96, 41, 49, 14, 23, 74, 66, 8, 42, 50, 71, 74, 31, 39, 47, 2, 60, 73, 73, 64, 13, 66, 20, 2, 63, 57, 50, 93, 84, 73, 18, 33, 30, 75, 67, 31, 62, 61, 13, 28, 42, 16, 14, 40, 80, 6, 59, 6, 43, 52, 46, 37, 49, 52, 69, 43, 99, 30, 24, 78, 53, 28, 69, 99, 3, 18, 84, 18, 80, 87, 95, 68, 65, 13, 42, 96, 94, 52, 37, 44, 40, 96, 30]
solved = np.zeros(len(numbers))


def solve(index, numbers):

    if index < 0:
        return 0
    if solved[index] > 0:
        return solved[index]
    # choice_0_2 = solve(index - 2, numbers) + numbers[index]
    # choice_1 = solve(index - 1, numbers)
    # # print solved
    # if  choice_0_2 > choice_1:
    #     solved[index] = choice_0_2
    #     return choice_0_2
    # else:
    #     solved[index] = choice_1
    #     return choice_1
    solved[index] = max(numbers[index] + solve(index - 2, numbers), solve(index - 1, numbers))
    return solved[index]


def solve_not_recursion(numbers):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return max(numbers[0], numbers[1])

    result = np.zeros(len(numbers))
    result[0] = numbers[0]
    result[1] = max(result[0], numbers[1])
    i = 2
    while i < len(numbers):
        result[i] = max(result[i-2] + numbers[i], result[i-1])
        i += 1
    return result[len(numbers) - 1]


if __name__ == '__main__':

    print solve(len(numbers)-1, numbers)
    print solve_not_recursion(numbers)
    # print solved

#
u'''
局部最优解
'''
# import random as seed
#
#
# def show_money_dict(money_dict):
#     print 'money: indexes'
#     for k in money_dict.keys():
#         print k, ' : ', money_dict.get(k)
#
#
# def add_money_dict(money_dict):
#     value = 0
#     for k in money_dict.keys():
#         for k2 in money_dict.get(k).keys():
#             if money_dict.get(k).get(k2) is not 0:
#                 value += k
#     return value
#
# if __name__ == '__main__':
#     # street_money = list()
#     # for i in range(street_length):
#     #     street_money.append(seed.randint(0, 100))
#     street_money = [64, 78, 78]
#     street_length = len(street_money)
#     print 'street money: ', street_money
#
#     print 'sorted: ', sorted(street_money)
#
#     money_dict = dict()
#     i = 0
#     while i < street_length:
#         if street_money[i] not in money_dict.keys():
#             money_dict[street_money[i]] = dict()
#         money_dict[street_money[i]][i] = 0
#         i += 1
#
#     show_money_dict(money_dict)
#
#     for it in money_dict.keys()[::-1]:
#         # it = max(money_dict.keys())
#         print it
#         value_dict = money_dict[it]
#         for k in value_dict.keys():
#             if k == 0 and k+1 <= len(street_money):
#                 if money_dict[street_money[k+1]][k+1] == 0:
#                     value_dict[k] = 1
#             elif k+1 >= len(street_money) and k > 0:
#                 if money_dict[street_money[k-1]][k-1] == 0:
#                     value_dict[k] = 1
#             elif value_dict[k] == 0 \
#                     and money_dict[street_money[k-1]][k-1] == 0 \
#                     and money_dict[street_money[k+1]][k+1] == 0:
#                 value_dict[k] = 1
#     show_money_dict(money_dict)
#     print add_money_dict(money_dict)
