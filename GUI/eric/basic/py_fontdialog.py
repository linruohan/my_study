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
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox=QVBoxLayout()
        btn=QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(10,20)
        btn.clicked.connect(self.showDialog)

        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.lb1=QLabel('Knowledge only matters',self)
        self.lb1.setGeometry(20,0,200,150)

        self.setGeometry(300,300,400,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def showDialog(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.lb1.setFont(font)

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
