import sys
import win32com.client, wmi


class Use_win32com:
    '''仅限于windows系统 和WMI很类似
    windows是psutil，
    wmi也能够获取进程的信息，效率不太高，可以做监控等性能要求不太高的情况
    '''

    def __init__(self):
        self.wmi = win32com.client.GetObject('winmgmts:')
        self.processes = self.wmi.InstancesOf('win32_process')
        self.length = len(self.processes)
        print("Now running with 【%d】 processes." % self.length)

    def process(self, name):
        if name in self.process_names():
            process = self.wmi.ExecQuery('select * from Win32_Process where Name = "%s"' % name)
        else:
            print("The process name is invalid ,Please check and try again...")
            print('Process names is such values like these:\n' + '*' * 50)
            print("Examples...")
            print('\n%s】' % self.process_names())
            sys.exit(0)
            # raise NameError
        return process

    def process_names(self):
        # names = [process.Properties_('Name').Value for process in self.processes]  # get name
        names=[p.Name for p in self.processes]
        # print('names:', names)
        formatList = list(set(names))
        formatList.sort(key=names.index)
        # print('sorted names:', formatList)
        return formatList

    def propnames(self, name):
        # let's look at all the process property names
        return [prop.Name for prop in self.process(name)[0].Properties_]

    def get_value_by_propname(self, name, propname):
        if not propname in self.propnames(name): return None
        if propname == "ProcessId": return self.process(name)[0].Properties_(propname)
        # print("The process 【%s】 of %s:%s"%(self.name,propname,self.process[0].Properties_(propname).Value))
        return self.process(name)[0].Properties_(propname).Value

    def process_infos(self, name):
        infos = []
        for proname in self.propnames(name):
            info = self.get_value_by_propname(name, proname)
            infos.append(info)
            print("【%s】%s:%s" % (name, proname, info))
        return infos

    def processes_info(self):
        for p in self.processes:
            print(p.Name, p.Properties_('ProcessId'), \
                  int(p.Properties_('UserModeTime').Value) + int(p.Properties_('KernelModeTime').Value))
            children = self.wmi.ExecQuery(
                'Select * from win32_process where ParentProcessId=%s' % p.Properties_('ProcessId'))
            for child in children:
                print('\t', child.Name, child.Properties_('ProcessId'), \
                      int(child.Properties_('UserModeTime').Value) + int(child.Properties_('KernelModeTime').Value))

    def parent_processes(self):
        '''进程名，pid,cpu的运行时间'''
        for p in self.processes:
            name = p.Name
            pid = p.Properties_('ProcessId')
            cpu_run_time = int(p.Properties_('UserModeTime').Value) + int(p.Properties_('KernelModeTime').Value)
            print("【name：%s】<<<...%s....>>>【%s】秒" % (name, pid, cpu_run_time))

    def children_processes_by_ppid(self, ppid):
        '''进程名，pid,cpu的运行时间'''
        process = self.wmi.ExecQuery('select * from Win32_Process where ProcessId = "%s"' % ppid)
        children = self.wmi.ExecQuery(
            'Select * from win32_process where ParentProcessId=%s' % process[0].Properties_('ProcessId'))
        for child in children:
            print('\t', child.Name, child.Properties_('ProcessId'), \
                  int(child.Properties_('UserModeTime').Value) + int(child.Properties_('KernelModeTime').Value))


if __name__ == '__main__':
    s1 = Use_win32com()
    s1.process_names()
    s1.process_infos('csrss.exe')
    s1.parent_processes()
    s1.children_processes_by_ppid(5940)
