# coding=utf8

import igraph
import random

def getsourcedata(minValue, maxValue):
    result = list()
    begin = 0
    end = 20
    for i in range(begin, end, 1):
        for j in range(i, end, 1):
            if random.randint(minValue, maxValue) > 0:
                result.append((i,j))

    return result

res = getsourcedata(-1, 10)
j = igraph.Graph(res)
print j
print '角色数: ', j.vcount()
print '最长的最短路径: ', j.diameter()
print j.get_diameter()
print '度: ', j.maxdegree()

commu = j.community_edge_betweenness(directed=False, weights=None)
print commu


# igraph.plot(j)


def show():
    for i in range(10):
        res = getsourcedata(-1, i)
        g = igraph.Graph(res)
        igraph.plot(g)



if __name__ == '__main__':

    show()
