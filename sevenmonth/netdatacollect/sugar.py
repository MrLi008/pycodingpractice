# # coding=utf8
#
#
# def out(x):
#     print 'out:', x
#     def _out(y):
#         print '_out:', x,y
#         return x+y
#     return _out
#
#
# def out1(x):
#     def _out(y):
#         def __out(z):
#             def ___out(a):
#                 return x+y+z+a
#             return ___out
#         return __out
#     return _out
#
#
# o = out1
# for i in range(4):
#     o = o(i)
#     print o
#

# o = out(1)
#
# print o
# _o = o(2)
# print _o
#
# d = dict()
# d[1] = {
#     u'发的说法':{
#         u'发的说法'
#         :{
#             u'发的说法'
#             :{
#                 u'发的说法'
#                 :[5,],
#             }
#         }
#     }
# }
# print d


# a_dict = dict()
# a_dict[1] = 2
# a_dict[3] = 4
# a_dict[5] = 6
#
#
# for a in a_dict.items():
#     print a
#
l3 = [1,0,0]
l2 = [0,1]

res = [(a,b,c,d,e,f,g) for a in l3 for b in l2 for c in l2 for d in l3 for e in l3 for f in  l2 for g in l2]
for r in res:
    print r