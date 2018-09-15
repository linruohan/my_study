#coding=utf-8







import os
import time
from appium import webdriver

desired_caps = {'platformName': 'Android',
                'platformVersion': '6.0.1',
                'deviceName': 'KIW-AL10',
                'noReset': True,
                'appPackage': 'com.baidu.searchbox',
                'appActivity': 'com.baidu.searchbox.SplashActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
time.sleep(3)  # app启动后等待3秒，方便元素加载完成
# 模拟手指点击操作
driver.tap([(918, 413), (1026, 521)], 100)
# 解释：上面tap方法中位置的元素点坐标是通过ui
# automator
# viewer获取，持续时间100是指100毫秒。