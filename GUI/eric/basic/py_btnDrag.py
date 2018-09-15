# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button1(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
    def mouseMoveEvent(self,e):
        if e.buttons()!=Qt.RightButton:
            return
        mimeData=QMimeData()
        drag=QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos()-self.rect().topLeft())

        dropAction=drag.exec_(Qt.MoveAction)
    def mousePressEvent(self, e):
        QPushButton.mouseMoveEvent(self,e)
        if e.buttons()==Qt.LeftButton:
            print('press')

class Example(QWidget):
    '''鼠标左键点击这个按钮会在控制台中输出’press’消息。
    鼠标右击进行拖动。'''
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setAcceptDrops(True)
        self.btn=Button1('button',self)
        self.btn.move(100,65)



        self.setGeometry(300,300,400,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def dragEnterEvent(self, e):
        e.accept()
    def dropEvent(self, e):
        position=e.pos()
        self.btn.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())








    # # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    # app = QApplication(sys.argv)
    # # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    # w = QWidget()
    # # resize()方法调整窗口的大小。这离是250px宽150px高
    # w.resize(250, 150)
    # # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    # w.move(300, 300)
    # # 设置窗口的标题
    # w.setWindowTitle('Simple')
    # # 显示在屏幕上
    # w.show()
    #
    # # 系统exit()方法确保应用程序干净的退出
    # # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    # sys.exit(app.exec_())
