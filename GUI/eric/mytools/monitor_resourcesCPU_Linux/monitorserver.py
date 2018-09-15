#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 15:59
# @Desc    : 服务器监控代码
# @File    : monitorserver.py
# @Software: PyCharm

"""仅仅对linux系统监测有效"""
import pexpect
import re
import time
import threading

class RomoteMonitor:
    """
    主方法
    127.0.0.1#远程服务器ip地址
    """
    def __init__(self,host,user,password):
        self.host=host
        self.user=user
        self.password=password

    def ssh_command(self,command):
        ssh_new_key = 'Are you sure you want to continue connecting'
        child = pexpect.spawn('ssh -l %s %s %s' % (self.user, self.host, command))
        i = child.expect([pexpect.TIMEOUT, ssh_new_key, 'password: '])
        if i == 0:
            print('ERROR!')
            print('SSH could not login. Here is what SSH said:')
            print(child.before, child.after)
            return None
        if i == 1:
            child.sendline('yes')
            child.expect('password: ')
            i = child.expect([pexpect.TIMEOUT, 'password: '])
            if i == 0:
                print('ERROR!')
                print('SSH could not login. Here is what SSH said:')
                print( child.before, child.after)
                return None
        child.sendline(self.password)
        return child
    def mem_info(self):
        """
        内存监控
        """
        child = self.ssh_command("cat /proc/meminfo")
        child.expect(pexpect.EOF)
        mem = child.before
        mem_values = re.findall("(\d+)\ kB", mem)
        MemTotal = mem_values[0]
        MemFree = mem_values[1]
        Buffers = mem_values[2]
        Cached = mem_values[3]
        SwapCached = mem_values[4]
        SwapTotal = mem_values[13]
        SwapFree = mem_values[14]
        print('******************************内存监控*********************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        print("总内存：", MemTotal)
        print("空闲内存：", MemFree)
        print("给文件的缓冲大小:", Buffers)
        print("高速缓冲存储器使用的大小:", Cached)
        print("被高速缓冲存储用的交换空间大小:", SwapCached)
        print("给文件的缓冲大小:", Buffers)
        if int(SwapTotal) == 0:
            print(u"交换内存总共为：0")
        else:
            Rate_Swap = 100 - 100 * int(SwapFree) / float(SwapTotal)
            print(u"交换内存利用率：", Rate_Swap)
        Free_Mem = int(MemFree) + int(Buffers) + int(Cached)
        Used_Mem = int(MemTotal) - Free_Mem
        Rate_Mem = 100 * Used_Mem / float(MemTotal)
        print( u"内存利用率：", str("%.2f" % Rate_Mem), "%")
    def vm_stat_info(self):
        """
        内核线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息
        """
        child = self.ssh_command("vmstat 1 2 | tail -n 1")
        child.expect(pexpect.EOF)
        vmstat_info = child.before.strip().split()
        processes_waiting = vmstat_info[0]
        processes_sleep = vmstat_info[1]
        swpd = vmstat_info[2]
        free = vmstat_info[3]
        buff = vmstat_info[4]
        cache = vmstat_info[5]
        si = vmstat_info[6]
        so = vmstat_info[7]
        io_bi = vmstat_info[8]
        io_bo = vmstat_info[9]
        system_interrupt = vmstat_info[10]
        system_context_switch = vmstat_info[11]
        cpu_user = vmstat_info[12]
        cpu_sys = vmstat_info[13]
        cpu_idle = vmstat_info[14]
        cpu_wait = vmstat_info[15]
        st = vmstat_info[16]
        print('****************************内核线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息监控****************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        print("等待运行进程的数量:", processes_waiting)
        print("处于不间断状态的进程:", processes_sleep)
        print("使用虚拟内存(swap)的总量:", swpd)
        print("空闲的内存总量:", free)
        print("用作缓冲的内存总量:", buff)
        print("用作缓存的内存总量:", cache)
        print("交换出内存总量 :", si)
        print("交换入内存总量 :", so)
        print("从一个块设备接收:", io_bi)
        print("发送到块设备:", io_bo)
        print("每秒的中断数:", system_interrupt)
        print("每秒的上下文切换数:", system_context_switch)
        print("用户空间上进程运行的时间百分比:", cpu_user)
        print( "内核空间上进程运行的时间百分比:", cpu_sys)
        print("闲置时间百分比:", cpu_idle)
        print("等待IO的时间百分比:", cpu_wait)
        print("从虚拟机偷取的时间百分比:", st)
    def cpu_info(self):
        '''
        cpu监控
        '''
        child = self.ssh_command("cat /proc/cpuinfo")
        child.expect(pexpect.EOF)
        cpuinfo = child.before
        cpu_num = re.findall('processor.*?(\d+)', cpuinfo)[-1]
        cpu_num = str(int(cpu_num) + 1)
        print('***************************************cpu监控***************************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        print(u"CPU数目：", cpu_num)
        li = cpuinfo.replace('\t', '').split('\r')
        CPUinfo = {}
        procinfo = {}
        nprocs = 0
        for line in li:
            if line.find("processor") > -1:
                CPUinfo['CPU%s' % nprocs] = procinfo
                nprocs = nprocs + 1
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
        for processor in CPUinfo.keys():
            print("CPU属于的名字及其编号、标称主频:", CPUinfo[processor]['model name'])
            print("CPU属于其系列中的哪一代的代号:", CPUinfo[processor]['model'])
            print("CPU制造商:", CPUinfo[processor]['vendor_id'])
            print("CPU产品系列代号:", CPUinfo[processor]['cpu family'])
            print("CPU的实际使用主频:", CPUinfo[processor]['cpu MHz'])
    def load_stat(self):
        """
        负载均衡
        """
        child = self.ssh_command("cat /proc/loadavg")
        child.expect(pexpect.EOF)
        loadavgs = child.before.strip().split()
        print( '************************负载均衡监控****************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        print("系统5分钟前的平均负载：", loadavgs[0])
        print( "系统10分钟前的平均负载：", loadavgs[1])
        print("系统15分钟前的平均负载：", loadavgs[2])
        print("分子是正在运行的进程数,分母为总进程数：", loadavgs[3])
        print("最近运行的进程id：", loadavgs[4])
    def ionetwork(self):
        """
        获取网络接口的输入和输出
        """
        child = self.ssh_command("cat /proc/net/dev")
        child.expect(pexpect.EOF)
        netdata = child.before
        li = netdata.strip().split('\n')
        print( '************************获取网络接口的输入和输出监控****************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        net = {}
        for line in li[2:]:
            line = line.split(":")
            eth_name = line[0].strip()
            # if eth_name != 'lo':
            net_io = {}
            net_io['Receive'] = round(float(line[1].split()[0]) / (1024.0 * 1024.0), 2)
            net_io['Transmit'] = round(float(line[1].split()[8]) / (1024.0 * 1024.0), 2)
            net[eth_name] = net_io
        print(net)
    def disk_stat(self):
        """
            磁盘空间监控
            """
        child = self.ssh_command("df -h")
        child.expect(pexpect.EOF)
        disk = child.before
        disklist = disk.strip().split('\n')
        disklists = []
        for disk in disklist:
            disklists.append(disk.strip().split())
        print('************************磁盘空间监控****************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        for i in disklists[1:]:
            print("\t文件系统：", i[0],)
            print("\t容量：", i[1],)
            print("\t已用：", i[2],)
            print("\t可用：", i[3],)
            print("\t已用%挂载点：", i[4])
    def getComStr(self):
        """
        端口监控
        一般是远程服务器用户名用户
        """
        child = self.ssh_command("netstat -tpln")
        child.expect(pexpect.EOF)
        Com = child.before
        print('******************************端口监控*********************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        print(Com)
    def cpu(self):
        """
        获取网络接口的输入和输出
        """
        child = self.ssh_command( 'cat /proc/stat | grep "cpu "')
        child.expect(pexpect.EOF)
        child1 = self.ssh_command( 'cat /proc/stat | grep "cpu "')
        child1.expect(pexpect.EOF)
        cpus = child.before.strip().split()
        cpus1 = child1.before.strip().split()
        print('************************cpu使用情况****************************')
        print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
        T1 = int(cpus[1]) + int(cpus[2]) + int(cpus[3]) + int(cpus[4]) + int(cpus[5]) + int(cpus[6]) + int(cpus[8]) + int(
            cpus[9])
        T2 = int(cpus1[1]) + int(cpus1[2]) + int(cpus1[3]) + int(cpus1[4]) + int(cpus1[5]) + int(cpus1[6]) + int(
            cpus1[8]) + int(cpus1[9])
        Tol = T2 - T1
        Idle = int(cpus1[4]) - int(cpus[4])
        print('总的cpu时间1:', T1)
        print( '总的cpu时间2:', T2)
        print('时间间隔内的所有时间片:', Tol)
        print('计算空闲时间idle:', Idle)
        print("计算cpu使用率：", 100 * (Tol - Idle) / Tol, "%")

    def alltask(self):
        """
        第一种执行
        """
        try:
            threads = []
            t1 = threading.Thread(target=self.mem_info)
            threads.append(t1)
            t2 = threading.Thread(target=self.vm_stat_info)
            threads.append(t2)
            t3 = threading.Thread(target=self.cpu_info)
            threads.append(t3)
            t4 = threading.Thread(target=self.load_stat)
            threads.append(t4)
            t5 = threading.Thread(target=self.ionetwork)
            threads.append(t5)
            t6 = threading.Thread(target=self.disk_stat)
            threads.append(t6)
            t7 = threading.Thread(target=self.getComStr)
            threads.append(t7)
            t8 = threading.Thread(target=self.cpu)
            threads.append(t8)
            for n in range(len(threads)):
                threads[n].start()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    host="193.169.100.138"
    user="Administrator"
    password="Admin123"
    monitor=RomoteMonitor(host,user,password)
    monitor.alltask()