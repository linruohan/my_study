# coding=utf-8
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads
# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "testsuites")
print('casepath>>>',casepath)
if not os.path.exists(casepath):
    print("测试用例需放到‘test_case’文件目录下")
    os.mkdir(casepath)
reportpath = os.path.join(curpath, "test_report")
if not os.path.exists(reportpath): os.mkdir(reportpath)
print('report_path>>>',reportpath)
def add_case(case_path=casepath, rule="*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
    pattern=rule,
    top_level_dir=None)
    # print(discover)
    return discover
@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试deafult报告', log_path='report')
if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    # print(cases)
    for i in cases:
        print(i)
        run(i)
