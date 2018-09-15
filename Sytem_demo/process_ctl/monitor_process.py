# coding=utf-8
import psutil
import sys
import time
# 输入需要监测的进程PID
PID = 9284


def get_cpu_info():
    # 将结果记录到本地文本
    text = open('D:\\CPUresult.txt', 'w')
    i = 0
    # 博主新手靠这样来现实循环
    while i < 100000000000000:
        i = i + 1
        # 找出本机CPU的逻辑核个数
        cpucount = psutil.cpu_count(logical=True)
        print("cpucount:",cpucount)
        # 传入进程PID，实现监测功能
        process = psutil.Process(int(PID))
        # cpupercent = process.cpu_percent(interval=2)
        cpupercent = process.cpu_percent(interval=0.3,percpu=True)
        print("cpuperc:",cpupercent)
        # 得到进程CPU占用，同资源检测管理器的数据
        cpu = float(cpupercent / cpucount)
        print("cpu:%s/%s==%s"%(cpupercent,cpucount,cpu))
        print("\n\n")
        # if cpu <= 50:
        #     print(u'CPU使用率:%s%%' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        # else:
        #     print(u'CPU使用率:%s%%,占用率过高' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    text.close()


get_cpu_info()
