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
# 根据元素xpath来定位  
# 点击“输入框”  
driver.find_element_by_id("com.baidu.searchbox:id/baidu_searchbox").click()
# 输入字段  
searchInputBox = driver.find_element_by_id('com.baidu.searchbox:id/SearchTextInput')
searchInputBox.clear()
searchInputBox.send_keys("Appium")

driver.press_keycode(66) # 点击屏幕键盘的搜索键
time.sleep(1)
#断言：由于手机百度搜索列表页，每个结果都不可以进行元素定位，所以无法通过搜索命中高亮显示来断言。
#这里采用搜索输入框显示的文字是我们输入的字段来简单断言一下
searchEditBoxText = driver.find_element_by_id('com.baidu.searchbox:id/SearchTextInput')
if(searchEditBoxText.text == 'Appium'):
    print("Test pass.")
else:
    print("Test Failed!!")


