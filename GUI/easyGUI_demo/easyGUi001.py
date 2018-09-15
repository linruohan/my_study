import easygui
# path = easygui.fileopenbox()
# print(path)
import os
import tkinter.filedialog as dialog

default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
# fname = dialog.askopenfilename(title=u"选择文件",
#                                      initialdir=(os.path.expanduser(default_dir)))
#
# print (fname)  # 返回文件全路径
print( dialog.askdirectory() ) # 返回目录路径