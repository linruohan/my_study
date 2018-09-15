#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
'''****************************************'''
'''****************************************'''
'''***********【   】模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find

class File_server(unittest.TestCase):
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
        s.findXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a').click()
            #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)


    """用例1——添加--------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_add(self):
        """添加"""
        driver=self.driver


    """用例2——查询------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_bigsearch(self):
        """查询"""
        driver=self.driver

    """用例3——查看------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_check(self):
        """查看目标"""
        driver=self.driver

    """用例4——修改------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_dataupdate(self):
        """修改目标"""
        driver=self.driver

    """用例5——删除------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_del(self):
        """删除目标"""
        driver=self.driver



    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
        unittest.main()
