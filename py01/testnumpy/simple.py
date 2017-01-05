# coding=utf8

import numpy as np
import random as seed
import descrip_time
import matplotlib.pyplot as plt
from pylab import mpl
import threading

mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['axes.unicode_minus'] = False

# print np

#
# l = list()
#
# for i in range(10):
#     l.append(seed.randint(0, 10)-5)
# l = np.array(l)
# print l

# print  np.where(l > 0, 2, -2)


# arr = np.random.randn(5, 4)
# print 'np.random.randn: \n', arr
# print arr.mean()
# print np.mean(arr)
# print arr.sum()

# arr = np.random.randn(7,7)

@descrip_time.dt.des_time
def show_arr(*arr, **kw):


    print arr[0]

# show_arr(arr)



@descrip_time.dt.des_time
def list_sort__(*arg, **kw):
    arr = sorted(arg[0][0])
    # print arr
    np.save('list_sort__', arr)
    # print arr
    return arr


@descrip_time.dt.des_time
def np_array_sort(*arg, **kw):
    arg[0][0].sort()
    np.save('np_array_sort', arg[0][0])

    print arg[0][0]
    return arg[0][0]

num_figure = 0


def show_result(arr_x, arr_y, str_x='arr_x', str_y='arr_y', figure_or_subplot=(0, 0, 0, 1), title='test'):
    global num_figure
    # print num_figure
    if figure_or_subplot[0] == 0:
        num_figure += 1
        plt.figure(num_figure)
    else:
        plt.subplot(figure_or_subplot[1], figure_or_subplot[2], figure_or_subplot[3])
    plt.scatter(arr_x, arr_y)

    plt.xlabel(str_x)
    # plt.xlim(min(arr_x) * 0.90, max(arr_x) * 1.10)
    plt.ylabel(str_y)
    # plt.ylim(min(arr_y) * 0.90, max(arr_y) * 1.10)
    plt.title(title)
    plt.grid(True)

if __name__ == '__main__':
    arr = list()
    length_data = 1000
    for i in range(length_data):
        arr.append(seed.uniform(0, 10))
    arr_y = list_sort__(arr)
    arr_x = range(length_data)
    print 'arr_x', arr_x
    print 'arr_y', arr_y
    show_result(arr_x, arr_y, figure_or_subplot=1)

    arr2 = np.random.randn(length_data*length_data)
    arr_y = np_array_sort(arr2)
    arr_x = range(length_data*length_data)
    show_result(arr_x, arr_y, figure_or_subplot=1)


    plt.show()

