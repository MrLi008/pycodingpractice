# coding=utf8


import numpy as np


def solve_use_recursion(n, m, arr_n, arr_m):
    if n > len(arr_n) or m > len(arr_m):
        return -1
    if n == len(arr_n) or m == len(arr_m):
        return 0

    if arr_n[n] == arr_m[m]:
        val = solve_use_recursion(n+1, m+1, arr_n, arr_m)+1
    else:
        val = -1

    return max([val,
        solve_use_recursion(n, m+1, arr_n, arr_m),
            solve_use_recursion(n+1, m, arr_n, arr_m)
    ])


def solve(n, m, arr_n, arr_m, result):
    if n > len(arr_n) or m > len(arr_m):
        return -1
    if n == len(arr_n) or m == len(arr_m):
        return 0

    if arr_n[n] == arr_m[m]:
        val = solve(n+1, m+1, arr_n, arr_m, result)+1
    else:
        val = -1
    if result[n][m] > 0:
        return result[n, m]

    result[n, m] = max([val,
        solve(n, m+1, arr_n, arr_m, result),
            solve(n+1, m, arr_n, arr_m, result)
    ])

    return result[n, m]

def solve_not_recursion(arr_n, arr_m, result):
    result[0, 0] = 0
    for n in range(0, len(arr_n))[::-1]:
        for m in range(0, len(arr_m))[::-1]:
            if arr_n[n] == arr_m[m]:
                val = result[n+1, m+1] + 1
            else:
                val = -1

            result[n, m] = max([val, result[n, m+1], result[n+1, m]])

    return result[n, m]



if __name__ == '__main__':
    m = np.random.randint(10, size=100)
    n = np.random.randint(10, size=100)

    # m = [1, 0, 1, 0, 2, 2, 2, 1, 2, 2]
    # n = [0, 0, 1, 2, 0, 1, 0, 2, 1, 2]
    print m
    print n

    # result = np.zeros((len(n), len(m)))
    # print solve_use_recursion(0, 0, n, m)

    result = np.zeros((len(n), len(m)))
    print solve(0, 0, n, m, result)
    # print result

    result = np.zeros((len(n)+1, len(m)+1))
    print solve_not_recursion(n, m, result)
    # print result