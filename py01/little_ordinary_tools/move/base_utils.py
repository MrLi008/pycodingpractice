# coding=utf8

import os
import platform
import paramiko


def OS_path_split():
    if platform.system() == 'Windows':
        return '\\'
    else :
        return '/'



# 登录到远程服务器, 并执行代码, 并返回结果
def request_by_ssh_from(**kwargs):
    print kwargs
    hostname = kwargs.get('hostname')
    port = int(kwargs.get('port'))
    username = kwargs.get('username')
    password = kwargs.get('password')

    exe_cmd = kwargs.get('exe_cmd')


    remote_client = paramiko.SSHClient()
    remote_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_client.connect(hostname=hostname,
              port=port,
              username=username,
              password=password)
    stdin, stdout, stderr = remote_client.exec_command(exe_cmd)
    stdin.write(exe_cmd)
    result = stdout.read()
    print 'out: ', len(result)
    print 'err: ', stderr.read()


    remote_client.close()

    return result


if __name__ == '__main__':
    request_by_ssh_from(hostname='210.31.104.123', port='20021', username='root',
                        password='Horose@1970',
                        exe_cmd='cat /etc/nginx/nginx.conf')


