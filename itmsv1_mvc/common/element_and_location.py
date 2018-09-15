# coding=utf-8
import os.path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from itmsv1_mvc.common.mylog import Log as log
from PIL import Image
log = log ()


# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Ele_loc (object):
    """
        Page基类，所有page都应该继承该类
    """

    def __init__(self, driver):
        self.driver = driver
    '''***********************   元素定位  --begin-- **************************************'''

    # 定位元素方法
    def find_element(self, selector):
        global element
        if '=>' not in selector:
            return self.driver.find_element_by_id (selector)
        selector_by = selector.split ('=>')[0]
        selector_value = selector.split ('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id (selector_value)
                s=element.tag_name
                log.info ("Had find the element  [ %s ] successful "
                          "by %s via value: %s " % (s, selector_by, selector_value))
            except NoSuchElementException as e:
                log.error ("NoSuchElementException: %s" % e)
                self.get_windows_img ()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name (selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name (selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text (selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text (selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name (selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath (selector_value)
                s = element.tag_name
                log.info ("Had find the element [ %s ] successful "
                          "by %s via value: %s " % (s, selector_by, selector_value))
            except NoSuchElementException as e:
                log.error ("NoSuchElementException: %s" % e)
                self.get_windows_img ()
        elif selector_by == "c" or selector_by == 'css':
            element = self.driver.find_element_by_css_selector (selector_value)
        else:
            raise NameError ("Please enter a valid type of targeting elements.")
        return element

    def find_elements(self,selector):
        global elements
        if '=>' not in selector:
            return self.driver.find_elements_by_id (selector)
        selector_by = selector.split ('=>')[0]
        selector_value = selector.split ('=>')[1]
        if selector_by == "i" or selector_by == 'id':
            try:
                elements = self.driver.find_elements_by_id (selector_value)
                s = element.tag_name
                log.info ("Had find the elements %s successful "
                          "by %s via value: %s " % (s, selector_by, selector_value))
            except NoSuchElementException as e:
                log.error ("NoSuchElementException: %s" % e)
                self.get_windows_img ()
        elif selector_by == "n" or selector_by == 'name':
            elements = self.driver.find_elements_by_name (selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.driver.find_elements_by_class_name (selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.driver.find_elements_by_link_text (selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text (selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.driver.find_elements_by_tag_name (selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath (selector_value)
                s=[kname.text for kname in self.driver.find_elements_by_xpath (selector_value)]
                log.info ("Had find the elements [ %s ] successful "
                          "by %s via value: %s " % (s, selector_by, selector_value))
            except NoSuchElementException as e1:
                log.error ("NoSuchElementException: %s" % e1)
                self.get_windows_img ()
        elif selector_by == "c" or selector_by == 'css':
            elements = self.driver.find_elements_by_css_selector (selector_value)
        else:
            raise NameError ("Please enter a valid type of targeting elements.")
        return elements
    '''*****************************   元素定位  --end--  ********************************************'''
    def js_to_view(self, js1,el):
        self.driver.execute_script (js1,el)
    def js(self, js):
        self.driver.execute_script (js)

    # select下拉框选择
    def select_value(self, selector, value):
        Select (self.find_element (selector)).select_by_value (value)
    def select_index(self, selector, index):
        Select (self.find_element (selector)).select_by_index (index)
    def select_visible_text(self, selector, text):
        Select (self.find_element (selector)).select_by_visible_text (text)

    def is_selected(self, selector):
        e1 = self.find_element (selector)
        if e1.is_selected ():
            return True
        else:
            return False

    # 输入
    def type(self, selector, text):
        e1 = self.presence_of_element_located(selector)
        e1.clear ()
        if e1.text:
            text1 = e1.text
        else:
            text1 = e1.get_attribute ('value')
        try:
            e1.send_keys (text)
            log.info ("Had type  [ %s ] in inputBox" % text)
        except NameError as e:
            log.error ("Failed to type in input box with %s" % text1)
            log.error ("Failed  %s" % e)
            self.get_windows_img ()

    # 回车键
    def enter_key(self, selector):
        e1 = self.find_element (selector)
        try:
            e1.send_keys (Keys.ENTER)
            log.info ("Had touch the Enter keys .")
        except Exception as e:
            log.error ("Failed to touch any keys")
            self.get_windows_img ()

    # 清除文本框
    def clear_text(self, selector):
        el = self.presence_of_element_located(selector)
        try:
            el.clear ()
            log.info ("Clear text in input box before typing.")
        except NameError as e:
            log.error ("Failed to clear in input box with %s" % e)
            self.get_windows_img ()

    # 获取元素的文本信息
    def get_text(self, selector):
        if self.find_element (selector).text:
            text = self.find_element (selector).text
        else:
            text = self.find_element (selector).get_attribute ('value')
        log.info ("get the element and iteself text:%s" % text)
        return text

    # 判断一个页面元素是否显示在当前页面
    def verifyElementIsPresent(element):
        try:
            if element.isDisplayed ():
                log.info ('the element %s is displayed.' % str (element))
        except Exception as e:
            log.info ('displayed error,%s' % e)

    # 点击元素
    def click(self, selector):
        s =self.presence_of_element_located(selector)
        try:
            s.click ()
            log.info ("The element was clicked." )
        except NameError as e:
            log.error ("Failed to click the element with %s" % e)

    def click_and_submit(self, selector, n):
        element=self.presence_of_element_located(selector)
        if n == 0:
            element.click ()
        else:
            element.submit ()

    def element_jietu(self,selector):
        self.driver.save_screenshot('element_picture/bdbutton.png')
        element = self.find_element(selector)
        # print(element.location)  # 打印元素坐标
        # print(element.size)  # 打印元素大小
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        im = Image.open('bdbutton.png')
        im = im = Image.open('bdbutton.png').crop((left, top, right, bottom))
        im.save('element_picture/bdbutton.png')
    '''*****************************----  wait_until  【开始】 ---*************************************************'''
    def handle_locator(self,selector):
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == 'id':
            by = By.ID
        elif selector_by == 'name':
            by = By.NAME
        elif selector_by == 'link text':
            by = By.LINK_TEXT
        elif selector_by == 'partial link text':
            by = By.PARTIAL_LINK_TEXT
        elif selector_by == 'tag name':
            by = By.TAG_NAME
        elif selector_by == 'class name':
            by = By.CLASS_NAME
        elif selector_by == 'css selector'or selector_by == 'css':
            by = By.CSS_SELECTOR
        elif selector_by == 'xpath':
            by = By.XPATH
        return (by,selector_value)
    '''***---wait_until---******'''
    def title_is(self,text):
        '''判断title,返回布尔值'''
        return  WebDriverWait(self.driver, 10).until(EC.title_is(text))
    def title_contains(self,text):
        '''判断title，返回布尔值'''
        return  WebDriverWait(self.driver, 10).until(EC.title_contains(text))
    def presence_of_element_located(self,selector):
        '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    def visibility_of_element_located(self,selector):
        '''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
        locator=self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    def visibility_of_element_located(self,selector):
        '''判断元素是否可见，如果可见就返回这个元素'''
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element(locator)))
    def presence_of_all_elements_located(self,selector):
        '''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
    def visibility_of_any_elements_located(self,selector):
        '''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(locator))
    def text_to_be_present_in_element(self,selector,text):
        '''判断指定的元素中是否包含了预期的字符串，返回布尔值'''
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
    def text_to_be_present_in_element_value(self,selector,value):
        '''判断指定元素的属性值中是否包含了预期的字符串，返回布尔值'''
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(locator,value))
    def frame_to_be_available_and_switch_to_it(self,locator):
        '''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
        # 注意这里并没有一个frame可以切换进去
        return WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it(locator))
    def invisibility_of_element_located(self,selector):
        '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
        # 注意#swfEveryCookieWrap在此页面中是一个隐藏的元素
        locator = self.handle_locator(selector)
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
    def element_to_be_clickable(self,selector):
        '''判断某个元素中是否可见并且是enable的，代表可点击'''
        # driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]").click()
        # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wrapper']/div[6]/a[1]"))).click()
        locator = self.handle_locator(selector)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
    def staleness_of(self,selector):
        '''等待某个元素从dom树中移除'''
        return WebDriverWait(self.driver,10).until(EC.staleness_of(self.find_element(selector)))
    def element_to_be_selected(self,selector):
        '''判断某个元素是否被选中了,一般用在下拉列表'''
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_selected(self.find_element(selector)))
    def element_selection_state_to_be(self,selector):
        '''判断某个元素的选中状态是否符合预期'''
        return WebDriverWait(self.driver, 10).until(
            EC.element_selection_state_to_be(self.find_element(selector), True))
    def element_located_selection_state_to_be(self,selector):
        '''判断某个元素的选中状态是否符合预期'''
        # self.driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
        locator = self.handle_locator(selector)
        return  WebDriverWait(self.driver, 10).until(
            EC.element_located_selection_state_to_be(locator, True))


    '''*****************************----  wait_until  【结束】 ---*************************************************'''