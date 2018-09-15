# 解决方案
# 方法一：每次运行后，手动关闭chromedriver.exe或者IEDriverServer.exe；
# 方法二：将下面代码保存为批处理，每次运行后手动运行一下:
# taskkill /f /im  chromedriver.exe
# taskkill /f /im  IEDriverServer.exe
# 方法三：封装成keywords
# step1:
import os

def close_driver( self,process_name):

    """Close a process by process name."""
    if process_name[-4:].lower () != ".exe":
        if process_name.split ('driver')[1] == '':
            process_name += "driver.exe"
        process_name += ".exe"
    os.system ("taskkill /f /im " + process_name)
