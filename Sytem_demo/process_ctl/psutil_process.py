import psutil
from psutil import _psutil_windows
import os
import psutil
import time
from datetime import datetime
from subprocess import PIPE
import operator


class Use_psutil:
    def __init__(self):
        self.pidDictionarys = {}
        # self.walk_path()

    def pids(self):
        # 返回一个列表，内容是当前所有进程的pid。
        # print( psutil.pids())
        return psutil.pids()

    def get_name_by_pid(self, pid):
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
        else:
            print("Pid is not existed or not running...")
            raise ValueError
        return p.name()

    def pinfo(self, pid):
        p = psutil.Process(pid)
        print(p.as_dict())
        pinfo = {'name': p.name(),  # 进程名
                 'exe': p.exe(),  # 进程的工作目录绝对路径
                 'cwd': p.cwd(),  # 进程的bin路径
                 'cmdline': p.cmdline(),
                 'pid': p.pid,
                 'ppid': p.ppid(),
                 'parent': p.parent(),
                 'children': p.children(),
                 'status': p.status(),  # 进程状态
                 'username': p.username(),  # 执行用户的名
                 'create_time': p.create_time(),  # 进程创建时间
                 # 'terminal': p.terminal(),#Unix
                 # 'uids': p.uids(),# 进程uid信息----Unix
                 # 'gids': p.gids(),# 进程的gid信息----Unix
                 'cpu_times': p.cpu_times(),  # 进程的cpu时间信息,包括user,system两个cpu信息
                 'cpu_percent(interval=1.0)': p.cpu_percent(interval=1.0),  # 进程的cpu时间信息,包括user,system两个cpu信息
                 'cpu_affinity': p.cpu_affinity(),  # get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
                 'cpu_affinity([0, 1])  ': p.cpu_affinity([0, 1]),  # set
                 'memory_info': p.memory_info(),  # 进程内存rss,vms信息
                 'memory_full_info()  ': p.memory_full_info(),  # "real" USS memory usage (Linux, macOS, Win only)
                 'memory_percent': p.memory_percent(),  # 进程内存利用率
                 'memory_maps': p.memory_maps(),
                 'io_counters': p.io_counters(),  # 进程的IO信息,包括读写IO数字及参数
                 'open_files': p.open_files(),
                 'connections': p.connections(),  # 返回进程对象的列表
                 'num_threads': p.num_threads(),  # 进程开启的线程数
                 'threads': p.threads(),
                 'num_ctx_switches': p.num_ctx_switches(),
                 'nice': p.nice(),
                 # 'nice(10)  ': p.nice(10),  # set
                 # 'ionice(psutil.IOPRIO_CLASS_IDLE)  ': p.ionice(psutil.IOPRIO_CLASS_IDLE),
                 # IO priority (Win and Linux only)
                 'ionice': p.ionice(),
                 # 'rlimit(psutil.RLIMIT_NOFILE, (5, 5))  ': p.rlimit(psutil.RLIMIT_NOFILE, (5, 5)),
                 # set resource limits (Linux only)
                 # 'rlimit(psutil.RLIMIT_NOFILE)': p.rlimit(psutil.RLIMIT_NOFILE),
                 'environ': p.environ(),
                 'as_dict': p.as_dict(),
                 'is_running': p.is_running(),
                 'suspend': p.suspend(),
                 'resume': p.resume(),
                 # 'terminate': p.terminate(),#会关闭当前进程
                 # 'wait(timeout)': p.wait(timeout=3),#等三秒关闭当前进程
                 }
        return p.as_dict()

    def pinfo_by_attrs(self, *argvs):
        attrs = argvs
        # for proc in psutil.process_iter(attrs=['pid', 'name']):
        for proc in psutil.process_iter(attrs=attrs):
            print(proc.info)

    def get_proc_by_name(pname):
        for proc in psutil.process_iter():
            try:
                if proc.name().lower() == pname.lower():
                    return proc  # return if found one
            except psutil.AccessDenied:
                pass
            except psutil.NoSuchProcess:
                pass
        return None

    def get_proc_by_id(self, pid):
        # 在知道某个特定进程的pid之后，可以使用p = psutil.Process(pid)来得到一个进程对象。
        # 这个进程对象相比于subprocess.Popen给出的进程对象有更多的信息
        return psutil.Process(pid)

    #  CPU
    def cpu_times(self):
        return psutil.cpu_times()

    def cpu_percent(self, interval=1, percpu=True):
        '''percpu means every little CPU
        it is timeable,即时性的，某一时刻的CPU百分比
        '''
        if interval and percpu: return psutil.cpu_percent()
        for i in range(3):
            # percent=psutil.cpu_percent(interval)
            # print("%.2f%%"%percent)
            percent = psutil.cpu_percent(interval, percpu)
            print(list(map(lambda x: "%.2f%%" % x, percent)))
        return psutil.cpu_percent(interval, percpu)

    def cpu_count(self, logical=True):
        '''logical逻辑处理器'''
        # print('psutil.cpu_count():', psutil.cpu_count())  # 返回cpu个数
        # print('psutil.cpu_times():', psutil.cpu_times())  # 返回cpu使用时间信息对象，包括用户时间，空转时间等等。这些信息都是属性，可以用.访问
        count = psutil.cpu_count()
        if not logical:
            count = psutil.cpu_count(logical=False)
        # print("cpu_count:%d" % count)
        return count

    def cpu_status(self):
        return psutil.cpu_stats()

    def cpu_freq(self):
        return psutil.cpu_freq()

    # memory
    def memory(self):
        vm = psutil.virtual_memory()  # 虚拟内存 # 系统内存信息
        sm = psutil.swap_memory()  # 交换内存 # swap内存信息
        return vm, sm

    # Disks
    def disks(self):
        disks = (psutil.disk_partitions(),
                 psutil.disk_usage('/'),
                 psutil.disk_io_counters(perdisk=False))
        return disks

    def top(self):
        print(psutil.test())

    # Network
    def network(self):
        net = (
            psutil.net_io_counters(pernic=True),  # 网卡属性，连接数，流量等信息
            psutil.net_connections(),
            psutil.net_if_addrs(),
            psutil.net_if_stats())
        return net

    # Sensors 传感器
    def sensors(self):
        s = (
            psutil.sensors_temperatures(),
            psutil.sensors_fans(),
            psutil.sensors_battery())
        return s

    # Other system info
    def user_btime(self):
        print('psutil.boot_time():', psutil.boot_time())  # 返回系统开机的时间
        print('psutil.users():', psutil.users())  # 返回用户信息
        user, boot_time = psutil.users(), psutil.boot_time()
        return user, boot_time

    # Windows services
    def win_service_info(self, name):
        '''
        # s = psutil.win_service_get('alg')
        # print(s.display_name(),s.username(),s.name(),s.description())
        :param name:
        :return:
        '''
        win_list = list(psutil.win_service_iter())
        if name in [i.name() for i in win_list]:
            s = psutil.win_service_get(name)
            return s.as_dict()
        else:
            print("Name is invalid...Just like this:")
            print(str([i.name() for i in win_list]))

        return None

    def on_terminate(proc):
        # waits for multiple processes to terminate
        # gone, alive = psutil.wait_procs(procs_list, timeout=3, callback=on_terminate)
        print("process {} terminated".format(proc))

    # Popen
    def popen(self):
        p = psutil.Popen(["c:\python36\python", "-c", "print('hello')"], stdout=PIPE)
        p.communicate()
        p.wait(timeout=2)
        print(p.name())
        print(p.username())

    def all_info(self):
        pidList = psutil.pids()
        outputFile = open('output' + str(time.strftime('%Y-%m-%d-%S')) + '.log', 'a')
        for pid in pidList:
            p = psutil.Process(pid)
            attrs = ['name', 'exe', 'cwd', 'status', 'create_time', 'cpu_percent', 'cpu_times',
                     'cpu_affinity', 'memory_percent', 'memory_info', 'io_counters', 'connections', 'num_threads',
                     'username']
            pidDictionary = p.as_dict(attrs=attrs)
            self.pidDictionarys[pid] = pidDictionary
            # 排序输出
            newpidDictionary = dict(
                sorted(pidDictionary.items(), key=operator.itemgetter(0)))  # 按照item中的第一个字符进行排序，即按照key排序
            for key in newpidDictionary.keys():
                tempText = key + ':' + str(newpidDictionary[key]) + '\n'
                outputFile.write(tempText)
            outputFile.write('*' * 100 + '\n\n')  # 写完一个进程，打印一行间隔符
        outputFile.close()

    def top_demo(self):
        logPath = os.path.dirname(__file__) + r'/proclogs/'
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        separator = "-" * 80
        format = "%7s %7s %12s %12s %30s %s  %s"
        format2 = "%7.4f\t%7.7s%%\t%12s\t%12s\t%30s\t%s\t%s"
        print(format % ("%CPU", "%MEM", "VMS", "RSS", "NAME", "PATH", "CREATETIME"))
        while True:
            logPath1 = logPath + r'/procLog%s.log' % str(time.strftime('%Y-%m-%d-%S'))
            f = open(logPath1, 'w')
            f.write(separator + "\n" + time.ctime() + "\n")
            f.write(format % ("%CPU", "%MEM", "VMS", "RSS", "NAME", "PATH", "CREATETIME") + "\n")
            pidList = psutil.pids()
            for pid in pidList:
                p = psutil.Process(pid)
                s = p.create_time()
                createtime = datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s)), "%Y-%m-%d %H:%M:%S")
                # print("create_time:%s"%createtime)
                cpu_percent = float(p.cpu_percent(interval=0.3) / int(self.cpu_count(True)))
                mem_percent = p.memory_percent()
                # print('cpu_percent:%.7s%%'%cpu_percent)
                rss, vms = p.memory_info()[0], p.memory_info()[1]
                name = p.name()
                try:
                    path = p.cwd()
                except  (psutil.ZombieProcess, psutil.AccessDenied, psutil.NoSuchProcess):
                    path = '?/'
                # print("path:",path)
                f.write(format2 % (cpu_percent, mem_percent, vms, rss, name, createtime, path))
                print(format2 % (cpu_percent, mem_percent, vms, rss, name, createtime, str(path)))
                f.write("\n\n")
            print("Finished log update!")
            time.sleep(3000)
            print("writing new log data!")
        f.close()


if __name__ == '__main__':
    ps = Use_psutil()
    # print(ps.pids())
    # print(ps.cpu_times())
    # print(ps.cpu_times()[1])
    # ps.cpu_percent()
    # ps.cpu_count(False)
    # print(ps.cpu_status())
    # print(ps.cpu_freq())
    # print(ps.memory())
    # print(ps.disks())
    # ps.top()
    # ps.win_service_info('12')
    # ps.pinfo(9284)
    # ps.write_log()
    # ps.top_demo()
    pidList = psutil.pids()
    p = psutil.Process(pidList[0])
    print(p.as_dict().keys())
    for i in p.as_dict().keys():print(i)
    print(p.cpu_percent())