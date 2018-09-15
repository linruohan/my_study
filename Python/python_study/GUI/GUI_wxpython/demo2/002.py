# coding=utf-8

import wx
import wx.grid as grid
import pprint

class MyGrid(grid.Grid):
    def __init__(self,parent):
        grid.Grid.__init__(self,parent,-1)
        self.CreateGrid(5,5)
        #表格事件
        self.Bind(grid.EVT_GRID_CELL_LEFT_CLICK,self.OnCellLeftClick)
        self.Bind(grid.EVT_GRID_CELL_RIGHT_CLICK,self.OnCellRightClick)
        self.Bind(grid.EVT_GRID_SELECT_CELL,self.OnSelectCell)
        self.Bind(grid.EVT_GRID_RANGE_SELECT,self.OnRangeSelect)
        self.Bind(grid.EVT_GRID_CELL_CHANGED,self.OnCellChanged)
        #当编辑单元格时出发的事件
        self.Bind(grid.EVT_GRID_EDITOR_SHOWN,self.OnEditorShown)
        self.Bind(grid.EVT_GRID_EDITOR_HIDDEN,self.OnEditorHidden)
        self.Bind(grid.EVT_GRID_EDITOR_CREATED,self.OnEditorCreated)
        #响应键盘输入
        self.Bind(wx.EVT_KEY_DOWN,self.OnkeyDown)



    def OnCellLeftClick(self,evt):
        print('(%d,%d)' %(evt.GetRow(),evt.GetCol()))
        evt.Skip()
    def OnCellRightClick(self,evt):
        wx.MessageBox('%s' %(evt.GetPosition()),u'提示')
        evt.Skip()
    def OnSelectCell(self,evt):
        self.SetBackgroundColour(evt.GetRow(),evt.GetCol(),wx.RED)
        evt.Skip()

    def OnRangeSelect(self,evt):
        if evt.Selecting():
            print('(%s,%s)' %(evt.GetTopLeftCoords(),evt,GetBottomRightCoords))
        evt.Skip()
    def OnCellChanged(self,evt):
        value=self.GetCellValue(evt.GetRow(),evt.GetCol())
        print(value)
    def OnEditorShown(self,evt):
        print('show')
        evt.Skip()
    def OnEditorHidden(self,evt):
        print('hiddon')
        evt.Skip()
    def OnEditorCreated(self,evt):
        print(evt.GetContol())
    def OnkeyDown(self,evt):
        pass

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'表格事件',size=(500,180))
        # panel=wx.Panel(self,-1)
        self.grid=MyGrid(self)

if __name__ == '__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
