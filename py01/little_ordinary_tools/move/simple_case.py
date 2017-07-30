# coding=utf8


from tests_ import Check



'''
    最简单的测试用例
    
    本地, 移动到 本地.
    一个文件
'''


class OneFileToLocal(Check):
    def __init__(self):
        self.src = ''
        self.pathfrom = ''
        self.pathto = ''


        self.status = ''


    def main(self):
        # send src from pathfrom to pathto
        pass


    # check auth has reading authrity of pathfrom
    # and writing authrity of pathto
    def check_authority(self):
        pass


    # by some protocol, send file data.
    def senddata(self):
        pass



    # 返回传输的结果.
    def result(self):
        pass