# coding=utf8


import pandas as pd
import numpy as np
from igraph import Graph, summary



a = pd.Series([1, 3, 5, np.nan, 6, 8])

print a

g = Graph([(0, 1), (0, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 0), (6, 3), (5, 6)])

print g

print summary(g)
print g.degree()