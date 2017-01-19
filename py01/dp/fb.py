
import numpy as np


def f(index, result):
    if index <= 0:
        return 0L

    if index == 1:
        # print 1,
        result[index] = 1L
        return 1L



    if result[index] >0:
        return result[index]

    result[index] = f(index-1, result)+f(index-2, result)
    # print result[index]
    return result[index]

if __name__ == '__main__':
    n = 50
    result = np.zeros(n+1, dtype=np.uint64)
    f(n, result)

    print result[1:]