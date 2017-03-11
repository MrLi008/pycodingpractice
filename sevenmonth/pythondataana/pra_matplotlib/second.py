# coding=utf8



# 据说是个爱心
# ......





# $$  $$
# $ $$ $
#  $  $
#   $$





import matplotlib.pyplot as plt


import numpy as np

start = -2
stop = 2

x = np.arange(start=start, stop=stop, step=0.1)

y = np.arange(start=start, stop=stop, step=0.1)



#
# print x
# print y
# print z1
#
# print z2


ax = plt.subplot(111)
# ax.plot_surface(X=x, Y=y, Z=z1)
# ax.plot_surface(X=x, Y=y, Z=z2)


# print z
# print len(z)
print len(x), len(y)

for i in range(len(x)):
    for j in range(len(y)):
        z1 = (x[i] ** 2 + y[j] ** 2 - 1) ** 2

        z2 = (x[i] ** 2) * (y[j] ** 2)

        z = ((z1 - z2) ** 2) < 0.0001
        if z == True:
            ax.scatter(x[i], y[j])


print '...'
#
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()