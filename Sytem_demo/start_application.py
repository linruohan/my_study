# coding=gbk
import os, win32api, io, sys, time, subprocess,win32process
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')

os.startfile(r'C:\Windows\System32\calc.exe')
os.system('notepad')
os.system('notepad 001.txt')
os.system("taskkill /F /IM notepad.exe")
b = os.popen('mkdir nwdir', 'r', 1)
# command -- ʹ�õ����
# mode -- ģʽȨ�޿����� 'r'(Ĭ��) �� 'w'��
# bufsize -- ָ�����ļ���Ҫ�Ļ����С��0��ζ���޻��壻1��ζ���л��壻������ֵ��ʾʹ�ò�����С�Ļ��壨���ֵ�����ֽ�Ϊ��λ��������bufsize��ζ��ʹ��ϵͳ��Ĭ��ֵ��һ����˵������tty�豸�������л��壻���������ļ�������ȫ���塣���û�иĲ�����ʹ��ϵͳ��Ĭ��ֵ��
win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)
# ShellExecute(hwnd, op , file , params , dir , bShow )
# ���������������ʾ��
# ��     hwnd�������ڵľ�������û�и����ڣ���Ϊ0��
# ��     op��Ҫ���еĲ�����Ϊ��open������print������Ϊ�ա�
# ��     file��Ҫ���еĳ��򣬻��ߴ򿪵Ľű���
# ��     params��Ҫ����򴫵ݵĲ���������򿪵�Ϊ�ļ�����Ϊ�ա�
# ��     dir�������ʼ����Ŀ¼��
# ��     bShow���Ƿ���ʾ���ڡ�0����ʾ��1����ʾ
win32api.ShellExecute(0, 'open', 'notepad.exe', '001.txt', '', 1)
win32api.ShellExecute(0, 'open', 'http://www.python.org', '','',1)#����ҳ
win32process.CreateProcess('c:\\windows\\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None,
                           win32process.STARTUPINFO())
# (4)ʹ��ģ��subprocess
# ˵���׻���subprocess��Ϊǿ����ʵ�ֺܶ๦�ܣ�����shell�����ȡ������Ϣ����ص��ù��̣���ʱ��ֹ�ȣ�Ҫ����ù��̲����������ܽ�����
            # ��CreateProcess������һ���ַ���������
            # args	                    shell����������ַ��������������ͣ��磺list��Ԫ�飩
            # bufsize	                ָ�����塣0 �޻���,1 �л���,���� ��������С,��ֵ ϵͳ����
            # stdin, stdout, stderr		                �ֱ��ʾ����ı�׼���롢�����
                        # subprocess.PIPE  �ڴ���Popen����ʱ��subprocess.PIPE���Գ�ʼ��stdin, stdout��stderr��������ʾ���ӽ���ͨ�ŵı�׼����
                        #subprocess.STDOUT   ����Popen����ʱ�����ڳ�ʼ��stderr��������ʾ������ͨ����׼����������
            # preexec_fn		                ֻ��Unixƽ̨����Ч������ָ��һ����ִ�ж���callable object�����������ӽ�������֮ǰ������
            # close_sfs		                ��windowsƽ̨�£����close_fds������ΪTrue�����´������ӽ��̽�����̳и����̵����롢���������ܵ������Բ��ܽ�close_fds����ΪTrueͬʱ�ض����ӽ��̵ı�׼���롢��������(stdin, stdout, stderr)��
            # shell		                ͬ��
            # cwd		                ���������ӽ��̵ĵ�ǰĿ¼
            # env		                ����ָ���ӽ��̵Ļ������������env = None���ӽ��̵Ļ����������Ӹ������м̳С�
            # universal_newlines		                ��ͬϵͳ�Ļ��з���ͬ��True -> ͬ��ʹ�� \n
            # startupinfo		                ֻ��windows����Ч���������ݸ��ײ��CreateProcess()���������������ӽ��̵�һЩ���ԣ��磺�����ڵ���ۣ����̵����ȼ��ȵ�
            # createionflags		                ͬ��

