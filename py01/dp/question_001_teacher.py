# coding=utf8
import numpy as np


def solve(index, nums):
    if index < 0:
        return 0
    m = max(nums[index] + solve(index-2, nums), solve(index - 1, nums))
    # print m
    return m

fib_result = np.zeros(15)


def fib(n):
    print fib_result
    if n <= 1:
        fib_result[n] = 1
        return fib_result[n]
    if fib_result[n] > 0:
        return fib_result[n]
    fib_result[n] = fib(n-1) + fib(n-2)
    return fib_result[n]

if __name__ == '__main__':
    nums = [64, 78, 78, 78]
    print solve(len(nums)-1, nums)
    print fib(5)
