# coding=gbk
import os, win32api, io, sys, time, subprocess,win32process
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')

os.startfile(r'C:\Windows\System32\calc.exe')
os.system('notepad')
os.system('notepad 001.txt')
os.system("taskkill /F /IM notepad.exe")
b = os.popen('mkdir nwdir', 'r', 1)
# command -- 使用的命令。
# mode -- 模式权限可以是 'r'(默认) 或 'w'。
# bufsize -- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。
win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)
# ShellExecute(hwnd, op , file , params , dir , bShow )
# 其参数含义如下所示。
# ·     hwnd：父窗口的句柄，如果没有父窗口，则为0。
# ·     op：要进行的操作，为“open”、“print”或者为空。
# ·     file：要运行的程序，或者打开的脚本。
# ·     params：要向程序传递的参数，如果打开的为文件，则为空。
# ·     dir：程序初始化的目录。
# ·     bShow：是否显示窗口。0不显示，1，显示
win32api.ShellExecute(0, 'open', 'notepad.exe', '001.txt', '', 1)
win32api.ShellExecute(0, 'open', 'http://www.python.org', '','',1)#打开网页
win32process.CreateProcess('c:\\windows\\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None,
                           win32process.STARTUPINFO())
# (4)使用模块subprocess
# 说到底还是subprocess最为强大，能实现很多功能：调用shell命令，获取调用信息，监控调用过程，超时终止等，要求调用过程不阻塞，还能交互，
            # 【CreateProcess】接收一个字符串参数，
            # args	                    shell命令，可以是字符串或者序列类型（如：list，元组）
            # bufsize	                指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
            # stdin, stdout, stderr		                分别表示程序的标准输入、输出、
                        # subprocess.PIPE  在创建Popen对象时，subprocess.PIPE可以初始化stdin, stdout或stderr参数。表示与子进程通信的标准流。
                        #subprocess.STDOUT   创建Popen对象时，用于初始化stderr参数，表示将错误通过标准输出流输出。
            # preexec_fn		                只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
            # close_sfs		                在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
            # shell		                同上
            # cwd		                用于设置子进程的当前目录
            # env		                用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
            # universal_newlines		                不同系统的换行符不同，True -> 同意使用 \n
            # startupinfo		                只在windows下有效，将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
            # createionflags		                同上

p=subprocess.Popen("df -h",shell=True,stdout=subprocess.PIPE)
# 【Popen】：
# Popen.poll()用于检查子进程是否已经结束。设置并返回returncode属性。
# Popen.wait()等待子进程结束。设置并返回returncode属性。
# 注意： 如果子进程输出了大量数据到stdout或者stderr的管道，并达到了系统pipe的缓存大小的话，
        #   子进程会等待父进程读取管道，而父进程此时正wait着的话，将会产生传说中的死锁，后果是非常严重滴。
        # 建议使用communicate() 来避免这种情况的发生。
