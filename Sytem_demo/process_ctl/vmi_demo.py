import wmi, sys

class Wmi_process:
    def __init__(self):
        self.processes = wmi.WMI().InstancesOf('Win32_Process')
        self.length = len(self.processes)
        print("Now running with 【%d】 processes." % self.length)
    def process(self,name):
        if name in self.process_names():
            process = wmi.WMI().ExecQuery('select * from Win32_Process where Name = "%s"' % name)
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
        names = [p.Name for p in self.processes]
        formatList = list(set(names))
        formatList.sort(key=names.index)
        return formatList
    # Here is how to get a single process and get its PID.
    def propnames(self,name):
        # let's look at all the process property names
        propname=[prop.Name for prop in self.process(name)[0].Properties_]
        return [prop.Name for prop in self.process(name)[0].Properties_]

    def get_value_by_propname(self,name, propname):
        if not propname in self.propnames(name): return None
        if propname == "ProcessId": return self.process(name)[0].Properties_(propname)
        # print("The process 【%s】 of %s:%s"%(self.name,propname,self.process[0].Properties_(propname).Value))
        return self.process(name)[0].Properties_(propname).Value

    def process_infos(self,name):
        infos = []
        for proname in self.propnames(name):
            info = self.get_value_by_propname(name,proname)
            infos.append(info)
            print("【%s】%s:%s" % (name, proname, info))
        return infos


if __name__ == '__main__':
    w = Wmi_process()
    print(w.process_names())
    print(w.propnames('services.exe'))
    w.process_infos('services.exe')
