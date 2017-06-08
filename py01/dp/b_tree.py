# coding=utf8
from collections import Iterable

def showmetadata(data, tab):
    print ' '*tab*3, data

def showdata(data, tab):
    if not isinstance(data, Iterable):
        showmetadata(data, tab)
    elif isinstance(data, str):
        showmetadata(data, tab)

    elif isinstance(data, list):
        for d in data:
            showdata(d, tab+1)
    elif isinstance(data, tuple):
        for d in data:
            showdata(d, tab+1)
    elif isinstance(data, dict):
        for k, v in data.items():
            showmetadata(k, tab)
            showdata(v, tab+1)
    else:
        showmetadata(data, tab)


class BTree:
    def __init__(self):
        self.data = dict()




    def __str__(self):
        print 'class: BTree'
        print 'data: '
        showdata(self.data)



# test data
data = {
    u'犯罪嫌疑人供述':
        {
            u'有罪供述':{
                u'时间':{
                    'type':'datetime',
                    'name':u'时间',
                    'value': None
                },
                u'地点':{
                    'type':'select',
                    'name':u'地点',
                    'value': None
                }
            },
            u'无罪供述':{

            }
        }
}


if __name__ == '__main__':

    showdata(data, 0)