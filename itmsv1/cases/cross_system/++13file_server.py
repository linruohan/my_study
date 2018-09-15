#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,sys,io,string
'''****************************************'''
'''****************************************'''
'''***********【文件服务器模块】*************'''
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
        # self.driver.set_page_load_timeout(20)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.key1=u"测试文件服务器001"#服务器名称--添加和删除设备名称
        self.key2=u'测试文件服务器002'
        self.ip='192.169.20.11'
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        # driver.switch_to_window(driver.window_handles[0])
        #进入子模块
        s.findXpath(driver,'//*[@id="13050315032667198043cea8b460eacd"]/a').click()
        #进入content-frame
        driver.switch_to.frame('content-frame')
        time.sleep(2)
    """用例1——添加--------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_add(self):
        """添加服务器"""
        driver=self.driver
        #获取添加前数据数
        num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        print(num0)
        '''************添加*****************'''
        #点击【添加】按钮
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
        # 基本信息
        s.findId(driver,'name').send_keys(self.key1)
        s.findId(driver,'ftpip').send_keys(self.ip)#ip
        s.findId(driver,'ftpport').send_keys('21')#ftport
        s.findId(driver,'httpport').send_keys('8099')#httpport
        s.findId(driver,'ftpuser').send_keys('xiangxun')#user
        s.findId(driver,'dirname').send_keys('ftp')#passwd
        s.findId(driver,'ftppassword').send_keys('88151312')#httpport
        '''**************保存***************'''
        # 点击【保存】按钮
        s.findXpath(driver,'//*[@id="inputForm"]/div[2]/button').click()
        time.sleep(2)

        #获取添加后数据数
        num1_0=s.findXpath(driver,'//*[@id="content_body"]/div[3]/div[2]/div[3]/b[3]')
        driver.execute_script("arguments[0].scrollIntoView();", num1_0)#元素聚焦
        num1=num1_0.text
        #验证添加
        self.assertEqual((int(num0)+1),int(num1),u"添加失败！")
        name=s.findsXpath(driver,'.//*[@id="tbody"]/tr/td[2]')
        names=[i.text for i in name]
        if self.key1 in names:
            print(u'【1】添加成功：successfully added！成功添加一条数据')

    """用例2——删除--------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_del(self):
        """删除服务器"""
        driver=self.driver
        #获取删除前数据数
        num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text

        '''**********删除目标*******************'''
        #搜索目标数据
        s.findId(driver,'name').send_keys(self.key2)
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[1]').click()
        time.sleep(2)
        num1=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        self.assertEqual(int(num1),1,u"目标数据重复或异常！")
        time.sleep(1)
        #点击删除按钮
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[9]/a[3]').click()
        driver.switch_to.alert.accept()
        time.sleep(2)
        '''*****************************'''
        #验证
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[2]').click()
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[1]').click()
        name=s.findsXpath(driver,'.//*[@id="tbody"]/tr/td[2]')
        names=[i.text for i in name]
        num2=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]')
        driver.execute_script("arguments[0].scrollIntoView();", num2)#元素聚焦
        num=num2.text
        self.assertEqual((int(num0)-1),int(num),u"删除文件服务器失败！")

        if self.key1 not in names:
            print(u'【2】刪除成功：successfully deleted！成功删除一条数据')
        else:
            print(u'【2】删除失败！')

    """用例3——查询------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_bigsearch(self):
        """查询服务器"""
        driver=self.driver
        #获取删除前数据数
        num0=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        # 输入查询条件
        s.findId(driver,'name').send_keys(self.key1)
        s.findId(driver,'ftpip').send_keys(self.ip)
        s.findId(driver,'ftpport').send_keys('21')
        s.findId(driver,'ftpuser').send_keys('xiangxun')
        time.sleep(2)
        #点击查询
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[1]').click()
        time.sleep(1)
        num1=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        self.assertEqual(int(num1),1,u"目标数据重复或异常！")
        time.sleep(1)
        #查询结果验证
        name=s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[2]').text
        if self.key1 == name:
            print(u'设备名称'+':'+name)
            print(u'【3】查询成功：successfully got the goal！')
        if int(num1)==0:
            print(u'【3】查询结果为空！')

        #重置——查询
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[2]').click()
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[1]').click()
        time.sleep(2)
        kong=s.findXpath(driver,'//*[@id="name"]').text
        num2=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        if kong=='' and num2>num1:
            print(u'重置成功！')
            print(u'共有'+num2+'条数据')
        else:
            print(u'重置失败！')

    """用例4——查看------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_check(self):
        """查看服务器"""
        driver=self.driver
        '''**********查看第一行*******************'''
        #搜索目标数据
        s.findId(driver,'name').send_keys(self.key1)
        s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[1]/form/table/tbody/tr/td[9]/input[1]').click()
        time.sleep(2)
        num1=s.findXpath(driver,'//*[@id="content_body"]/div[2]/div[2]/div[3]/b[3]').text
        self.assertEqual(int(num1),1,u"目标数据重复或异常！")
        name=s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[2]').text
        if self.key1 == name:
            print(u'设备名称'+':'+name)
            print(u'开始查看该设备')
        # 查看
        s.findXpath(driver,'//*[@id="tbody"]/tr[1]/td[9]/a[1]').click()
        time.sleep(2)
        name1=s.findXpath(driver,'//*[@id="content_body"]/div/div[1]/table/tbody/tr[1]/td[2]').text
        self.assertEqual(name,name1,'查看设备名称不匹配')
        s.jietu(driver)
        print(u'【4】查看成功！successfully checking it！')


    """用例5——修改--------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_dataupdate(self):
        """修改服务器"""
        driver=self.driver
        '''**********修改目标*******************'''
        #获取目标
        name0=s.findsXpath(driver,'//*[@id="tbody"]/tr/td[2]')
        name=[i.text for i in name0]
        for i in name:
            if i==self.key1:
                index=name.index(i)+1
            if self.key1 not in name:
                print(u'不存在该名称'+self.key11)

        #开始修改
        s.findXpath(driver,'//*[@id="tbody"]/tr['+str(index)+']/td[9]/a[2]').click()
        dname=s.findXpath(driver,'//*[@id="name"]')
        dname.clear()
        dname.send_keys(self.key2)
        #修改完保存
        s.findXpath(driver,'//*[@id="inputForm"]/div[2]/button').click()
        time.sleep(2)

        #驗證修改
        name1=s.findsXpath(driver,'//*[@id="tbody"]/tr/td[2]')
        text=[i.text for i in name1]
        if self.key2 in text:
            print(u'自定義分組名稱【'+self.key1+'】改爲:'+self.key2)
            print(u'【3】修改成功！successfully reset the data')
        else:
            print(u'sorry，修改失敗！')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
