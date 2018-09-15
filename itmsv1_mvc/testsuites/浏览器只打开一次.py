# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest,time
from itmsv1_mvc.common import find01
s=find01
class BolgHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        base_url = "http://193.169.100.249:8086/itmsld/"
        cls.driver.get(base_url)
        cls.driver.maximize_window()
        s.findId(cls.driver, 'username').clear()
        s.findId(cls.driver, 'password').clear()
        s.findId(cls.driver, 'username').send_keys('admin')
        s.findId(cls.driver, 'password').send_keys('admin')
        s.findXpath(cls.driver, '//input[@value="登 录"]').submit()
        time.sleep(2)
    def setUp(self):
        print('每个用例【开始】都执行一次')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def tearDown(self):
        driver=self.driver
        driver.switch_to.default_content()
        s.findXpath(driver,'//*[@id="main-interface"]/a').click()
        time.sleep(2)
        print('每个用例【结束】都执行一次')

    def test_01(self):
        #进入卡口系统
        driver = self.driver
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        #设备管理——卡口设备——添加
        s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
        # driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findId(driver,'tree-rec_1_span').click()
        print('testcase1')

    def test_02(self):
        driver = self.driver
        s.findId(driver, 'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        # 设备管理——卡口设备——添加
        s.findXpath(driver, '//*[@id="130502094519328f815bc3af1d635903"]/a').click()
        # driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findId(driver, 'tree-rec_5_a').click()
        driver.switch_to.frame('myIframe')
        number0 = s.findXpath(driver, '//div[@class="page_info"]/b[3]').text
        print(number0)

        print('testcase2')

if __name__ == "__main__":
    unittest.main()