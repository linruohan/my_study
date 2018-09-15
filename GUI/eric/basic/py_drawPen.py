# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
import sys,random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    '''鼠标左键点击这个按钮会在控制台中输出’press’消息。
    鼠标右击进行拖动。'''
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):


        self.setGeometry(300,300,400,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def paintEvent(self, e):
        qp=QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
    def drawLines(self,qp):
        pen=QPen(Qt.red,2,Qt.SolidLine)#钢笔绘制风格,颜色  宽度为2像素

        qp.setPen(pen)
        qp.drawLine(20,40,250,80)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20,120,250,80)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20,160,250,80)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20,200,250,80)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        '''Qt.CustomDashLine并调用了setDashPattern()方法，
        它的参数(一个数字列表)定义了一种风格，必须有偶数个数字；
        其中奇数表示绘制实线，偶数表示留空。数值越大，直线或空白
        就越大。这里我们定义了1像素的实线，4像素的空白，5像素实线，4像素空白'''
        qp.setPen(pen)
        qp.drawLine(20,240,250,80)


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
