#coding=utf-8

import os
import time
from appium import webdriver

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径

desired_caps = {'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': 'SCL-AL00',
                'noReset': True,
                'appPackage': 'com.baidu.searchbox',
                'appActivity': 'com.baidu.searchbox.SplashActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
                }

driver = webdriver.Remote('http://193.169.100.238:4723/wd/hub', desired_caps)  # 启动app
time.sleep(13)  # app启动后等待3秒，方便元素加载完成





time.sleep(3) #app启动后等待3秒，方便元素加载完成
# 打印屏幕高和宽
print(driver.get_window_size())
#获取屏幕的高
x = driver.get_window_size()['width']
# 获取屏幕宽
y = driver.get_window_size()['height']
# 滑屏，大概从屏幕右边2分之一高度，往左侧滑动,滑动后显示的是 热点tab
driver.swipe(6/7*x, 1/2*y, 1/7*x, 1/2*y, 100)
time.sleep(4)
#向右滑动，显示推荐tab 内容，第五个参数，时间设置大一点，否则容易看不到滑动效果
driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 200)
time.sleep(4)
#向上滑
driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/7*y, 200)
time.sleep(4)
# 向下滑动
driver.swipe(1/2*x, 1/7*y, 1/2*x, 6/7*y, 200)