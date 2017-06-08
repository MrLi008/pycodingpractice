# coding=utf8

print __file__
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


# data
w = np.arange(-1,1,0.01)
h = np.arange(-1,1,0.01)
w,h = np.meshgrid(w,h)

re1 = (w+h)/2
re2 = np.abs(w-h)

res = re2/re1
# res = np.zeros((w.shape[0],h.shape[0]))
# for i in range(w.shape[0]):
#     for j in range(h.shape[0]):
#         if 0 in (w[i], h[j]):
#             continue
#         res[i,j] = np.abs(w[i]-h[j])/(w[i]+h[j])/2




ax = plt.subplot(111, projection='3d')
ax.plot_surface(w,h,res, cmap='rainbow')



ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()