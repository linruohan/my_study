# import wx
# app=wx.App()
# window=wx.Frame(None,title="文件夹",size=(500,600), name = "frame")
# window.CreateToolBar(id=1,name="ToolBarNameStr")
# panel=wx.Panel(window)
# label=wx.StaticText(panel,label="hello world",pos=(100,100))
# window.Show(True)
# app.MainLoop()
# -*- coding: utf-8 -*-
"""
http://blog.csdn.net/chenghit
"""
import wx
# wx.Frame(Parent, ID, Title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="frame")
app = wx.App(False) #创建1个APP，禁用stdout/stderr重定向
frame = wx.Frame(None, wx.ID_ANY, "Hello, World!")  #这是一个顶层的window
frame.Show(True)    #显示这个frame
app.MainLoop()
