# coding=utf8


'''
随机漫步

随机产生数字
当该数字值为某一个数或某个范围时, 停止产生随机数, 并记录当前所用时间
以0-10000为x轴
以所用时间为y轴
绘制图形
'''

import random as seed
import matplotlib.pyplot as plt
from simple import show_result
import numpy as np
import descrip_time
# import time
num_target = 5
# 统计循环的次数
counter = 0


# @descrip_time.dt.des_time
def test_length_data_not_np(*arg, **kw):
    times_data = (100, 200, 500, 1000, 2500, 5000, 7000, 8000, 10000)
    global counter
    counter = 0

    for l in times_data:
        # print l
        ary_y1 = list()
        arr_y = dict()
        for x in range(l):
            counts = 0
            value = -1
            while value != num_target:
                value = seed.randint(0, 100)
                counts += 1
            ary_y1.append(counts)
            if counts not in arr_y.keys():
                arr_y[counts] = 0
            arr_y[counts] += 1

        print 'prepare to show.......'
        ary_x1 = range(len(ary_y1))
        ary_y1 = ary_y1

        arr_x = arr_y.keys()
        arr_y = arr_y.values()
        # plot
        plt.figure(counter)
        show_result(arr_x, arr_y, u'x-', u'y-次数', title='size: '+str(l), figure_or_subplot=(1, 2, 2, 2))
        show_result(ary_x1, ary_y1, 'x index', 'y time', title='size:'+str(l), figure_or_subplot=(1, 2, 2, 1))
        # 再增加一个保存图片的功能
        # 方便之后测试结果的比较

        counter += 1


def get_target_counter(target, begin, end):
    value = -1
    counts = 0
    while value is not target:
        value = seed.randint(begin, end)
        counts += 1
    return counts

'''
:param target: 一维数组
: [being,end) 取值范围
'''


def get_target_counter_by_np_array(target, begin, end, l):
    index = 0
    arr_y = np.zeros(l)

    arr_y_dict = dict()
    while index < l:
        arr_y[index] = get_target_counter(target, begin, end)
        if arr_y[index] not in arr_y_dict.keys():
            arr_y_dict[arr_y[index]] = 0
        arr_y_dict[arr_y[index]] += 1

        index += 1

    # print arr_y

    return arr_y, arr_y_dict


# @descrip_time.dt.des_time
def test_length_data_use_np(*arg, **kw):
    target = 10
    begin = 0
    end = 100
    # 单次实验测试次数
    times_data = (100, )  # 200, 500, 1000, 2500, 5000, 7000, 8000, 10000)
    global counter
    counter = 0
    for l in times_data:
        arr_x = np.arange(l)

        arr_y, arr_y_dict = get_target_counter_by_np_array(target, begin, end, l)

        # print arr_x, arr_y, l

        print 'prepare ......'
        plt.figure(counter)
        show_result(arr_x, arr_y, u'实验编号', u'得到target的次数', title=u'次数: '+str(l), figure_or_subplot=(1, 2, 2, 3))

        arr_x_dict = arr_y_dict.keys()
        arr_y_dict = arr_y_dict.values()
        show_result(arr_x_dict, arr_y_dict, u'次数', u'出现该次数的次数', title=u'次数的次数'+str(l), figure_or_subplot=(1, 2, 2, 4))

        counter += 1
        return arr_y[arr_y_dict]

if __name__ == '__main__':
    # test_length_data_not_np(1, 2)
    # plt.show()
    print get_target_counter(10, 0, 100)
    arr = test_length_data_use_np(1, 2)
    plt.show()
    print arr
