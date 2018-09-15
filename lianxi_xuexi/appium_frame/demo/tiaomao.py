
import os
import time
from appium import webdriver

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径  

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '6.0.1'  # 设备系统版本
desired_caps['deviceName'] = 'KIW-AL10'  # 设备名称

# 测试apk包的路径  
desired_caps['app'] = apk_path + '\\app\\shoujibaidu.apk'
# 不需要每次都安装apk  
desired_caps['noReset'] = True
# 应用程序的包名  
desired_caps['appPackage'] = 'com.tmall.wireless'
desired_caps['appActivity'] = 'com.tmall.wireless.splash.TMSplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
time.sleep(3)  # app启动后等待3秒，方便元素加载完成
# 根据元素 content-desc来定位  
# 点击“天猫超市”  
driver.find_element_by_accessibility_id("天猫超市").click()