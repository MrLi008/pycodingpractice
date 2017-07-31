# coding=utf8

'''

    支持传输文件的通用方法
    不同的具体传输方式的类都应该继承自该类.
'''

class IMoveFile():
    def __init__(self):
        pass

    def analysis_params(self, **kwargs):
        pass

    # check authority
    def check_authority(self):
        return False


    # send data
    def senddata(self):
        pass

    # show result
    def showresult(self):
        print 'This is base class for checking authority and ' \
              'sendding data.\nif you want sendding data from pathfrom' \
              'to pathto, you should implement this class.'