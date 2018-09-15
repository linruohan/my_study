# coding=utf-8
from selenium.webdriver.support.ui import Select
import unittest, time

'''****************************************'''
'''****************************************'''
'''***********卡口设备模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
from itmsv1_mvc.common import find01, sj_3, sj_12str, sj_hz, sj_IP

s = find01
from selenium import webdriver

driver = webdriver.Chrome ()
driver.maximize_window()
driver.get ('http://193.169.100.249:8086/itmsld/login')
s.findId (driver, 'username').clear ()
s.findId (driver, 'password').clear ()
s.findId (driver, 'username').send_keys ('admin')
s.findId (driver, 'password').send_keys ('admin')
s.findXpath (driver, '//input[@value="登 录"]').submit ()
time.sleep (2)
# 进入卡口系统
s.findId (driver, 'menu_130619095023993fa6f0e33461840c4b').click ()
time.sleep (2)
# 设备管理——卡口设备
s.findXpath (driver, '//*[@id="130904154952125082d5a9e45d9061e1"]/a').click ()
# driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
driver.switch_to.frame ('content-frame')
time.sleep (2)
s.findXpath (driver, '//*[@id="content_body"]/div[3]/div[2]/div[1]/div[1]/button[1]').click ()
time.sleep(1)
s.findId(driver,'platenum').send_keys('陕CJ7216')
#号牌颜色
s.findXpath(driver,'//*[@id="plateColorCode_chzn"]/a/span').click()
time.sleep(1)
s.findXpath(driver,'//*[@id="plateColorCode_chzn_o_3"]').click()
time.sleep(2)
#号牌类型
s.findXpath(driver,'//*[@id="inputForm"]/div/table/tbody/tr[2]/td[4]/div/a/span').click()
time.sleep(1)
s.findXpath(driver,'//*[@id="inputForm"]/div/table/tbody/tr[2]/td[4]/div/div/ul/li[3]').click()
