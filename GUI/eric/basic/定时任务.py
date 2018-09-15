#coding=utf-8
#这里需要引入三个模块
import time, os, sched
class Dingshi:
    # 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
    # 第二个参数以某种人为的方式衡量时间
    schedule = sched.scheduler(time.time, time.sleep)

    def perform_command(self,cmd, inc):
        os.system(cmd)

    def timming_exe(self,cmd, inc = 60):
        # enter用来安排某事件的发生时间，从现在起第n秒开始启动
        self.schedule.enter(inc, 0,  self.perform_command, (cmd, inc))
        # 持续运行，直到计划时间队列变成空为止
        self.schedule.run()

class Zhouqixing:
    # 周期性执行实例
    # 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
    # 第二个参数以某种人为的方式衡量时间
    schedule = sched.scheduler(time.time, time.sleep)

    def perform_command(self,cmd, inc):
        # 安排inc秒后再次运行自己，即周期运行
        self.schedule.enter(inc, 0, self.perform_command, (cmd, inc))
        os.system(cmd)

    def timming_exe(self,cmd, inc = 60):
        # enter用来安排某事件的发生时间，从现在起第n秒开始启动
        self.schedule.enter(inc, 0, self.perform_command, (cmd, inc))
        # 持续运行，直到计划时间队列变成空为止
        self.schedule.run()

class Xunhuan:
    def re_exe(self,cmd, inc = 60):
        while True:
            os.system(cmd);
            time.sleep(inc)

if __name__ == '__main__':
    d = Dingshi()
    print("show time after 10 seconds:")
    d.timming_exe("echo %time%", 10)

    # z = Zhouqixing()
    # print("show time after 10 seconds:")
    # z.timming_exe("echo %time%", 10)


    # x = Xunhuan()
    # x.re_exe("echo %time%", 3)