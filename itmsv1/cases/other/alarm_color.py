#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find
driver=login_in_out.login()
#进入卡口系统
s.findXpath(driver,'//*[@id="menu_1304261304150253833622fa401af96b"]/a').click()
s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
time.sleep(2)
#进入卡口系统-实时监控-报警颜色
s.findXpath(driver,'//*[@id="131128083220030196117fcf823f3758"]/a').click()
s.jietu(driver)
#选择颜色——保存
"""

"""









driver.quit()
