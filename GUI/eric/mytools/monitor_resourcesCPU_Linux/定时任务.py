#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc    : 定时任务，以需要的时间间隔执行某个命令
import time, os
from monitorserver import alltask

def roll_back(cmd, inc=60):
    while True:
        # 执行方法，函数
        alltask()
        time.sleep(inc)
roll_back("echo %time%", 5)
# 第二种：
import time, os
def roll_back(cmd, inc=60):
    while True:
        # 监控代码文件所在位置
        os.system('python  /home/../monitorserver.py');
        time.sleep(inc)

roll_back("echo %time%", 5)
# 做过监控应该都知道，我们主要监控服务器，
# 负载均衡、磁盘、内存、CPU、网络接口（流量）、端口代码，

