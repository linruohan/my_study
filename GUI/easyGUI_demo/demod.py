#coding =utf-8
import easygui as g

import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# g.msgbox('显示一个窗口并显示这些文字')
msg='message'
title='开始'
choices=['1234','老鼠和米','我','你',]
# choice=g.choicebox(msg,title,choices)
# g.msgbox(choice)
# g.msgbox(msg="(Your message goes here)",title=" ",ok_button="OK",image=None,root=None)
# if g.ccbox('要再来一次吗？', choices=('要啊要啊^_^', '算了吧T_T')):
#     g.msgbox('不给玩了，再玩就玩坏了......')
# else:
#     sys.exit(0) # 记得先 import sys 哈
# g.buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, )
# g.msgbox(g.buttonbox("我爱你",'你说爱不爱',('唉','你唉','爱爱爱','爱爱爱')))
# g.buttonbox('大家说我长得帅吗？', image='1.jpg', choices=('帅', '不帅', '!@#$%'))
# g.multchoicebox(msg='Pick as many items as you like.', title=' ', choices=choices, )
# str1=g.multchoicebox('你现在最想干啥','这是标题',('抽烟','打游戏','和蔡伟伟一起玩','学东西写代码','唉,日了狗了'))
# if str1==None:
#     g.msgbox('你选择了错误')
# print(str1)
# g.msgbox(str1)


# integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments)

# g.integerbox(msg='输入你的分数 0~150', title='分数采集 ', default=0, lowerbound=0, upperbound=150)
# g.textbox('下面是题解','求模','str1',1)
# g.passwordbox(msg='Enter your password.', title=' ', default='', image='1.jpg', root=None)
# (account,password)=g.multpasswordbox('请输入您的账号密码','登录框',('帐号','密码'))
# g.msgbox('显示用户信息','小明','帐号:  '+account+'\n'+'密码:  '+password)
# str1=g.diropenbox('选择文件目录','浏览文件夹','C:/Users/Administrator/Desktop')
# g.msgbox(str1)
str1=g.fileopenbox('选择文件','提示','C:/Users/Administrator/Desktop/__pycache__')
s=g.msgbox(str1)
print(s.__getattribute__.value)
