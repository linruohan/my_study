#coding=utf-8
import subprocess,re,psutil
def get_alive_port(program):
    """
      获取目标程序占用的端口
      :param program {string} 目标进程
      :return portlist {list} 目标进程占用的端口列表
     """
    cmd = 'wmic process where caption="%s" get commandline /value' % program
    ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    portlist = []
    while True:
        out = ps.stdout.readline()
        if out:
            out = out.decode("gb2312")
            templist = re.findall("[0-9]{4,5}", out)
            portlist.extend(templist)
        else:
            break
        return portlist
def howmuch_memory(program):
     """
      监控目标进程内存是否超过阀值，若超过则关闭
     """
     cmd = 'wmic process where caption="%s" get processid /value' % program
     ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
     pids = []
     while True:
          out = ps.stdout.readline()
          if out:
               out = out.decode("gb2312")
               templist = re.findall("[0-9]{3,6}", out)
               pids.extend(templist)
          else:
            break
     for pid in pids:
          try:
               p = psutil.Process(int(pid))
               p_memory = p.memory_info()
               if int(p_memory.rss / (1024 * 1024)) >= 200:
                    p.kill()
          except Exception as e:
           print("出现如下错误:{0}".format(e))
           continue

if __name__ == '__main__':
    s=get_alive_port('Mysql')
    print(s)