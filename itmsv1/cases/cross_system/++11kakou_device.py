#coding=utf-8
from selenium.webdriver.support.ui import Select
import unittest,time
'''****************************************'''
'''****************************************'''
'''***********卡口设备模块*************'''
'''**************（测试）**********************'''
'''****************************************'''
from itmsv1.unit import find,login_in_out,sj_3,sj_8str,sj_hz,sj_IP
s=find

class KakouSystem(unittest.TestCase):
    def equal(self, first, second, msg=None):
        # self._write_to_log()
        super(KakouSystem, self).assertEqual(first, second, msg)

    def setUp(cls):
        cls.driver = login_in_out.login()
        cls.driver.implicitly_wait(10)
        cls.verificationErrors = []
        cls.accept_next_alert = True
        super()
    """用例1——添加设备【卡口系统】-【设备管理】-【卡口设备】------------------------------------------"""
    # @unittest.skip('暂时跳过')
    def test_add_device(self):
        """添加卡口设备"""
        driver=self.driver
        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        #设备管理——卡口设备
        s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
        # driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findId(driver,'tree-rec_5_a').click()

        # driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findClassName(driver,'icon-plus').click()
        driver.switch_to.frame('myIframe')
        time.sleep(2)
        # driver.switch_to.frame('myIframe')
        # number0=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
        # driver.switch_to.default_content()
        #基本信息
        js = 'document.getElementById("orgNames").removeAttribute("readonly");'
        driver.execute_script(js)
        s.findId(driver,'orgNames').click()
        time.sleep(1)
        s.findXpath(driver,'//*[@id="orgTreeSpace_2_span"]').click()
        s.findXpath(driver,'//*[@id="tab1"]/div[1]/table/tbody/tr[3]/td[2]/div/button').click()
        s.findXpath(driver,'//*[@id="dropdown-ul"]/li[1]').click()
        s.findId(driver,'name').send_keys(sj_hz.s())
        time.sleep(2)
        s.findId(driver,'deviceTypeNames').click()
        time.sleep(2)
        s.findId(driver,'dtTreeSpace_2_span').click()
        s.findId(driver,'pattern').send_keys(sj_8str.s())
        #环境配置
        s.findXpath(driver,'//*[@id="inputForm"]/ul/li[2]/a').click()
        time.sleep(2)
        s.findId(driver,'ip').send_keys(sj_IP.s())
        s.findId(driver,'timeout').send_keys(sj_3.s())
        #方向配置
        time.sleep(2)
        s.findXpath(driver,'//*[@id="inputForm"]/ul/li[3]/a').click()
        s.findCss(driver,'#directionCode_01').click()
        time.sleep(2)
        #建设信息
        s.findXpath(driver,'//*[@id="inputForm"]/ul/li[4]/a').click()
        s.findXpath(driver,'//*[@id="companyId_chzn"]/a/span').click()
        s.findId(driver,'companyId_chzn_o_2').click()
        time.sleep(2)

        #保存
        confire=s.findId(driver,'submit_btn')
        driver.execute_script("arguments[0].scrollIntoView();", confire)#元素聚焦
        confire.click()
        time.sleep(2)

        #验证长安路设备数量
        # number1=s.findCss(driver,'#content_body > div > div > div.page_info > b:nth-child(3)').text
        # self.equal((int(number0)+1),int(number1),u"添加卡口设备失败！")
        # if int(number1)-int(number0)==1:
        #     print(number1+'-'+number0+'=1')
        #     print(u'successfully added！成功添加一条数据')
        # else:
        #     print(u'sorry，添加失败')

    """用例2——查看卡口设备信息【卡口系统】-【设备管理】-【卡口设备】------------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_check_device(self):
        """查看卡口设备"""
        driver=self.driver

        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        #设备管理——卡口设备——查看
        s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
        # driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findId(driver,'tree-rec_5_a').click()
        driver.switch_to.frame('myIframe')

        key=u'立毛叹元口'
        knames=s.findsXpath(driver,'//tbody[@id="tbody"]/tr/td[2]')
        kname=[kname.text for kname in knames]
        kindex=[kname.index(i) for i in kname if key in i]
        s.findXpath(driver,("//*[@id='rowcount"+str(kindex[0])+"']/td[9]/a[1]")).click()
        print(u'设备信息查看成功！')

    """用例3——删除卡口设备信息【卡口系统】-【设备管理】-【卡口设备】-------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_del_device(self):
        """删除卡口设备"""
        driver=self.driver

        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        #设备管理——卡口设备——添加
        s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
        # driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findId(driver,'tree-rec_5_a').click()
        driver.switch_to.frame('myIframe')
        number0=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
        print(number0)

        #找到名称为key的卡口设备并删除
        key=u'奶瓜太斥无'
        knames=s.findsXpath(driver,'//tbody[@id="tbody"]/tr/td[2]')
        kname=[kname.text for kname in knames]
        kindex=[kname.index(i) for i in kname if key in i]
        s.findXpath(driver,("//*[@id='rowcount"+str(kindex[0])+"']/td[9]/a[3]")).click()

        #点击确认删除alert
        del_alert=driver.switch_to_alert()
        print(del_alert.text)
        del_alert.accept()
        # del_alert.dismiss()#取消删除
        #验证长安路设备数量
        time.sleep(3)
        number1=s.findCss(driver,'#content_body > div > div > div.page_info > b:nth-child(3)').text
        print("number1="+number1)
        if int(number0)-int(number1)==1:
            print(number0+'-'+number1+'=1')
            s.jietu(driver)
            print(u'successfully added！成功删除一条数据')
        else:
            print(u'sorry，删除失败')

        print(u'设备信息删除成功！')
    """用例4——查询卡口设备信息【卡口系统】-【设备管理】-【卡口设备】-------------------------------------"""
    @unittest.skip('暂时跳过')
    def test_search_device(self):
        """查询卡口设备"""
        driver=self.driver

        #进入卡口系统
        s.findId(driver,'menu_1304261304150253833622fa401af96b').click()
        time.sleep(2)
        #设备管理——卡口设备——添加
        s.findXpath(driver,'//*[@id="130502094519328f815bc3af1d635903"]/a').click()
        # driver.execute_script("window.scrollBy(0,120)","")#向下滚动200px
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findId(driver,'tree-rec_1_span').click()
        #输入查询条件
        name='县城二环设备'
        s.findXpath(driver,'//*[@id="s_name"]').send_keys(name)
        s.findXpath(driver,'//*[@id="s_code"]').send_keys('522728000001011013')
        Select(s.findId(driver,"dev-select")).select_by_value('1708021631148488b93e')
        """
        <option value="1708021631148488b93e">西安详讯</option>
        <option value="170803143742659d109f">银江股份</option>
        <option value="17092009274439868d31">西安详讯</option>
        <option value="170803143721033f3a29">海康威视</option>
        """
        Select(s.findId(driver,"selXSF")).select_by_value('01')
        '''
        <option value="01">闯红灯</option>
        <option value="02">公路卡口设备</option>
        <option value="03">测速设备</option>
        <option value="04">闭路电视</option>
        <option value="05">移动摄像</option>
        <option value="06">警务通</option>
        <option value="07">区间测速</option>
        <option value="08">卫星定位装置</option>
        <option value="09">其它电子设备</option>
        '''
        s.findXpath(driver,'//*[@id="deviceTypeNames"]').click()
        s.findXpath(driver,'//*[@id="dtTreeSpace_2_span"]').click()
        s.findXpath(driver,'//*[@id="dtTreeSpace_5_check"]').click()
        time.sleep(2)
        s.findXpath(driver,'//*[@id="orgNames"]').click()
        s.findXpath(driver,'//*[@id="orgTreeSpace_4_span"]').click()
        time.sleep(2)
        s.findXpath(driver,'//*[@id="s_ip"]').send_keys('192.25.54.6')

        #開始查詢
        s.findXpath(driver,'//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[1]').click()
        time.sleep(2)

        driver.switch_to.frame('myIframe')
        number0=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
        print(u'查詢結果：一共有'+number0+'條卡口數據')
        dname=s.findXpath(driver,'//*[@id="rowcount0"]/td[2]').text
        if name==dname:
            print(u'查詢成功！')
        else:
            print(u'查詢失敗')
        #重置查詢
        driver.switch_to.default_content()
        driver.switch_to.frame('content-frame')
        time.sleep(2)
        s.findXpath(driver,'//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[2]').click()
        s.findXpath(driver,'//*[@id="content_body"]/div[4]/div[1]/form/table/tbody/tr[2]/td[8]/input[1]').click()
        time.sleep(2)
        driver.switch_to.frame('myIframe')
        number1=s.findXpath(driver,'//div[@class="page_info"]/b[3]').text
        print(u'重置後，一共有'+number1+'條卡口數據')


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
