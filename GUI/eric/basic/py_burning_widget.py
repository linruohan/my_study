# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
import sys,random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Communicate(QObject):
    updateBW=pyqtSignal(int)

class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self .initUI()
    def initUI(self):
        self.setMinimumSize(1,30)
        self.value=75
        self.num=[75, 150, 225, 300, 375, 450, 525, 600, 675]
    def setValue(self,value):
        self.value=value
    def paintEvent(self, QPaintEvent):
        qp=QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
    def drawWidget(self,qp):
        font=QFont('Serif',7,QFont.Light)
        qp.setFont(font)

        size=self.size()
        w=size.width()
        h=size.height()

        step=int(round(w/10.0))
        '''till参数定义了需要绘制的总尺寸，
        它根据slider控件计算得出，是整体区域的比例值。
        full参数定义了红色区域的绘制起点。
        注意在绘制时为取得较大精度而使用的浮点数运算。'''
        till=int((w/750.0)*self.value)
        full=int((w/750.0)*700)

        if self.value>=700:
            qp.setPen(QColor(255,255,255))
            qp.setBrush(QColor(255,255,184))
            qp.drawRect(0,0,full,h)
            qp.setPen(QColor(255,175,175))
            qp.setBrush(QColor(255,175,175))
            qp.drawRect(full,0,till-full,h)
        else:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)
        pen=QPen(QColor(20,20,20),1,Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0,0,w-1,h-1)


        j=0
        for i in range(step,10*step,step):
            qp.drawLine(i,0,i,5)
            metrics=qp.fontMetrics()
            fw=metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2,h/2,str(self.num[j]))
            j+=1



class Example(QWidget):
    '''Burning widget(烧录控件)
这个控件可能会在Nero，K3B或其他CD/DVD烧录软件中见到。'''
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        sld=QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1,750)
        sld.setValue(75)
        sld.setGeometry(30,40,150,30)

        self.c=Communicate()
        self.wid=BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox=QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.setGeometry(300,300,400,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def changeValue(self,value):
        self.c.updateBW.emit(value)
        self.wid.repaint()

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
