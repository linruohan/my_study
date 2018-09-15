#encoding=utf-8
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os,sys,io
from lxml import etree
import lxml.html as HTML
from urllib.request import urlopen
from urllib import request
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
driver = webdriver.Chrome()#用的谷歌，到http://chromedriver.storage.googleapis.com/index.htm 下载
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("http://193.169.100.249:8086/itmsld/login")

# try:
#     driver.get("http://music.163.com/#/song?id=31877470")
# except selenium.common.exceptions.TimeoutException:
#     print("time out of 10 s")
#     driver.execute_script('window.stop()')

# print(u"休眠结束")
# driver.switch_to.frame("contentFrame")
# time.sleep(5)
# print(driver.find_element_by_id('comment-box').text.encode('GBK', 'ignore'))
bsObj = BeautifulSoup(driver.page_source,'lxml')
source = driver.page_source.encode('GBK', 'ignore')
# open('163.txt','wb').write(source)
#163.txt文件可以看到精彩评论的
# print(driver.page_source.encode('GBK', 'ignore'))
print(type(source))
html=driver.page_source
page = etree.HTML(html)
hrefs = page.xpath(u"//a")
# 打印属性和文本内容
for href in hrefs:
    print (href.attrib)
    print(href.text)

htree = etree.ElementTree(page)

# 依次打印出hdoc每个元素的文本内容和xpath路径
# for t in page.iter():
#     print (htree.getpath(t))
#     print (t.text)
#     # if t.text:
    #     print (htree.getpath(t))
    #     print (t.text)
