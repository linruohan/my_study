#coding=utf-8

import  os
from appium import webdriver
# 获取当前目录的根路径
apk_path=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
print(apk_path)


desired_caps ={}
desired_caps['platformName'] = 'Android' #设备系统
desired_caps['platformVersion'] = '5.1.1' #设备系统版本
desired_caps['deviceName'] = 'SCL-AL00' #设备名称

# 测试包的路径
desired_caps['app']=apk_path+'\\app\\baidu.apk'
# 不需要每次都安装apk
desired_caps['noReset'] = True
# 应用程序的包名
# desired_caps['appPackage']='com.baidu.searchbox'
# desired_caps['appActivity']='com.baidu.searchbox.SplashActivity'
#如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之

driver=webdriver.Remote('http://193.169.100.238:4723/wd/hub',desired_caps)#启动app

print('已经打开app。。。')

