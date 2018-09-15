import numpy as np
import pandas as pd
import time_utils
import hbase_utils
device_id =""
start_time = time_utils.string_to_timestamp("2018-06-29_04-00-00") * 1000
end_time = time_utils.string_to_timestamp("2018-06-29_07-00-00") * 1000
hbase = hbase_utils.HbaseUtil()
row_start = hbase.get_row_key(device_id, start_time)
row_stop = hbase.get_row_key(device_id, end_time)
result = hbase.scan_table("bigdata:tb_run_data", row_start=row_start,
                          row_stop=row_stop, include_timestamp=False)
result_ = []
for i in result:
    result_.append(i)
cols = ["cf:DeviceId", "cf:DataTime", "cf:ALinkStatus", "cf:AHasAnybody", "cf:AHeartRate","cf:ABreathRate",
        "cf:AActivityEnergy", "cf:ATurnOverTimes"]
# 取出十分钟数据中最后300条数据
# print result
pd_clos = ["DeviceId", "DataTime", "ALinkStatus", "AHasAnybody", "AHeartRate","ABreathRate",
        "AActivityEnergy", "ATurnOverTimes"]
all_data = np.array([[int(row[1][col]) for col in cols] for row in result_])
all_data = pd.DataFrame(all_data, columns=pd_clos)
data_time = []
for i in all_data["DataTime"].values:
    data_time.append(time_utils.timestamp_to_string(i /1000))
all_data["DataTime"] = data_time
all_data = pd.DataFrame(all_data)
all_data.to_csv('D:// '+ str(device_id) + '.csv')