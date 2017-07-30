# coding=utf8

# system
import os
import time

# local
from tests_ import Check
import base_utils


'''
    最简单的测试用例
    
    本地, 移动到 本地.
    一个文件
'''


class OneFileToLocal(Check):
    def __init__(self, src, pathfrom, pathto):

        # filename to move
        self.src = src

        # 源文件的父目录的绝对路径
        self.pathfrom = pathfrom

        # 目标文件的服务路的绝对路径
        self.pathto = pathto

        # 根据文件传送状态, 逐级增加
        self.statuslist = [u'未传送',u'正在传送', u'完成传送']
        self.status = 1

        # 表示程序执行的过程, 相关的数据
        self._result = '传送的文件信息: ' + self.src + '\n源地址: ' + self.pathfrom + '\n目的地址: ' + self.pathto + '\n'

        # time consuming
        self.consuming_time = 0

    # 执行序列
    # 先改变状态, 再执行具体功能
    def main(self):
        # send src from pathfrom to pathto
        self.status = 0
        if self.check_authority():
            # begin send data
            self.status += 1
            self.senddata()
            # end send data,

            # finish sending data
            self.status += 1

            # and show result
            self.showresult()

        # pass
        if self.status >= len(self.statuslist)-1:
            return True
        else:
            return False


    # check auth has reading authrity of pathfrom
    # and writing authrity of pathto
    def check_authority(self):
        # print self.src, os.stat(self.src)
        print self.pathfrom, os.stat(self.pathfrom)
        print self.src, os.stat(self.pathfrom+base_utils.OS_path_split()+self.src)
        print self.pathto, os.stat(self.pathto)

        return True


    # by some protocol, send file data.
    # 可以采用系统本地的移动命令, 但不具有平台兼容
    # 因此采用了python所带的方法.

    def senddata(self):
        begin = time.time()
        with open(self.pathfrom+base_utils.OS_path_split() + self.src, 'rb') as in_file:
            with open(self.pathto + base_utils.OS_path_split() + self.src, 'wb') as out_file:
                out_file.write(in_file.read())
        end = time.time()

        self.consuming_time = end - begin





    # 返回传输的结果.
    def showresult(self):
        print self._result
        print '本次数据传输结果: ', self.statuslist[self.status]
        print '耗时: ', self.consuming_time



if __name__ == '__main__':
    t = OneFileToLocal('test.txt', 'from', 'to')
    t.main()