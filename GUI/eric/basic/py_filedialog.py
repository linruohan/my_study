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
from PyQt5.QtWidgets import QInputDialog,QFrame,QColorDialog,QFontDialog,QSizePolicy,QFileDialog
import webbrowser,docx
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit=QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile=QAction(QIcon('read.ico'),'打开文件',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        openFileBox=QAction(QIcon('snake.ico'),'打开文件夹',self)
        openFileBox.setShortcut('Ctrl+F')
        openFileBox.setStatusTip('Open new Filebox')
        openFileBox.triggered.connect(self.showDialog_Box)

        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(openFileBox)



        self.setGeometry(300,300,400,420)#x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('bug.ico'))
        self.show()
    def showDialog(self):
        '''打开文件'''
        fname=QFileDialog.getOpenFileName(self,'Open file','')
        if fname and fname[0]!='':
            if fname[0].split('.')[-1]=='docx':
                file = docx.Document(fname[0])
                # print("段落数:" + str(len(file.paragraphs)))  # 段落数为13，每个回车隔离一段
                s = ''
                for para in file.paragraphs:
                    if para.text.split(':')[0] == '段落数':
                        para.text = ''
                    s += para.text + '\n'
                self.textEdit.setText(s)
            else:
                f=open(fname[0],'r',encoding='utf-8')
                with f:
                    data=f.read()
                    self.textEdit.setText(data)

    def showDialog_Box(self):
        '''打开文件夹'''
        filename = QFileDialog.getExistingDirectory(self, directory='')
        if filename and filename[0] != '':
            self.textEdit.setText(filename)

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
