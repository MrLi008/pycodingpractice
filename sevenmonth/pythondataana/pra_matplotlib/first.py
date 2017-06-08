# coding=utf8




# $$  $$
# $ $$ $
#  $  $
#   $$

print __file__



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


start = -2
stop = 2

x = np.arange(start=start, stop=stop, step=0.01)

y = np.arange(start=start, stop=stop, step=0.01)

x, y = np.meshgrid(x, y)

z1 = np.sin((x ** 2 +y ** 2 - 1) ** 2)

z2 = (x**2)*(y**2)

#
# print x
# print y
# print z1
#
# print z2


ax = plt.subplot(111, projection='3d')
# ax.plot_surface(X=x, Y=y, Z=z1)
# ax.plot_surface(X=x, Y=y, Z=z2)

z = ((z1-z2)**2) #<0.001
ax.plot_surface(x, y, z, cmap='rainbow')



print z


#
#
# a,b = (list(), list)
# for i in range(len(x)):
#     for j in range(len(y)):
#         if z[i, j] is True:
#             a.append(x[i])
#             b.append(y[j])






ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')



plt.show()