#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,sys,io
import sys
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import find
s=find
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.maximize_window()
base_url = "http://193.169.100.201:8080/itmsv2mdj"
driver.get(base_url)
s.findId(driver,'username').clear()
s.findId(driver,'password').clear()
s.findId(driver,'username').send_keys('admin')
s.findId(driver,'password').send_keys('admin')
s.findXpath(driver,'//input[@value="登 录"]').submit()
time.sleep(1)


s.findXpath(driver,'//*[@id="menu_1808211049161578859fd8eb44194fc8"]/p/a').click()
time.sleep(1)
s.findXpath(driver,'//*[@id="180821110113086ab3d15afb8b14fde2"]/a').click()
time.sleep(1)
driver.switch_to.frame('content-frame')
# time.sleep(2)
# s.findId(driver,'plateNumber').send_keys("")
# js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"  # 1.原生js，移除属性
# js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
# js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
# js = "$('input[id=beginDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
# js1 = "$('input[id=beginDate]').attr('readonly','')"

js = 'document.getElementById("beginDate").removeAttribute("readonly");'
driver.execute_script(js)
s.findId(driver,'beginDate').send_keys('2018-09-14 08:00:00')
time.sleep(1)
js1 = "document.getElementById('endDate').removeAttribute('readonly')"
driver.execute_script(js1)
s.findId(driver,"endDate").send_keys('2018-09-14 08:10:00')
time.sleep(2)

s.findXpath(driver,'//*[@id="searchForm"]/table/tbody/tr[4]/td[3]/input[1]').click()


