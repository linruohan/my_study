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
from PyQt5.QtWidgets import QInputDialog,QFrame,QColorDialog
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        col = QColor(12, 133, 30)

        self.btn=QPushButton('Dialog',self)
        self.btn.move(100,200)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(100, 245)


        self.btn=QPushButton('ColorDialog',self)
        self.btn.move(10,20)
        self.btn.clicked.connect(self.showColorDialog)

        self.frm=QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color:%s}'% col.name())
        self.frm.setGeometry(130,20,30,30)

        self.setGeometry(300,300,300,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def showDialog(self):
        '''对话框返回输入的文本和一个布尔值。
        点击Ok按钮,布尔值是True'''
        text,ok=QInputDialog.getText(self,'Input Dialog','Enter your words:')
        if ok:
            self.le.setText(str(text))
    def showColorDialog(self):
        col=QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color:%s}' % col.name())

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
