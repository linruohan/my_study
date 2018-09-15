# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
import sys
from PyQt5.QtWidgets import QApplication, QWidget,\
    QToolTip,QPushButton,QMessageBox,QDesktopWidget,QLabel
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,\
    QGridLayout,QTextEdit,QLineEdit,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon ,QFont,QColor#图标,字体
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtWidgets import QSlider,QLCDNumber
from PyQt5.QtWidgets import QInputDialog,QFrame,QColorDialog,QFontDialog,QSizePolicy
from PyQt5.QtWidgets import QCheckBox
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        '''-------------单选框------------------'''
        cb=QCheckBox('Show title',self)
        cb.move(120,120)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        '''-------------开关按钮------------------'''
        self.col=QColor(0,0,0)
        redb=QPushButton('Red',self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked.connect(self.setColor)

        greenb=QPushButton('Green',self)
        greenb.setCheckable(True)
        greenb.move(10,60)
        greenb.clicked.connect(self.setColor)

        blueb=QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked.connect(self.setColor)

        whiteb=QPushButton('white',self)
        whiteb.setCheckable(True)
        whiteb.move(10,180)
        whiteb.clicked.connect(self.setColor)

        self.square=QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget { background-color:%s}'% self.col.name())



        self.setGeometry(300,300,400,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def changeTitle(self,state):
        '''单选框'''
        if state==Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
    def setColor(self,pressed):
        source=self.sender()
        if pressed:
            val=255
        else:val=0
        if source.text()=='Red':
             self.col.setRed(val)
        elif source.text()=='Green':
            self.col.setGreen(val)
        elif source.text()=='white':
            self.col.setAlpha(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet('QWidget { background-color:%s}' % self.col.name())


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
