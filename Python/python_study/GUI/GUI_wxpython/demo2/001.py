# coding=utf-8

import wx
import wx.grid


class MyFrame(wx.Frame):
    def __init__(self):
        rowtitle=[u'第1行',u'第2行',u'第3行',u'第4行',]
        coltitle=[u'第1列',u'第2列',u'第3列',u'第4列',]
        wx.Frame.__init__(self,None,title=u'表格',size=(450,500))
        grid=wx.grid.Grid(self)#定义表格控件
        grid.CreateGrid(4,4)
        for i in range(4):
            grid.SetRowLabelValue(i,rowtitle[i])#行标题
            grid.SetColLabelValue(i,coltitle[i])#列标题
            for j in range(4):
                grid.SetCellValue(i,j,str(j))#设置单元格的值

    

if __name__ == '__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
