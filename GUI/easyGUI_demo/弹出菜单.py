from tkinter import *

top=Tk()
top.wm_title("弹出菜单")
top.geometry("400x300+300+200")

def popLabel():
    global top
    Label(top,text="I love python").pack()

# 创建菜单
menubar=Menu(top)
for x in ['java','javascript','php']:
    menubar.add_command(label=x)

# 创建第四个菜单项，并 绑定事件
menubar.add_command(label='python',command=popLabel)

def pop(event):
    # Menu 类里面有一个 post 方法，它接收两个参数，即 x 和y 坐标，它会在相应的位置弹出菜单。
    menubar.post(event.x_root,event.y_root)

# 鼠标右键是用的<Button-3>
# 使用 Menu 类的 pop 方法来弹出菜单
top.bind("<Button-3>",pop)
top.mainloop()