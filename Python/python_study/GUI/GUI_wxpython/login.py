import wx

class Mywin(wx.Frame):
   def __init__(self, parent, title):
      super(Mywin, self).__init__(parent, title = title,size = (350,250))#重构应用类的构造方法
# ——————【面板窗口】
      panel = wx.Panel(self) #面板窗口
# =============BoxSizer垂直的容器=========================================================
      vbox = wx.BoxSizer(wx.VERTICAL) #大小测定器(sizers)垂直的
    # =============BoxSizer水平的容器=========================================================
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) #大小测定器(sizers)水平的
      l1 = wx.StaticText(panel, -1, "用户名")

      hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t1 = wx.TextCtrl(panel)

      hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped)
      vbox.Add(hbox1)
    # =============BoxSizer水平的容器==========================================================
      hbox2 = wx.BoxSizer(wx.HORIZONTAL)#大小测定器(sizers)水平的
      l2 = wx.StaticText(panel, -1, "密码")

      hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5)
      self.t2 = wx.TextCtrl(panel,style = wx.TE_PASSWORD)
      self.t2.SetMaxLength(5)

      hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      vbox.Add(hbox2)
      self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
      # ==============BoxSizer水平的容器=========================================================
      hbox3 = wx.BoxSizer(wx.HORIZONTAL)#大小测定器(sizers)水平的
      l3 = wx.StaticText(panel, -1, "信息显示")

      hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t3 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE)

      hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      vbox.Add(hbox3)
      self.t3.Bind(wx.EVT_TEXT_ENTER,self.OnEnterPressed)
    # =================BoxSizer水平的容器======================================================
      hbox4 = wx.BoxSizer(wx.HORIZONTAL)#大小测定器(sizers)水平的
      l4 = wx.StaticText(panel, -1, "提示信息")

      hbox4.Add(l4, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      self.t4 = wx.TextCtrl(panel, value = "密码错误",style = wx.TE_READONLY|wx.TE_CENTER)

      hbox4.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
      vbox.Add(hbox4)
      panel.SetSizer(vbox)

      self.Centre()
      self.Show()
      self.Fit()

   def OnKeyTyped(self, event):
      print (event.GetString())

   def OnEnterPressed(self,event):
      print ("Enter pressed" )

   def OnMaxLen(self,event):
      print ("Maximum length reached" )

app = wx.App()
Mywin(None,  '登录')
app.MainLoop()
