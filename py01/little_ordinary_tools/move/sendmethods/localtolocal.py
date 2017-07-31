# coding=utf8


import os




import base_interface
import base_utils
class localtolocal_(base_interface.IMoveFile):
    def __init__(self):
        pass


    # 解析到需要的数据
    def analysis_params(self, **kwargs):
        print kwargs

        self.src = kwargs.get('src')
        self.pathfrom = kwargs.get('pathfrom')
        self.pathto = kwargs.get('pathto')



    # check authority
    def check_authority(self):
        # return False
        if self.check_readable(self.pathfrom+base_utils.OS_path_split()+self.src) \
            and self.check_writeable(self.pathto, False):

            return True
        return False


    # send data
    def senddata(self):
        try:
            with open(self.pathfrom+base_utils.OS_path_split() + self.src, 'rb') as in_file:
                with open(self.pathto + base_utils.OS_path_split() + self.src, 'wb') as out_file:
                    out_file.write(in_file.read())
        except Exception as e:
            print e, 'in localtolocal, senddata'
    # show result
    def showresult(self):
        print 'This is base class for checking authority and ' \
              'sendding data.\nif you want sendding data from pathfrom' \
              'to pathto, you should implement this class.'



    # check write authority
    def check_writeable(self, path, check_parent=False):
        '''
        Check if a given path is writeable by the current user.
        :param path to check 
        :param check_parentif the path to check does not exist,
            check for the ability to write to the parent directory instead
        :return: True for writeable, False for unwriteable
        '''

        if os.access(path, os.F_OK) and os.access(path, os.W_OK):
            # the path exists and is writeable
            return True

        if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
            return False

        # the path does not exists or is not writeable
        if check_parent is False:
            return False

        # lets get the parent directory of the provided path
        parent_dir = os.path.dirname(path)

        if not os.access(parent_dir, os.F_OK):
            return False

        return os.access(parent_dir, os.W_OK)


    # check read authority
    def check_readable(self, path):
        '''
        Check if a given path is readable by the current user.
        :param path: The path to check
        :return: True for readable, False for unreadable
        '''

        if os.access(path, os.F_OK) and os.access(path, os.R_OK):


            # the path exits and is reable
            return True

        return False