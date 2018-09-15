# -*- coding: utf-8-*-
# python调用windows的exe可执行程序
# 传参调用exe程序（解决相对路径，觉得路径问题），等待exe进程结束，此程序才结束。
import os, sys,time
import win32process, win32event
import psutil
'''# 需要用的模块：pywin32-214.win32-py2.5.exe
        # CreateProcess(appName, commandLine , processAttributes , threadAttributes , bInheritHandles , dwCreationFlags , newEnvironment , currentDirectory , startupinfo )
        # 其参数含义如下。
        #  appName    可执行文件名。
        #  commandLine   命令行参数。
        #  processAttributes  进程安全属性，如果为None则为默认的安全属性。
        #  threadAttributes  线程安全属性，如果为None则为默认的安全属性。
        #  bInheritHandles   继承标志。
        #  dwCreationFlags  创建标志。
        #  newEnvironment  创建进程的环境变量。
        #  currentDirectory  进程的当前目录。
        #  startupinfo    创建进程的属性。'''
class Run_exe:
    def __init__(self, path):
        self.path = path
        # os.chdir(exe_path)
        self.running=None
        self.handle=None
    def start(self):
        try:
            self.handle = win32process.CreateProcess(self.path, '', None, None, 0,
                                                win32process.CREATE_NO_WINDOW,
                                                None, None, win32process.STARTUPINFO())
            self.running = True
        except Exception as e:
            print("Create Error!", e)
            self.handle = None
            self.running = False
        while self.running:
            # rc = win32event.WaitForSingleObject(self.handle[0], 1000)
            # rc = win32event.WaitForSingleObject(self.handle[0], -1)#一直等待
            rc=win32process.TerminateProcess(self.handle[0], 0)
            if rc == win32event.WAIT_OBJECT_0:
                self.running = False
                print("已打开应用程序...")

if __name__ == '__main__':
    path = r"C:\Windows\System32\calc.exe"
    s=Run_exe(path)
    s.start()



