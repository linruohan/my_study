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

# 截图
img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_save_path = img_folder + time + '.png'
driver.get_screenshot_as_file(screen_save_path)
# 运行一下，刷新screenshots文件夹，发现了以时间戳的一个png图片，打开是手机百度首页内容。