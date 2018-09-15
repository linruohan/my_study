#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
'''****************************************'''
'''****************************************'''
'''***********自定义分组模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
sys.path.append('E:\\atom\\Python\\itmsv1\\unit')
import find,login_in_out,sj_IP,sj_8str,sj_hz,sj_3
s=find

class Custom_grouping(unittest.TestCase):
    def setUp(self):
        self.driver = login_in_out.login()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        super()
    """用例1——添加自定义分组【卡口系统】-【设备管理】-【自定义分组】------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_add_device(self):
        """添加自定义分组"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        #获取添加前数据数
        num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        s.findCss(driver,'#content_body > div.conten_box > div.table_box > div.btn-group-wrap.mar_b5 > div.btn-group.pull-right > button:nth-child(1)').click()
        key=sj_hz.s()#自定义分组名称
        s.findId(driver,'name').send_keys(key)
        s.findXpath(driver,'//*[@id="inputForm"]/div[2]/button').click()
        time.sleep(5)

        #获取添加后数据数
        num1_0=s.findXpath(driver,'//*[@id="content_body"]/div[3]/div[2]/div[3]/b[3]')
        driver.execute_script("arguments[0].scrollIntoView();", num1_0)#元素聚焦
        num1=num1_0.text
        #验证
        self.assertEqual((int(num0)+1),int(num1),u"添加卡口设备失败！")
        print(u'【1】添加成功：successfully added！成功添加一条数据')


    """用例2——删除自定义分组【卡口系统】-【设备管理】-【自定义分组】------------------------------------------"""
    # @unittest.skip('暂时跳过用例2的测试')
    def test_del_device(self):
        """删除自定义分组"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        #获取删除前数据数
        num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        print(num0)
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[3]/a[3]').click()
        driver.switch_to.alert.accept()

        time.sleep(3)
        #验证
        num1_0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]')
        driver.execute_script("arguments[0].scrollIntoView();", num1_0)#元素聚焦
        num1=num1_0.text
        print(num1)
        #验证
        self.assertEqual((int(num0)-1),int(num1),u"删除卡口设备失败！")
        print(u'【2】刪除成功：successfully deleted！成功删除一条数据')


    """用例3——修改自定义分组【卡口系统】-【设备管理】-【自定义分组】------------------------------------------"""
    # @unittest.skip('暂时跳过用例3的测试')
    def test_update_device(self):
        """修改自定义分组"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        name0=s.findXpath(driver,'//*[@id="tbody"]/tr[2]/td[2]').text
        s.findXpath(driver,'//*[@id="tbody"]/tr[2]/td[3]/a[2]').click()
        name=s.findXpath(driver,'//*[@id="name"]')
        name.clear()
        key=sj_hz.s()
        name.send_keys(key)
        s.findXpath(driver,'//*[@id="inputForm"]/div[2]/button').click()
        time.sleep(2)

        #驗證修改
        name1=s.findsXpath(driver,'//*[@id="tbody"]/tr/td[2]')
        text=[i.text for i in name1]
        # print(text)
        if key in text:
            print(u'自定義分組名稱【'+name0+'】改爲:'+key)
            print(u'【3】修改成功！successfully reset the data')
        else:
            print(u'sorry，修改失敗！')

    """用例4——查看自定义分组【卡口系统】-【设备管理】-【自定义分组】------------------------------------------"""
    # @unittest.skip('暂时跳过用例3的测试')
    def test_check_device(self):
        """查看自定义分组"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[3]/a[1]').click()
        s.jietu(driver)
        print(u'【4】查看成功！successfully checking it！')


    """用例5——分配设备-自定义分组【卡口系统】-【设备管理】-【自定义分组】------------------------------------------"""
    # @unittest.skip('暂时跳过用例3的测试')
    def test_give_device(self):
        """分配设备-自定义分组"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[3]/a[4]').click()

        driver.switch_to.default_content()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        sb=s.findsCss(driver,'.sort_device_list>li>input')
        for i in sb:
            i.click()
        # 保存
        bc=s.findXpath(driver,'//*[@id="submit_btn"]')
        driver.execute_script("arguments[0].scrollIntoView();", bc)#元素聚焦
        bc.click()
        time.sleep(3)
        #驗證
        driver.switch_to.default_content()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        ck=s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[3]/a[1]')
        driver.execute_script("arguments[0].scrollIntoView();", ck)#元素聚焦
        ck.click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0,0)")
        n=s.findsXpath(driver,'//*[@id="content_body"]/div/div[2]/table/tbody/tr/td')
        print(u'設備分配爲如下所示：')
        for i in n:
            print(i.text)
        print('【5】設備分配成功：successfully given devices！')


    """用例6——查询设备-自定义分组【卡口系统】-【设备管理】-【自定义分组】------------------------------------------"""
    # @unittest.skip('暂时跳过用例3的测试')
    def test_search_device(self):
        """查询设备-自定义分组"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="1404161355392917afeff9583374f9a1"]/a').click()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        # 开始查询
        key='亿'
        s.findXpath(driver,'//*[@id="name"]').send_keys(key)
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[3]/input[1]').click()
        #查询结果
        num=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        name=s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[2]').text
        if key in name:
            print(key+':'+name)
            print(u'查询成功：successfully got the goal！')
        if int(num)==0:
            print(u'查询结果为空！')
        #重置
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[3]/input[2]').click()
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[3]/input[1]').click()
        time.sleep(2)
        kong=s.findXpath(driver,'//*[@id="name"]').text
        summery=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        if kong=='':
            print(u'重置成功！')
            print(u'共有'+summery+'条数据')
        else:
            print(u'重置失败！')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
