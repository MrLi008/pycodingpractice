# coding=utf8


import sys
value = 2

def g():
    frame = sys._getframe()

    print 'current func: %s'%frame.f_code.co_name

    print 'caller: ', frame.f_back.f_code.co_name

    print 'caller local namespace: ', frame.f_back.f_locals
    print 'coller global namespace: ', frame.f_back.f_globals


def f():
    a=1
    b=2
    g()


def show():
    f()


if __name__ == '__main__':
    show()