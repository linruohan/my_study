#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out
s=find

class WeifaSystem(unittest.TestCase):
    def setUp(self):
        self.driver = login_in_out.login()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
    #用例1
    def test_denglu(self):
        """平台搜索"""
        driver=self.driver
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        login_in_out.quit(driver)
    #用例2
    def test_baidu_set(self):
        """卡口"""
        driver=self.driver
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        s.findId(driver,'130502094519328f815bc3af1d635903').click()
        login_in_out.quit(driver)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
