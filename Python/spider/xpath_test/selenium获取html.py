 # -*- coding: utf-8 -*-
from selenium import webdriver
import sys
from urllib import request
import time
import codecs

def gethtml(url):
    page = request.urlopen(url)
    html_all = page.read()
    return html_all

def get_jingtai_dongtai_html(url):
    sel = webdriver.Chrome()
    sel.get(url)
    time.sleep(3)
    sel.set_window_size(480, 600)
    html1=sel.page_source
    print(html1)

    # with codecs.open('result-dongtai4.html','w',encoding='utf-8')as putin1:
    #     putin1.write(html1)
    #     html2=gethtml(url)
    #     with codecs.open('result-jingtai4.html','w',encoding='utf-8')as putin2:
    #         putin2.write(html2)
    # sel.close()
    # sel.quit()
url="http://193.169.100.249:8086/itmsld/login"
# gethtml(url)
# get_jingtai_dongtai_html(url)
# sel = webdriver.Chrome()
# sel.get(url)
# time.sleep(3)
# sel.set_window_size(480, 600)
# html1=sel.page_source
# print(type(html1))
