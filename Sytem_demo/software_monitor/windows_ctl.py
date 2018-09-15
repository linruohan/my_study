# -*- coding:utf-8 -*-
# python操作Windows窗口程序


# Pywin32
# 首先，安装一个Pywin32，为python提供访问Windows API的扩展，提供了齐全的windows常量、接口、线程以及COM机制等等。其次，为了方面查找目标窗口的句柄，可以下载一个微软自家的Spy++，这玩意儿满大街都是。有了它，还能很方便的查看窗体的消息。
# 句柄是一个32位整数，在windows中标记对象用，类似一个dict中的key。
# 消息是windows应用的重要部分，用来告诉窗体“发生了什么”，比如给一个按钮发送BN_CLICKED这么个消息，按钮就知道“哦，我被点了”，才能执行相应的下一步操作。本文将大量使用消息机制。详情参看这篇文章。
#
# 查找窗体句柄
# 貌似在win32编程的世界里，包括窗口到文本框的所有控件就是窗体，所有的窗体都有独立的句柄。要操作任意一个窗体，你都需要找到这个窗体的句柄，这里，我们就可以用到FindWindow函数和FindWindowEx函数。在pywin32中，他们都属于win32gui的模块。
#
# FindWindow(lpClassName=None, lpWindowName=None):
# 描述：自顶层窗口（也就是桌面）开始搜索条件匹配的窗体，并返回这个窗体的句柄。不搜索子窗口、不区分大小写。找不到就返回0
# 参数：
# lpClassName：字符型，是窗体的类名，这个可以在Spy++里找到。
# lpWindowName：字符型，是窗口名，也就是标题栏上你能看见的那个标题。
# 说明：这个函数我们仅能用来找主窗口。
#
# FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None, lpszWindow=None);
# 描述：搜索类名和窗体名匹配的窗体，并返回这个窗体的句柄。不区分大小写，找不到就返回0。
# 参数：
# hwndParent：若不为0，则搜索句柄为hwndParent窗体的子窗体。
# hwndChildAfter：若不为0，则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体，否则从第一个子窗体开始搜索。
# lpClassName：字符型，是窗体的类名，这个可以在Spy++里找到。
# lpWindowName：字符型，是窗口名，也就是标题栏上你能看见的那个标题。
# 说明：找到了主窗口以后就靠它来定位子窗体啦。
#
# 菜单操作
# 有了句柄，我们就可以操作FaceGen了！嗯，要先打开文件，File→Open，然后再File→Save Image（很悲剧，Save Image没有快捷键，所以不得不进行菜单操作）。现在我们有了FindWindow和FindWindowEx，要怎么操作菜单呢？
#
# 哦，抱歉，靠他俩还做不到。
#
# 窗口的菜单就像窗口的标题栏一样，是窗口自身的一部分，不是其他窗体控件，也就没有办法用FindWindow和FindWindowEx返回句柄。所以要对菜单进行操作的话，我们需要新的函数，也就是GetMenu，GetSubMenu和GetMenuItemID，它们也都属于win32gui模块。结合下图来说：
#
# PostMessage(hWnd, Msg, wParam, lParam)
# 描述：在消息队列中加入为指定的窗体加入一条消息，并马上返回，不等待线程对消息的处理。
# 参数：
# hWnd：整型，接收消息的窗体句柄
# Msg：整型，要发送的消息，这些消息都是windows预先定义好的，可以参见系统定义消息（System-Defined Messages）
# wParam：整型，消息的wParam参数
# lParam：整型，消息的lParam参数
# 说明：简单说，就是给指定程序发一个消息，这些消息都用整型编好号，作为windows的常量可以查询的。在这里，我们用的就是win32con这个库里定义的WM_COMMAND这个消息，具体的wParam和lParam是根据消息的不同而不同的。具体请根据MSDN查阅。
#
# GetMenu(hwnd)
# 描述：获取窗口的菜单句柄。
# 参数：
# hwnd：整型，需要获取菜单的窗口的句柄。
# 说明：获取的是插图中黄色的部分。
#
# GetSubMenu(hMenu, nPos)
# 描述：获取菜单的下拉菜单或者子菜单。
# 参数：
# hMenu：整型，菜单的句柄，从GetMenu获得。
# nPos：整型，下拉菜单或子菜单的的索引，从0算起。
# 说明：这个可以获取插图中蓝色的部分；如描述所述，这个不仅可以获取本例中的下拉菜单，还可以获取子菜单。
#
# GetMenuItemID(hMenu, nPos)
# 描述：获取菜单中特定项目的标识符。
# 参数：
# hMenu：整型，包含所需菜单项的菜单句柄，从GetSubMenu获得。
# nPos：整型，菜单项的索引，从0算起。
# 说明：这个获取的就是红色区域中的项目啦，注意，分隔符是被编入索引的，所以Open的索引是2而非1，而Exit的索引是9而非6。
#
# 控件操作
# 在这里，我们用了SendMessage而不是PostMessage，其区别就在于我们可以通过SendMessage取得消息的返回信息。因为对于我们要设置文本框信息的WM_SETTEXT信息来说，设置成功将返回True。
#
# SendMessage(hWnd, Msg, wParam, lParam)
# 描述：在消息队列中加入为指定的窗体加入一条消息，直到窗体处理完信息才返回。
# 参数：
# hWnd：整型，接收消息的窗体句柄
# Msg：整型，要发送的消息，这些消息都是windows预先定义好的，可以参见系统定义消息（System-Defined Messages）
# wParam：整型，消息的wParam参数
# lParam：整型，消息的lParam参数
# 说明：wParam和IParam根据具体的消息不同而有不同的定义，详情参阅Part 2.


"""
Created on 2018/3/12
# 定时获取数据接口数据写入Excel表格，Excel需要被其他程序使用，需要处于开启状态。
@author: jj
"""
import urllib
import json
import xlwt
import copy
import time
import os
import win32gui
import win32con

def write_ex(data):
    """
    数据 写 文件
    :param data:
    :return:
    """
    file = xlwt.Workbook(encoding='utf-8')
    table = file.add_sheet("sheet4")
    params = ['类型', '项目名称', '设备编号', '阀门开关', '泵1开关', '泵2开关', '水位', '上报时间', '水池大小', '管径']
    params_code = ['leixing', 'name', 'code', 'famen', 'ben1', 'ben2', 'shuiwei', 'date', 'daxiao', 'guanjing']
    for index, item in enumerate(params):
        table.write(0, index, item)
    table.write(0, 10, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for l_index, equipment in enumerate(data):
        for j_index, item in enumerate(params_code):
            table.write(l_index+1, j_index, equipment.get(item))
    filename = u"003.xlsx"
    file_path = os.path.join(filename)
    file.save(file_path)

if __name__ == '__main__':
    print (u'盐池数据同步已开启 >> 西部绿谷数据.xlsx')
    while True:
        # get_api()
        print (u'盐池数据本次同步已完成 时间 %s  数据5分钟后更新 >> 西部绿谷数据.xls' % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        os.startfile(u"002.xlsx")   # 打开文件
        wndtitle = u"002.xlsx - Excel"   # 进程名
        wndclass = None
        wnd = win32gui.FindWindow(wndclass, wndtitle)    # 获取窗口句柄
        win32gui.CloseWindow(wnd)      # 窗口最小化
        time.sleep(300)
        win32gui.SendMessage(wnd, win32con.WM_CLOSE)   # 关闭窗口