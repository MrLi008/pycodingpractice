# coding=utf8
import csv
from igraph import Graph as IGraph, plot

edges = list()


firstline = True
with open('stormofswords.csv', 'rb') as f:
    for row in csv.reader(f.read().splitlines()):
        if firstline is True:
            firstline = False
            continue
        ufrom, uto, v = row

        # print ufrom, uto,v
        edges.append((ufrom, uto, int(v)))


g = IGraph.TupleList(edges, directed=False,
                     vertex_name_attr='name',
                     edge_attrs=None,
                     weights=True)


print g
names = g.vs['name']
g.vs['label'] = g.vs['name']
print names

print '角色数: ', g.vcount()
print '最长的最短路径: ', g.diameter()
print g.get_diameter()
print [names[x] for x in g.get_diameter()]
print '度: ', g.maxdegree()
for p in g.vs:
    print p['name'], p.degree(),
    print [x['name'] for x in p.neighbors()]


# pagerank
pg = g.pagerank()
pgvs = list()
for p in zip(g.vs, pg):
    print p
    pgvs.append({'name':p[0]['name'],'pg':p[1]})


print pgvs


colors = {0:'blue', 1:'black', 2:'yellow',3:'pink',4:'gray',5:'red',6:'green', 7:'orange'}
colors_all = [list() for i in range(g.vcount())]
# Community Detection
clusters = IGraph.community_walktrap(g, weights='weight').as_clustering()
nodes = [{'name':name} for name in g.vs['name']]
community = dict()

for node in nodes:
    idx = g.vs.find(name=node['name']).index
    node['community'] = clusters.membership[idx]
    if node['community'] not in community:
        community[node['community']] = [(node['name'], idx)]
    else:
        community[node['community']].append((node['name'], idx))

for c, l in community.iteritems():
    print c, ':', l
    for name, idx in l:
        colors_all[idx] = colors[c]


g.vs['color'] = colors_all

plot(g, 'thronesresult.pdf')

