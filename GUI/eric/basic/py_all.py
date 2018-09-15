# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
import sys
from PyQt5.QtWidgets import QApplication, QWidget,\
    QToolTip,QPushButton,QMessageBox,QDesktopWidget,QLabel
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,\
    QGridLayout,QTextEdit,QLineEdit,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon ,QFont#图标,字体
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider,QLCDNumber
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # ---------------------按钮和窗体鼠标放上去显示提示信息
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        # QToolTip.setFont(QFont('SansSerif', 10))
        # # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        # self.setToolTip('This is a <b>QWidget</b> widget')
        # # 创建一个PushButton并为他设置一个tooltip
        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # # btn.sizeHint()显示默认尺寸
        # btn.resize(btn.sizeHint())
        # btn.move(50,50)

        # ------------------退出按钮
        # qtbn=QPushButton('quit',self)
        # qtbn.clicked.connect(QCoreApplication.instance().quit)
        # qtbn.resize(qtbn.sizeHint())
        # qtbn.move(80,80)

        #绝对定位  ---------标签
        # lbl1=QLabel('Zetcode',self)
        # lbl1.move(10,10)
        # lbl2=QLabel('tutorials',self)
        # lbl2.move(10,20)
        # lbl3=QLabel('for programers',self)
        # lbl3.move(10,30)
        #框布局---------确定和取消按钮
        # okbutton=QPushButton('ok')
        # canclebutton=QPushButton('cancel')
        #     # 水平布局 添加一个伸展因子和两个按钮
        # hbox=QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okbutton)
        # hbox.addWidget(canclebutton)
        #     # 垂直布局
        # vbox=QVBoxLayout()
        # vbox.addStretch(1)#添加伸展因子
        # vbox.addLayout(hbox)
            #设置窗口的布局界面
        # self.setLayout(vbox)

        #表格布局qgridlayout------计算器实例
        # grid=QGridLayout()
        # self.setLayout(grid)
        # names=['Cls','Bck','','Close',
        #        '7', '8', '9', '/',
        #        '4', '5', '6', '*',
        #        '1', '2', '3', '-',
        #        '0', '.', '=', '+']
        # positons=[(i,j) for i in range(5) for j in range(4)]
        # for positon,name in zip(positons,names):
        #     if name=='':
        #         continue
        #     button=QPushButton(name)
        #     grid.addWidget(button,*positon)

        # -----------------------------评论
        # title=QLabel('Title')

        # author=QLabel('Author')
        # review=QLabel('Review')
        #
        # titleEdit=QLineEdit()
        # authorEdit=QLineEdit()
        # reviewEdit=QLineEdit()
        #
        # grid=QGridLayout()#创建方格布局
        # grid.setSpacing(10)#设置每行空白间隔
        #
        # grid.addWidget(title,1,0)
        # grid.addWidget(titleEdit,1,1)
        #
        # grid.addWidget(author,2,0)
        # grid.addWidget(authorEdit,2,1)
        #
        # grid.addWidget(review,3,0)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)#reviewEdit控件跨度5行
        #
        # self.setLayout(grid)

        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction=QAction(QIcon('class.png'),'&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')#提示信息
        exitAction.triggered.connect(self.close)

        self.statusBar()
        menubar=self.menuBar()
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(exitAction)


        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)



        self.setGeometry(300,300,300,220)#x,y,w,h
        # self.center()#居中显示
        # self.statusBar().showMessage('Ready')#状态栏
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()
    def closeEvent(self, event):
        reply=QMessageBox.question(self,'Message','Are you sure to quit?',
                                   QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


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
