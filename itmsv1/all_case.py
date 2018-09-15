#coding=utf-8
from selenium import webdriver
import unittest
import HTMLTestRunner
import os ,time
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

list_test='E:\\atom\\Python\\itmsv1\\testcase'
def creatsuitel():
    testunit=unittest.TestSuite()
    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(list_test,pattern ='*.py',top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            # print (testunit)
    return testunit

alltestnames = creatsuitel()
now = time.strftime(' %Y-%m-%d-%H_%M_%S ',time.localtime(time.time()))
filename = 'E:\\atom\\Python\\itmsv1\\report\\'+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'测试报告',
description=u'用例执行情况：')
#执行测试用例
runner.run(alltestnames)
