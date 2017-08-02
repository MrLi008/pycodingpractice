# coding=utf8

# system
import os
import time
import random

# local
from tests_ import Check
import base_utils


'''
    最简单的测试用例
    test1
    本地, 移动到 本地.
    一个文件
    
    test2
    远程服务器, 移动到 远程服务器(ssh)
    
    test3
    复杂地址的数据传输
'''

'''
    
'''

class OneFileToLocal(Check):
    '''
        src:            源文件
        
        pathfrom:       源地址
        pathto:         目标地址
    '''
    def __init__(self, src, pathfrom='', pathto='', aim='', sendmethod=None):

        # filename to move
        self.src = src

        # 源文件的父目录的绝对路径
        self.pathfrom = pathfrom

        # 目标文件的服务路的绝对路径
        if pathto=='':
            self.pathto =  pathfrom
        else:
            self.pathto = pathto
        if aim=='':
            self.aim = src+'_'+str(random.randint(0,1))
        else:
            self.aim = aim

        # 根据文件传送状态, 逐级增加
        self.statuslist = (u'未传送',u'正在传送', u'完成传送')
        self.status = 1

        # 表示程序执行的过程, 相关的数据
        self._result = '传送的文件信息: ' + self.src + '\n源地址: ' + self.pathfrom + '\n目的地址: ' + self.pathto + '\n'

        # time consuming
        self.consuming_time = 0

        # support send data
        self.support_send_methods = {'by_open_file':'localtolocal', 'by_ssh':'remotetoremote'}
        self.sendmethod = sendmethod

        self.ins = None


    # 执行序列
    # 先改变状态, 再执行具体功能
    def main(self):
        # send src from pathfrom to pathto
        self.status = 0
        self.sendmethod = self.confirmsendmethod()
        self.ins = self.createinstancebyclassname()
        self.ins.analysis_params(src=self.src,
                                 pathfrom=self.pathfrom,
                                 pathto=self.pathto,
                                 aim=self.aim)
        if self.check_authority():
            # begin send data
            self.status += 1
            self.senddata()
            # end send data,

            # finish sending data
            self.status += 1

            # and show result
            self.showresult()
        else:
            print '不具备权限'
        # pass
        if self.status >= len(self.statuslist)-1:
            return True
        else:
            return False


    # check auth has reading authrity of pathfrom
    # and writing authrity of pathto
    def check_authority(self):
        # return True
        # print self.src, os.stat(self.src)
        print self.pathfrom, os.stat(self.pathfrom)
        print self.src, os.stat(self.pathfrom+base_utils.OS_path_split()+self.src)
        print self.pathto, os.stat(self.pathto)

        return self.ins.check_authority()


    # by some protocol, send file data.
    # 可以采用系统本地的移动命令, 但不具有平台兼容
    # 因此采用了python所带的方法.

    def senddata(self):
        begin = time.time()
        self.ins.senddata()
        end = time.time()

        self.consuming_time = end - begin


    # 返回传输的结果.
    def showresult(self):
        print self._result
        self.ins.showresult()
        print '本次数据传输结果: ', self.statuslist[self.status]
        print '耗时: ', self.consuming_time


    # confirm send method
    def confirmsendmethod(self):
        if self.sendmethod in (None, ''):
            # 自动判断传输方式
            # TODO:
            pass
        else:
            return self.sendmethod

    # 根据类名常见实例, 由于不同类, 需要的参数不一样
    # 所以在此不传递参数.
    # 所以子类可以有单独的参数解析函数.
    def createinstancebyclassname(self):
        classname = self.support_send_methods.get(self.sendmethod)
        targetmode=__import__('sendmethods.'+classname, fromlist=[classname, ])
        Class_ = getattr(targetmode, classname)
        print Class_
        print targetmode
        return Class_()




# Little test for the class function is OK.
if __name__ == '__main__':

    # # for localtolocal
    #
    # src = 'test.txt'
    # src_path = 'from'
    # aim_path = 'to'
    #
    # if not os.path.exists(src_path):
    #     os.mkdir(src_path)
    # if not os.path.exists(src_path+base_utils.OS_path_split()+src):
    #     with open(src_path+base_utils.OS_path_split()+src, 'wb') as f:
    #         f.write('1234\t'*10000)
    #
    #
    # if not os.path.exists(aim_path):
    #     os.mkdir(aim_path)
    #
    # t = OneFileToLocal(src, src_path, aim_path, sendmethod='by_open_file')
    # t.main()
    #

    # for remote to remote by ssh

    src = 'nginx.conf'
    src_path = '/etc/nginx'
    aim_path = ''

    # if not os.path.exists(src_path):
    #     os.mkdir(src_path)
    # if not os.path.exists(src_path+base_utils.OS_path_split()+src):
    #     with open(src_path+base_utils.OS_path_split()+src, 'wb') as f:
    #         f.write('1234\t'*10000)


    # if not os.path.exists(aim_path):
    #     os.mkdir(aim_path)

    t = OneFileToLocal(src, src_path, aim_path, sendmethod='by_ssh')
    t.main()



