#coding=utf-8
from ctypes import *
from my_debugger_defines import *

kernel32=windll.kernel32#加载kernel32.dll


class debugger():
    def __init__(self):
        self.h_process=None
        self.pid=None
        self.debugger_active=False
        self.h_thread=None
        self.context=None

    def load(self, path_to_exe):
        print("path_to_exe:%s" % path_to_exe)
        # dwCreation flag determines how to create the process
        # set creation_flags = CREATE_NEW_CONSOLE if you want
        # to see the calculator GUI
        creation_flags = DEBUG_PROCESS

        # instantiate the structs
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        # The following two options allow the started process
        # to be shown as a separate window. This also illustrates
        # how different settings in the STARTUPINFO struct can affect
        # the debuggee.
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        # We then initialize the cb variable in the STARTUPINFO struct
        # which is just the size of the struct itself
        startupinfo.cb = sizeof(startupinfo)
        # s=kernel32.CreateProcessW(path_to_exe,
        #宽字符问题，于是把my_debugger里的CreateProcessA改成CreateProcessW，来来来，给你宽宽宽。
        s=kernel32.CreateProcessW(path_to_exe,
                                None,
                                None,
                                None,
                                None,
                                creation_flags,
                                None,
                                None,
                                byref(startupinfo),
                                byref(process_information))

        if s:
            print ("[*] We have successfully launched the process!")
            print ("[*] PID:%d" % process_information.dwProcessId)
            # 保存一个指向新建进程的有效句柄，以供后续的进程访问使用
            self.h_process=self.open_process(process_information.dwProcessId)

        else:
            print ("[*] Error with error code %d." % kernel32.GetLastError())

    def open_process(self,pid):
        # h_process=kernel32.OpenProcess(PROCESS_ALL_ACCESS,pid,False)#windows
        h_process=kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)#linux
        return h_process
    def attach(self,pid):
        # if not self.enableDebugPrivilege():
        #     return False

        self.h_process=self.open_process(pid)
        #视图附加到目标进城，若附加失败，则输出提示信息后退出
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active=True
            self.pid=pid
            # self.run()#获取CPU寄存器状态时注释掉
        else:
            print("[*] Unable  to attach to the process.")
            print ("[*] Error with error code %d." % kernel32.GetLastError())
    def run(self):
        #现在等待发生在debugee进程中的调试事件
        while self.debugger_active==True:
            self.get_debug_event()

    def get_debug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        # INFINITE表示无限等待
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
            # 获取相关线程的句柄并提取上下文环境信息
            self.h_thread = self.open_thread(debug_event.dwThreadId)
            self.context = self.get_thread_context(self.h_thread)
            print("Event Code:%d  Thread ID:%d" % (debug_event.dwDebugEventCode, debug_event.dwThreadId))
            kernel32.ContinueDebugEvent(debug_event.dwProcessId, debug_event.dwThreadId, continue_status)

        # INFINITE表示无限等待
        # if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
        #     #目前还没构建任何与实践处理相关的功能逻辑
        #     #只是简单的恢复执行目标进程
        #     # input("press a key to continue...")#获取CPU寄存器状态时注释掉
        #     # self.debugger_active=False#获取CPU寄存器状态时注释掉
        #     kernel32.ContinueDebugEvent(debug_event.dwProcessId,debug_event.dwThreadId,continue_status)
    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Finished debugging, Exiting...")
            return True
        else:
            print("Threre was an error")
            print("[*] Error with error code %d." % kernel32.GetLastError())
            return False

    def enableDebugPrivilege(self):
        '''提权限方法'''
        advapi32 = windll.LoadLibrary("Advapi32.dll")
        hToken = HANDLE()
        if advapi32.OpenProcessToken(kernel32.GetCurrentProcess(), 0x20, byref(hToken)):
            tp = TOKEN_PRIVILEGES()
            tp.PrivilegeCount = 1
            if not advapi32.LookupPrivilegeValueA(0, "SeDebugPrivilege", byref(tp.Privileges[0].Luid)):
                print("[*]can't lookup privilege value.")
                print("[*]errorcode:0x%08x." % kernel32.GetLastError())
                return False

            tp.Privileges[0].Attributes = 0X02
            if not advapi32.AdjustTokenPrivileges(hToken, 0, byref(tp), sizeof(tp), 0, 0):
                print("[*]can't adjust privilege value.")
                print("[*]errorcode:0x%08x." % kernel32.GetLastError())
                return False

            kernel32.CloseHandle(hToken)
            return True
        else:
            print("[*]can't open process token.")
            print("[*]error code:0x%08x." % kernel32.GetLastError())
            return False

    def open_thread(self, thread_id):
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, thread_id)
        if h_thread is not None:
            return h_thread
        else:
            print("[*] Could not obtain a valid thread handle.")
            return False

    def enumerate_threads(self):
        thread_entry = THREADENTRY32()
        thread_list = []
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)
        if snapshot is not None:
            #正确设置结构体的大小，否则调用会失败
            thread_entry.dwSize = sizeof(thread_entry)
            success = kernel32.Thread32First(snapshot, byref(thread_entry))
            while success:
                if thread_entry.th32OwnerProcessID == self.pid:
                    thread_list.append(thread_entry.th32ThreadID)
                success = kernel32.Thread32Next(snapshot, byref(thread_entry))

            kernel32.CloseHandle(snapshot)
            return thread_list
        else:
            print("enumerate_threads fail.")
            return False

    def get_thread_context(self, thread_id):
        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        #获取线程句柄
        h_thread = self.open_thread(thread_id)
        if kernel32.GetThreadContext(h_thread, byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            print("get_thread_context fail.")
            return False


