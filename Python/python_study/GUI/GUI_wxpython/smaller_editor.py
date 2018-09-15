# -*- coding: utf-8 -*-
import wx

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(300,400))
        self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu=wx.Menu()

        filemenu.Append(wx.ID_ABOUT,u"关于",u"关于程序的信息")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,u"退出",u"终止应用程序")


        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,u"文件")
        self.SetMenuBar(menuBar)
        self.Show(True)

app=wx.App(False)
frame=MainWindow(None,"editor")
app.MainLoop()