p.communicate(input=None)
# 和子进程交互：发送数据到stdin，并从stdout和stderr读数据，直到收到EOF。等待子进程结束。可选的input如有有的话，要为字符串类型。
# 此函数返回一个元组： (stdoutdata , stderrdata ) 。
# 注意，要给子进程的stdin发送数据，则Popen的时候，stdin要为PIPE；同理，要可以接收数据的话，stdout或者stderr也要为PIPE。
p1=subprocess.Popen('cat /etc/passwd',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
p2=subprocess.Popen('grep 0:0',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
# 注意：读到的数据会被缓存在内存里，所以数据量非常大的时候要小心了。
p.communicate()
# (b'Filesystem     Size    Used   Avail Capacity  Mounted on\n/dev/ad0s1a    713M    313M    343M    48%    /\ndevfs          1.0K    1.0K      0B   100%    /dev\n/dev/ad0s1e    514M    2.1M    471M     0%    /tmp\n/dev/ad0s1f    4.3G    2.5G    1.4G    64%    /usr\n/dev/ad0s1d    2.0G    121M    1.7G     6%    /var\n', None)
# Communicate()返回一个元组：(stdoutdata, stderrdata)。
# 注意：如果希望通过进程的stdin向其发送数据，在创建Popen对象的时候，参数stdin必须被设置为PIPE。同样，如果希望从stdout和stderr获取数据，必须将stdout和stderr设置为PIPE。
# Popen.send_signal(signal)向子进程发送信号。
# Popen.terminate()停止(stop)子进程。在windows平台下，该方法将调用WindowsAPI   TerminateProcess（）来结束子进程。
# Popen.kill()杀死子进程。
# Popen.stdin/Popen.stdout/Popen.stderr如果在创建Popen对象是，参数被设置为PIPE，将返回一个文件对象用于策子进程发送指令。否则返回None。
# Popen.pid获取子进程的进程ID。
# Popen.returncode获取进程的返回值。如果进程还没有结束，返回None。
# time_start = time.time()
# max_check_time = 3
# html_output_folder, src_file = '', ''
# cmd = "pdf2htmlEX --no-drm 1 --embed-css 0 --embed-image 0 --embed-font 0 " \
#       "--split-pages 1 --fit-width 748 --css-filename html.css --dest-dir %s " \
#       "--embed-external-font 0 --auto-hint 1 %s" % (html_output_folder, src_file)
# cmd_list = cmd.split(" ")
# sub2 = subprocess.Popen(cmd_list)
# i = 0
# while 1:
#     ret1 = subprocess.Popen.poll(sub2)
#     if ret1 == 0:
#         time_end = time.time()
#         time_take = int(time_end - time_start + 0.5)
#         with global_value_lock:
#             success_ids[param[2]] = time_take
#         print(sub2.pid, 'end')
#         break
#     elif ret1 is None:
#         print(sub2.pid, 'running')
#         if i >= max_check_time:
#             time_end = time.time()
#             time_take = int(time_end - time_start + 0.5)
#             with global_value_lock:
#                 timeout_ids[param[2]] = time_take
#             sub2.kill()
#             log_insert("%s%s%s" % (log_dir(output_folder), os.sep, "convert_log.txt"), src_file, "Timeout_Error",
#                        'None')
#             print("*****************Timeout_Error*****************")
#             break
#         time.sleep(check_time)
#     else:
#         time_end = time.time()
#         time_take = int(time_end - time_start + 0.5)
#         with global_value_lock:
#             converterror_ids[param[2]] = time_take
#         log_insert("%s%s%s" % (log_dir(output_folder), os.sep, "convert_log.txt"), src_file, "Process_Term_Error",
#                    str(ret1))
#         print(sub2.pid, 'term', ret1, ret1)
#         break
#     i += 1
# # ！！注意：当我们直接用cmd而非cmd_list时，得到的pid并不是pdf2html起的进程，而是其父进程，切记切记
# args = ''
# subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None,
#                  close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None,
#                  creationflags=0)
# 可以执行shell命令的相关模块和函数有：
# os.system
# os.spawn
print(subprocess.getstatusoutput('dir'))
# (0, '/home/ronny')
print(subprocess.getoutput('dir'))
# '/home/ronny'
print(subprocess.getstatus('dir'))

ret1 = subprocess.call("ifconfig")
ret2 = subprocess.call("ipconfig")
print(ret1)  # 0
print(ret2)  # 1

ret = subprocess.call(["ls", "-l"], shell=False)  # shell为False的时候命令必须分开写
ret = subprocess.call("ls -l", shell=True)
subprocess.check_call(["ls", "-l"])
subprocess.check_call("exit 1", shell=True)
subprocess.check_output(["echo", "Hello World!"])
subprocess.check_output("exit 1", shell=True)
(4)
# subprocess.Popen(...)#用于执行复杂的系统命令
ret1 = subprocess.Popen(["mkdir", "t1"])
ret2 = subprocess.Popen("mkdir t2", shell=True)
obj = subprocess.Popen("mkdir t3", shell=True, cwd='/home/dev', )  # 在cwd目录下执行命令
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
obj.stdin.close()
cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
out_error_list = obj.communicate()
print(out_error_list)
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
out_error_list = obj.communicate('print("hello")')
print(out_error_list)