# coding=utf8
from .. import base_interface
class localtolocal(base_interface.IMoveFile):
    def __init__(self):
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