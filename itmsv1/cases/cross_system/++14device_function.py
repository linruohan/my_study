#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
from selenium.webdriver.common.action_chains import ActionChains
'''****************************************'''
'''****************************************'''
'''***********【设备功能】模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find

class Device_function(unittest.TestCase):
    def setUp(self):
        self.driver = login_in_out.login()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        #进入卡口系统
        driver=self.driver
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
            #进入子模块
        s.findXpath(driver,'//*[@id="13050614093381218f13d4006428bc9e"]/a').click()
            #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        self.key1=u'设备功能零零幺'
        self.key2=u'设备功能零零贰'
        folders=s.findsClassName(driver,'ico_close')
        for i in folders:
            ActionChains(driver).double_click(i).perform()
            time.sleep(2)
    """用例1——添加--------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_add(self):
        """添加"""
        driver=self.driver
        sname=s.findsTagName(driver,'span')
        snames=[i.get_attribute('textContent') for i in sname]
        if self.key1 not in snames:
            s.findId(driver,'tree-org_3_span').click()
            s.findXpath(driver,'//*[@id="content_body"]/div[3]/div/div[1]/div[1]/button[1]').click()
            driver.switch_to.frame('myIframe')
            s.findId(driver,'devicetype-name').send_keys(self.key1)
            s.findClassName(driver,'mar_r10').click()
        else:
            s.findXpath(driver,'//*[@id="cancel_btn"]').click()
            print(u'【1】添加失败！该数据已存在！')

        # 验证
            # 展开文件夹
        driver.switch_to.default_content()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        folders=s.findsClassName(driver,'ico_close')
        for i in folders:
            ActionChains(driver).double_click(i).perform()
            time.sleep(2)
            # 获取名称name
        sname=s.findsTagName(driver,'span')
        snames=[i.get_attribute('textContent') for i in sname]
        if self.key1 in snames:
            print(u'【1】添加成功！')
        else:
            print(u'【1】添加失败！')


    """用例2——查看------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_check(self):
        """查看目标"""
        driver=self.driver
        sname=s.findsTagName(driver,'span')
        for i in sname:
            print(i.get_attribute('textContent'))
        s.jietu(driver)
        print(u'【2】查看成功！')

    """用例3——修改------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_dataupdate(self):
        """修改目标"""
        driver=self.driver
        sname=s.findsTagName(driver,'span')
        snames=[i.get_attribute('textContent') for i in sname]

        if self.key1 in snames and self.key2 not in snames:
            sname[snames.index(self.key1)].click()
            s.findXpath(driver,'//*[@id="content_body"]/div[3]/div/div[1]/div[1]/button[2]').click()
            time.sleep(2)
            driver.switch_to.frame('myIframe')
            time.sleep(2)
            name=s.findId(driver,'deviceTypeInfo-name')
            if name.get_attribute('value')==self.key1:
                name.clear()
                name.send_keys(self.key2)
                s.findXpath(driver,'//*[@id="inputForm"]/div[2]/input[1]').click()
                time.sleep(3)
            else:
                s.findXpath(driver,'//*[@id="cancel_btn"]').click()
        else:
            print(u'设备名已存在，请检查！')

        # 验证
        driver.switch_to.default_content()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        folders=s.findsClassName(driver,'ico_close')
        for i in folders:
            ActionChains(driver).double_click(i).perform()
            time.sleep(2)
        sname1=s.findsTagName(driver,'span')
        snames1=[i.get_attribute('textContent') for i in sname1]
        if self.key2 not in snames and self.key2 in snames1:
            print(u'【3】修改成功！')
        else:
            print(u'【3】修改失败！')


    """用例4——删除------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_del(self):
        """删除目标"""
        driver=self.driver
        sname=s.findsTagName(driver,'span')
        snames=[i.get_attribute('textContent') for i in sname]
        if self.key2 in snames :
            sname[snames.index(self.key2)].click()
            s.findXpath(driver,'//*[@id="content_body"]/div[3]/div/div[1]/div[1]/button[3]').click()
            driver.switch_to.alert.accept()
            time.sleep(2)
        # 验证
        driver.switch_to.default_content()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        folders=s.findsClassName(driver,'ico_close')
        for i in folders:
            ActionChains(driver).double_click(i).perform()
            time.sleep(2)
        sname1=s.findsTagName(driver,'span')
        snames1=[i.get_attribute('textContent') for i in sname1]
        if self.key2 not in snames1 :
            print(u'【4】删除成功！')
        else:
            print(u'【4】删除失败！')


    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
        unittest.main()
