from itmsv1_mvc.common.mylog import Log as log
log = log ()
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time,os,sys,io
'''浏览器相关'''
class BrowserUtil:
    # --浏览器的操作
    def __init__(self, driver):
        self.driver = driver

    # 获取当前页面url
    def get_url(self):
        url = self.driver.current_url
        log.info("get the current page url:%s" % url)
        return url
    # 或者网页标题
    def get_title(self):
        log.info("Current page title is %s" % self.driver.title)
        return self.driver.title
    # 浏览器前进操作
    def forward(self):
        self.driver.forward ()
        log.info ("Click forward on current page.")
    # 浏览器后退操作
    def back(self):
        self.driver.back ()
        log.info ("Click back on current page.")
    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait (seconds)
        log.info ("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close ()
            log.info ("Closing and quit the browser.")
        except NameError as e:
            log.error ("Failed to quit the browser with %s" % e)
    def quit(self):
        self.driver.quit()

    # 截图
    def screenshot(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname (os.path.dirname (__file__)) + '/screenshots/'
        rq = time.strftime ('%Y%m%d%H%M', time.localtime (time.time ()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file (screen_name)
            log.info ("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            log.error ("Failed to take screenshot! %s" % e)
            self.get_windows_img ()

    # 获取当前window handle
    def get_now_handle(self):
        handle = self.driver.current_window_handle
        log.info ("current widnow handles is:%s" % handle)
        return handle

    def switch_frame(self, fname):
        self.driver.switch_to.frame (fname)
        time.sleep (1)
    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()
        time.sleep (1)
    def switch_current_frame(self):
        self.driver.switch_to.default_content()
        time.sleep (1)
        # 多窗口切换

    def switch_window(self, to_handle):
        now_handle = self.get_current_window_handle
        old_handle = to_handle
        handles = self.driver.window_handles
        log.info("current handles number is:%s" % len(handles))
        for handle in handles:
            if handle != now_handle:
                log.info('now to switch another window:%s' % handle)
                self.driver.close()  # 关闭当前焦点所在的窗口
                self.driver.switch_to.window(to_handle)  # 切换到第二个窗口

    def alert_is_present(self):
        instance = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
        print(instance.text)
        instance.accept()
    def switch_alert_accept(self):
        self.driver.switch_to_alert().accept()

    def switch_alert_cancel(self):
        self.driver.switch_to_alert().dismiss()
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        log.info("Sleep for %d seconds" % seconds)

    def get_source(self):
        page = self.driver.page_source
        return page