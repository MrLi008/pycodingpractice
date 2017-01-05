# coding=utf8
'''

# 使用注意事项:
1, 尽量被计时函数无参, 或者能够解析(*arg, **kw)参数
2, 计时精度在秒级, 之后可能会提升精度


'''
import time


def des_time(func):
    # print 'here....des_time', func.__name__

    def _des_time(*arg, **kw):
        # print 'here...._des_time', arg
        # print 'here....__des_time'
        begin = time.time()
        res = func(arg, kw)
        end = time.time()
        print u'函数: ', func.__name__  , u' 用时: ' , ( end - begin ) , ' s '

        return res

    return _des_time


if __name__ == '__main__':
    @des_time
    def test(*arg, **kw):
        print kw
        (begin, end) = arg[0]
        print begin, '-->', end
        while begin < end:
            print begin,'----->....>', end
            begin += 1
    test(1, 5)
