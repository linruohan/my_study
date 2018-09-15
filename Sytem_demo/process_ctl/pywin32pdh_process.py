import psutil,sys
import win32pdh, string, win32api
import win32com.client,wmi

class Use_win32pdh:
    def __init__(self):
        for name,id in self.procids():
            print("【%s】<<<... %s ....>>>"%(name,id))
    def procids(self):
        # each instance is a process, you can have multiple processes w/same name
        junk, instances = win32pdh.EnumObjectItems(None, None, 'process', win32pdh.PERF_DETAIL_WIZARD)
        proc_ids = []
        proc_dict = {}
        for instance in instances:
            if instance in proc_dict:
                proc_dict[instance] = proc_dict[instance] + 1
            else:
                proc_dict[instance] = 0
        for instance, max_instances in proc_dict.items():
            for inum in range(max_instances + 1):
                hq = win32pdh.OpenQuery()  # initializes the query handle
                path = win32pdh.MakeCounterPath((None, 'process', instance, None, inum, 'ID Process'))
                counter_handle = win32pdh.AddCounter(hq, path)
                win32pdh.CollectQueryData(hq)  # collects data for the counter
                type, val = win32pdh.GetFormattedCounterValue(counter_handle, win32pdh.PDH_FMT_LONG)
                proc_ids.append((instance, str(val)))
                win32pdh.CloseQuery(hq)

        proc_ids.sort()
        return proc_ids


if __name__ == '__main__':
    s1=Use_win32pdh()
