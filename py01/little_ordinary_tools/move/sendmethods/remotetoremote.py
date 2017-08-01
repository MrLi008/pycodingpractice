# coding=utf8
# coding=utf8


import os


'''
整体思路:
使用ssh登录到远程服务器a, 
拷到文件数据
在发送到远程服务器b上
'''

import base_interface
import base_utils
class remotetoremote(base_interface.IMoveFile):
    def __init__(self):
        self.src = ''
        self.pathfrom = ''
        self.pathto = ''
        self.aim = ''
        # by ssh
        self.sshobj=dict()

        # self.OS_path_split = '/'


    # 解析到需要的数据
    def analysis_params(self, **kwargs):
        print kwargs

        self.src = kwargs.get('src')
        self.pathfrom = kwargs.get('pathfrom')
        self.pathto = kwargs.get('pathto')
        self.aim = kwargs.get('aim')

        src_ip = raw_input('src ip: ')
        src_port = raw_input('src ssh port')
        src_username = raw_input('src username: ')
        src_password = raw_input('src password: ')

        remote_ip = raw_input('remote ip: ')
        remote_port = raw_input('remote ssh port: ')
        remote_username = raw_input('remote username: ')
        remote_password = raw_input('remote password: ')

        self.sshobj['src_ip'] = src_ip or '210.31.104.123'
        self.sshobj['src_port'] = src_port or 20021
        self.sshobj['src_username'] = src_username or 'root'
        self.sshobj['src_password'] = src_password or 'Horose@1970'
        self.sshobj['remote_ip'] = remote_ip or '210.31.104.123'
        self.sshobj['remote_port'] = remote_port or 20021
        self.sshobj['remote_username'] = remote_username or 'root'
        self.sshobj['remote_password'] = remote_password or 'Horose@1970'




    # check authority
    def check_authority(self):
        # return False
        if self.check_readable(self.pathfrom+self.OS_path_split()+self.src) \
            and self.check_writeable(self.pathto+self.OS_path_split()+self.aim, True):

            return True
        return False


    # send data
    def senddata(self):
        try:
            # TODO: send data by ssh
            filedata = base_utils.request_by_ssh_from(
                hostname=self.sshobj.get('src_ip'),
                port=self.sshobj.get('src_port'),
                username=self.sshobj.get('src_username'),
                password=self.sshobj.get('src_password'),
                exe_cmd='cat '+ self.pathfrom+self.OS_path_split()+self.src
            )
            base_utils.request_by_ssh_from(
                hostname=self.sshobj.get('src_ip'),
                port=self.sshobj.get('src_port'),
                username=self.sshobj.get('src_username'),
                password=self.sshobj.get('src_password'),
                exe_cmd='echo \''+ filedata + '\' >> ' \
                        + self.pathto+self.OS_path_split()+self.aim
            )


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
            print 'writeable'
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
            print 'readable'


            # the path exits and is reable
            return True

        return False

    def OS_path_split(self):
        return '/'