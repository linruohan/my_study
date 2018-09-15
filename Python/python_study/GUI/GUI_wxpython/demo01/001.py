#coding=utf-8

import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'text',size=(400,575))
        panel=wx.Panel(self,-1)
        text=wx.StaticText(panel,-1,'hello world',(230,30),(80,15))#静态文本框
        text.SetForegroundColour('blue')#前景色
        text.SetBackgroundColour('white')#背景色
        font=wx.Font(12,wx.DEFAULT,wx.ITALIC,wx.NORMAL,True)#字体
        text.SetFont(font)#设置字体

        #用户名
        Label1=wx.StaticText(panel,-1,u'用户名:',pos=(10,10))
        self.inputText=wx.TextCtrl(panel,-1,'',pos=(80,10),size=(150,-1))
        self.inputText.SetInsertionPoint(0)
        #密码
        Label2=wx.StaticText(panel,-1,u'密码:',pos=(10,50))
        self.pwdText=wx.TextCtrl(panel,-1,'',pos=(80,50),size=(150,-1),style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER,self.OnLostFocus,self.pwdText)


        #创建多行文本框
        multiText=wx.TextCtrl(panel,-1,'adfasdf\
                asdfsadfasd\
                asdfasdfasdf\
                asdfasdfsadf',
                pos=(10,93),size=(190,80),style=wx.TE_MULTILINE|wx.TE_CENTER)
        multiText.SetBackgroundColour('red')
        multiText.SetFocus()

        #位图按钮
        tmp=wx.Image('E:\\atom\\Python\\GUI\\GUI_wxpython\\demo01\\1.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.button=wx.BitmapButton(panel,-1,tmp,pos=(80,175),size=(100,100))
        self.Bind(wx.EVT_BUTTON,self.Onclick,self.button)

        #单选框
        radioRed=wx.RadioButton(panel,-1,u'红',pos=(20,190))
        radioBlue=wx.RadioButton(panel,-1,u'蓝',pos=(20,210))
        radioGreen=wx.RadioButton(panel,-1,u'绿',pos=(20,230))
        #建立颜色和wx常量的对应关系
        self.colors={'红':wx.RED,'蓝':wx.BLUE,'绿':wx.GREEN,}
        self.textcolor=wx.TextCtrl(panel,-1,'',pos=(10,300))

        for radio in (radioRed,radioBlue,radioGreen):
            self.Bind(wx.EVT_RADIOBUTTON,self.Onradio,radio)

    def Onradio(self,event):
        radioSelect=event.GetEventObject()
        str=radioSelect.GetLabel()
        #选择radio的背景色
        self.textcolor.SetBackgroundColour(self.colors(str.encode('utf-8')))
        self.textcolor.SetFocus()


    def Onclick(self,event):
        wx.MessageBox('hello,world',u'提示')

    def OnLostFocus(self,evt):
        wx.MessageBox('%s,%s' %(self.inputText.GetValue(),self.pwdText.GetValue()),'显示')

if __name__=="__main__":
    app=wx.App()
    frame=TextFrame()
    frame.Show()
    app.MainLoop()
