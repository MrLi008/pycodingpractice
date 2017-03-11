# coding=utf8


# 点运算
# s = c*pow(r,y)


import numpy as np
import matplotlib.pyplot as plt

start = 0
stop = 1
step = 0.001
c = 1


x = np.arange(start=start, stop=stop, step=step)

i=0.04
while i < 26:
    y = c*x**i

    plt.plot(x,y)
    plt.text(i, np.mean(y, axis=0)*0.7, 'i='+str(i))

    i+=i/2
    # print x
    # print y
    print i


plt.xlabel('x')
plt.ylabel('y')




plt.show()