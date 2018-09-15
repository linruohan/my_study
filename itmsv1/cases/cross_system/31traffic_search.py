#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
'''****************************************'''
'''****************************************'''
'''***********【通行车辆查询】模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find

class Traffic_search(unittest.TestCase):
    def setUp(self):
        self.driver = login_in_out.login()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.key=''
        #进入卡口系统
        driver=self.driver
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
            #进入子模块
        s.findXpath(driver,'//*[@id="131120162537187b91202c6b3a1ee2b8"]/a').click()
            #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)


    """用例1——查询------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_bigsearch(self):
        """查询"""
        driver=self.driver
        s.findId(driver,'plateNumber').send_keys()
        select=s.findId(driver,'carPlateColorCode')
        select.select_by_value('2')#[0白1黄2蓝3黑4其他]

        select_cd=s.findId(driver,'laneCode')
        select_cd.select_by_value('2')#  【第n车道】

    """用例2——查看------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_check(self):
        """查看目标"""
        driver=self.driver

    """用例3——翻页------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_dataupdate(self):
        """翻转页面"""
        driver=self.driver


    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
        unittest.main()
