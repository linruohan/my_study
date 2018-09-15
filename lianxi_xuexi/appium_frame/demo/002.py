#coding=utf-8
import time
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
desired_caps['appPackage']='com.baidu.searchbox'
desired_caps['appActivity']='com.baidu.searchbox.SplashActivity'
#如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之

driver=webdriver.Remote('http://193.169.100.238:8888/wd/hub',desired_caps)#启动app

print('已经打开app。。。')
time.sleep(15)
# 根据元素id来定位
# driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').click()

# 根据元素id来定位
# 点击“热点”频道
#hot = driver.find_element_by_id('com.baidu.searchbox:id/tab_indi_title')
hot = driver.find_element_by_android_uiautomator("text(\"热点\")")
hot.click()
# 点击“推荐”频道
rec = driver.find_element_by_android_uiautomator("text(\"推荐\")")
rec.click()

# 根据元素class 来定位
# 点击“输入框”
# searchBox = driver.find_element_by_class_name('android.widget.Button')
# searchBox.click()
time.sleep(12)


'''   这样来回切换点击是运行不成功，
如果每次只点击一个，发现点击麦克风的index是1，
但是ui automator viewer给出的是index是2，
这个地方是有问题的。'''

# 点击“我的”
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='4']").click()
time.sleep(2)
# 点击“默认主页“
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='0']").click()
time.sleep(2)
# 点击““视频
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='1']").click()
time.sleep(2)
# 点击“我的关注“
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='3']").click()
time.sleep(2)
# 点击“麦克风“
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='2']").click()
time.sleep(2)

# 点击“我的”
# my_home = driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][5]").click()
time.sleep(2)






driver.quit()



