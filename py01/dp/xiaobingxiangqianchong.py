# coding=utf8
'''
u'小兵从左下角走到右上角
求有多少种走法
只能向上和右方向走'
'''
import numpy as np

result = np.zeros((5, 10))


def solve(n, m):
    if n < 0:
        return 0
    if m < 0:
        return 0
    # print '(', m, ',', n, ')',
    if m == n and n == 0:
        # print
        result[m][n] = 1
        return result[m][n]
    result[m][n] = solve(n-1, m) + solve(n, m-1)

    return result[m][n]


def solve_not_recursion(n, m):
    result[0][0] = 1
    result[1][0] = 1
    result[0][1] = 1
    for m1 in range(0, m):
        for n1 in range(0, n):
            if m1 == 0 or n1 == 0:
                result[m1][n1] = 1
            else:
                result[m1][n1] = result[m1-1][n1] + result[m1][n1-1]


if __name__ == '__main__':
    print solve(5, 2)
    print result
    result = np.zeros((10, 10))
    solve_not_recursion(10, 10)
    print result.astype(dtype=np.int)