p=subprocess.Popen("df -h",shell=True,stdout=subprocess.PIPE)
# ��Popen����
# Popen.poll()���ڼ���ӽ����Ƿ��Ѿ����������ò�����returncode���ԡ�
# Popen.wait()�ȴ��ӽ��̽��������ò�����returncode���ԡ�
# ע�⣺ ����ӽ�������˴������ݵ�stdout����stderr�Ĺܵ������ﵽ��ϵͳpipe�Ļ����С�Ļ���
        #   �ӽ��̻�ȴ������̶�ȡ�ܵ����������̴�ʱ��wait�ŵĻ������������˵�е�����������Ƿǳ����صΡ�
        # ����ʹ��communicate() ��������������ķ�����
p.communicate(input=None)
# ���ӽ��̽������������ݵ�stdin������stdout��stderr�����ݣ�ֱ���յ�EOF���ȴ��ӽ��̽�������ѡ��input�����еĻ���ҪΪ�ַ������͡�
# �˺�������һ��Ԫ�飺 (stdoutdata , stderrdata ) ��
# ע�⣬Ҫ���ӽ��̵�stdin�������ݣ���Popen��ʱ��stdinҪΪPIPE��ͬ��Ҫ���Խ������ݵĻ���stdout����stderrҲҪΪPIPE��
p1=subprocess.Popen('cat /etc/passwd',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
p2=subprocess.Popen('grep 0:0',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
# ע�⣺���������ݻᱻ�������ڴ�������������ǳ����ʱ��ҪС���ˡ�
p.communicate()
# (b'Filesystem     Size    Used   Avail Capacity  Mounted on\n/dev/ad0s1a    713M    313M    343M    48%    /\ndevfs          1.0K    1.0K      0B   100%    /dev\n/dev/ad0s1e    514M    2.1M    471M     0%    /tmp\n/dev/ad0s1f    4.3G    2.5G    1.4G    64%    /usr\n/dev/ad0s1d    2.0G    121M    1.7G     6%    /var\n', None)
# Communicate()����һ��Ԫ�飺(stdoutdata, stderrdata)��
# ע�⣺���ϣ��ͨ�����̵�stdin���䷢�����ݣ��ڴ���Popen�����ʱ�򣬲���stdin���뱻����ΪPIPE��ͬ�������ϣ����stdout��stderr��ȡ���ݣ����뽫stdout��stderr����ΪPIPE��
# Popen.send_signal(signal)���ӽ��̷����źš�
# Popen.terminate()ֹͣ(stop)�ӽ��̡���windowsƽ̨�£��÷���������WindowsAPI   TerminateProcess�����������ӽ��̡�
# Popen.kill()ɱ���ӽ��̡�
# Popen.stdin/Popen.stdout/Popen.stderr����ڴ���Popen�����ǣ�����������ΪPIPE��������һ���ļ��������ڲ��ӽ��̷���ָ����򷵻�None��
# Popen.pid��ȡ�ӽ��̵Ľ���ID��
# Popen.returncode��ȡ���̵ķ���ֵ��������̻�û�н���������None��
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
# # ����ע�⣺������ֱ����cmd����cmd_listʱ���õ���pid������pdf2html��Ľ��̣������丸���̣��м��м�
# args = ''
# subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None,
#                  close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None,
#                  creationflags=0)
# ����ִ��shell��������ģ��ͺ����У�
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

ret = subprocess.call(["ls", "-l"], shell=False)  # shellΪFalse��ʱ���������ֿ�д
ret = subprocess.call("ls -l", shell=True)
subprocess.check_call(["ls", "-l"])
subprocess.check_call("exit 1", shell=True)
subprocess.check_output(["echo", "Hello World!"])
subprocess.check_output("exit 1", shell=True)
(4)
# subprocess.Popen(...)#����ִ�и��ӵ�ϵͳ����
ret1 = subprocess.Popen(["mkdir", "t1"])
ret2 = subprocess.Popen("mkdir t2", shell=True)
obj = subprocess.Popen("mkdir t3", shell=True, cwd='/home/dev', )  # ��cwdĿ¼��ִ������
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