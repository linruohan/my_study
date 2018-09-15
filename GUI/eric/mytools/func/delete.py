#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '7/29/2015-029'
"""
import fnmatch
from os import walk, path, remove
import sys

if len(sys.argv) >= 3:
    EXT = sys.argv[2]
    DEL_DIR = sys.argv[1]
elif len(sys.argv) >= 2:
    EXT = 'pyc'
    DEL_DIR = sys.argv[1]
else:
    EXT = 'pyc'
    DEL_DIR = r'E:\mine\python_workspace\WebSite'
if not path.exists(DEL_DIR):
    print('error: DEL_DIR not found!!!')
    exit()
print('DEL_DIR: ', DEL_DIR, '\ndelete file extension: ', EXT)

print('deleted files:\n')


def del_pyc(DEL_DIR):
    for filepath, _, filename_list in walk(DEL_DIR):
        for filename in filename_list:
            if fnmatch.fnmatch(filename, '*.' + EXT):  # unix shell风格匹配方式
                # if filename.endswith('.pyc'):
                print(filename)
                remove(path.join(filepath, filename))


if __name__ == '__main__':
    del_pyc(DEL_DIR)