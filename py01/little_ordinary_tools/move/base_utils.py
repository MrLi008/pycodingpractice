# coding=utf8

import os
import platform


def OS_path_split():
    if platform.system() == 'Windows':
        return '\\'
    else :
        return '/'