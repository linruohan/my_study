import os,time
import logging
logging.getLogger().setLevel(logging.INFO)
import ctypes, sys,stat

# if not ctypes.windll.shell32.IsUserAnAdmin():
#     if sys.version_info[0] == 3:  # in python3
#         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#     else:  # in python2.x
#         ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)

os.chmod(os.path.realpath(__file__), stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO) # mode:777
def admin():
    #获取管理员权限
    if not ctypes.windll.shell32.IsUserAnAdmin():
        if sys.version_info[0] == 3:# in python3
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)


class ManageService:
    def __init__(self,name):
        if isinstance(name,str):
            self.name=name
        else:
            print('name is error!!')
    def status(self):
        serviceNames = os.popen("sc query type= all state= all |findstr /i %s"%self.name).read()
        self.name=serviceNames.split('SERVICE_NAME: ')[1].split('\n')[0]
        status=""
        result = os.popen("sc query %s" % self.name).read()
        if "RUNNING" in result:
            status="RUNNING"
        elif "START_PENDING" in result:
            status = "START_PENDING"
        elif "STOP_PENDING" in result:
            status = "STOP_PENDING"
        elif "STOPPED" in result:
            status = "STOPPED"
        else:
            status = "other"
        return status
    def start(self):
        if self.status() == "RUNNING":
            # print("The Service %s is already started!!! "  % self.name)
            return None
        os.popen("sc start %s" % self.name).read()
        while(True):
            # logging.info("The Service %s is starting....... " % self.name)
            if self.status()=="RUNNING":
                # logging.info("The Service started Succesivlly")
                break
            time.sleep(1)
    def stop(self):
        if self.status() == "STOPPED":
            # print("The Service %s is already stopped!!! "  % self.name)
            return None
        os.popen("sc stop %s" % self.name).read()
        while (True):
            # logging.info("Stoping Service ........")
            if self.status() == "STOPPED":
                # logging.info("The Service stoped Succesivlly")
                break
            time.sleep(1)
    def started_services(self):
        service_started = []
        s = os.popen("net start").read()
        for i in s.split("\n")[2:-3]:
            service_started.append(i.strip())
        # print(service_started)
        return service_started
def deleteFile(filepath):
    if os.path.isfile(filepath):
        try:
            os.remove(filepath)
        except:
            print("delete File failure: %s" % filepath)
    elif os.path.isdir(filepath):
        for item in os.listdir(filepath):
            itemsrc = os.path.join(filepath, item)
            deleteFile(itemsrc)
        try:
            os.rmdir(filepath)
        except:
            print("delete Folder failure: %s" % filepath)

#拷贝文件
# shutil.copyfile(src, target)

if __name__ == '__main__':
    # s = ManageService("mysql571")
    s=ManageService("apache2.2")
    s.stop()
    # s.start()
    # s.status()

    # os.path.realpath(__file__)
    print(os.path.realpath(__file__))
