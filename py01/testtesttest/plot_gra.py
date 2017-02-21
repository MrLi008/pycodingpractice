# coding=utf8



from matplotlib import pyplot as plt
import numpy as np



from testnumpy.simple import show_result



x = [float(i)/100 for i in range(-50,50)]
y = [pow(np.e, v)+4*v-3 for v in x]

show_result(x, y, 'x', 'y', title='line')

plt.show()