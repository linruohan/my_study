#coding=utf-8
from selenium import webdriver
import unittest
import HTMLTestRunner
import os ,time
from  email.mime.text import MIMEText

def sentmail(file_new):
    #发信邮箱
    mail_from='fnngj@126.com'
    #收信邮箱
    mail_to='123456@qq.com'
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.126.com')
    #用户名密码
    smtp.login('fnngj@126.com','123456')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print ('email has send out !')

#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'E:\\atom\\Python\\itmsv1\\report'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print (file_new)
    #调用发邮件模块
    sentmail(file_new)

path = 'E:\\atom\\itmsv1\\testcase'
def creatsuitel():
    testunit=unittest.TestSuite()
    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(path,
    pattern ='*.py',
    top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print (testunit)
    return testunit

if __name__ == "__main__":
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
    #执行发邮件
    sendreport()
