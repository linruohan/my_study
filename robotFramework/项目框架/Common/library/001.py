import os,datetime
base = 'E:\\atom\\robotFramework\\'
s=os.path.join(base, 'logs', datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
os.mkdir(s)

