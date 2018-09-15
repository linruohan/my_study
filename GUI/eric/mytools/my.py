#coding=utf-8
import sys,os,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
class DragButton(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
    def mouseMoveEvent(self,e):
        if e.buttons()!=Qt.LeftButton:
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
class MylineEdit(QLineEdit):
    def __init__(self,parrent=None):

        QLineEdit.__init__(self,parrent)
        self.id=None
    def focusInEvent(self, e):
        print("输入焦点在:",self.id)
        QLineEdit.focusInEvent(self,e)
    def focusOutEvent(self, e):
        print(self.id,"失去焦点了")
        QLineEdit.focusOutEvent(self, e)
    def event(self, e):
        if e.type()==QEvent.Shortcut:
            if self.id==e.shortcutid():
                self.setFocus(Qt.ShortcutFocusReason)
                return True
        return QLineEdit.event(self,e)
class MyFilter(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
    def eventFilter(self, obj, e):
        if e.type() == QEvent.KeyPress:
            if e.key() == Qt.Key_B:
                print("The event from the key will not reach the component")
                return True
        return QObject.eventFilter(self, obj, e)
class MyEvent(QEvent):
    idType = QEvent.registerEventType()
    def __init__(self, data):
        QEvent.__init__(self, MyEvent.idType)
        self.data = data
    def get_data(self):
        return self.data

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.load_data(QSplashScreen(QPixmap("img/fmale_male.gif")))#加载动画
        self.initUI()
        self.end()
    def load_data(self, sp):
        for i in range(1, 11):  # 模拟主程序加载过程
            time.sleep(0.1)  # 加载数据
            sp.showMessage("Onloading... {0}%".format(i * 10), Qt.AlignRight | Qt.AlignBottom, Qt.black)
            qApp.processEvents()  # 允许主进程处理事件
            sp.show()
    def end(self):
        self.setGeometry(800, 300, 600, 400)  # x,y,w,h
        self.setWindowTitle('水寒是')
        self.setWindowIcon(QIcon('./img/bug.ico'))
        self.show()
    def addMenu0(self,menuName,addMenu):
        fileMenu = self.menuBar().addMenu('&'+menuName)
        if isinstance(addMenu, tuple):
            for i in addMenu:
                fileMenu.addAction(i)
        else:
            fileMenu.addAction(addMenu)
        return fileMenu
    def addMenu1(self,icon,name,shotkey,tips,func):
        menu = QAction(QIcon(icon), name, self)
        menu.setShortcut(shotkey)
        menu.setStatusTip(tips)
        menu.triggered.connect(func)
        return menu
    def initUI(self):
        self.setAcceptDrops(True)
        # 拖拽
        data = QMimeData()
        data.setText("Drag text")
        drag = QDrag(self)
        drag.setMimeData(data)

        self.label = QLabel("(&E)使输入焦点移动到编辑框1")
        # 将MyEvent事件发送到标签控件的代码：
        QCoreApplication.sendEvent(self.label, MyEvent("512"))#自定义时间发送
        self.label1 = QLabel("横向layer I am 1.")
        # self.label.setAlignment(Qt.AlignHCenter)
        btnQuit = QPushButton("关闭窗口(&C)")
        self.btnQuit2 = DragButton('我是窗口(&C)',self)
        btnQuit1 = QPushButton("横向layer I am 1.")
        btnQuit.clicked.connect(qApp.quit)
        btnQuit1.clicked.connect(self.on_clicked)
        #timer
        self.timer_id = 0
        self.btn1 = QPushButton('开始')
        self.btn2 = QPushButton('停止')
        self.btn2.setEnabled(False)
        self.btn1.clicked.connect(self.onclick_btn1)#绑定事件
        self.btn2.clicked.connect(self.onclick_btn2)#绑定事件
        #editline 焦点切换
        self.line1 = MylineEdit()
        self.line2 = MylineEdit()
        # self.line2.installEventFilter(MyFilter(self.line2))#安装过滤器
        self.line2.removeEventFilter(MyFilter(self.line2))#移除过滤器，最后安装的过滤器最先执行

        self.label.setBuddy(self.line1)
        self.line2.id=self.line2.grabShortcut(QKeySequence.mnemonic("&D"))
        #获取焦点1
        self.btn3=QPushButton("(&R)删除编辑框1的输入焦点")
        self.btn3.clicked.connect(self.clearfocus)
        self.line3=QLineEdit()
        self.shc=QShortcut(QKeySequence.mnemonic("&M"),self)
        self.shc.setContext(Qt.WindowShortcut)
        self.shc.activated.connect(self.line2.setFocus)
        # 获取焦点2
        self.act=QAction()
        self.act.setShortcut(QKeySequence.mnemonic("&W"))
        self.act.triggered.connect(self.line2.setFocus)
        self.addAction(self.act)
        tab = QTabWidget()
        tab.addTab(QLabel("Tab Content 1"), "Tab & 1")
        tab.addTab(QLabel("Tab Content 2"), "Tab & 2")
        tab.addTab(QLabel("Tab Content 3"), "Tab & 3")
        tab.setCurrentIndex(0)

        toolBox = QToolBox()
        toolBox.addItem(QPushButton("工具 1"), QIcon('./img/bug.ico'),"工具页签 &1")
        toolBox.addItem(QLabel("工具 2"), QIcon('./img/bug.ico'),"工具页签 &2")
        toolBox.addItem(QLabel("工具 3"), QIcon('./img/bug.ico'), "工具页签 &3")
        # toolBox.setCurrentIndex(0)

        # splitter = QSplitter(Qt.Vertical)#垂直
        splitter = QSplitter(Qt.Horizontal)#水平
        label1 = QLabel("标签组件 1")
        label2 = QLabel("标签组件 2")
        label1.setFrameStyle(QFrame.Box | QFrame.Plain)
        label2.setFrameStyle(QFrame.Box | QFrame.Plain)
        splitter.addWidget(label1)
        splitter.addWidget(label2)
        # splitter.scroll(2,3)
        vbox = QVBoxLayout()
        hbox=QHBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(tab)#添加tab
        vbox.addWidget(toolBox)#添加工具盒
        vbox.addWidget(splitter)#添加大小可调整面板QSplitter类


        vbox.addWidget(self.line1)
        vbox.addWidget(self.line2)
        vbox.addWidget(self.line3)

        vbox.addWidget(btnQuit)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btnQuit2)


        hbox.addLayout(vbox)
        # 设置容器内组件的排列方式
        # (1)hbox.setContentsMargins (20, 40, 20, 40)
        m = QMargins(4, 2, 4, 2)
        hbox.setContentsMargins(m)
        # self.setLayout(vbox)#将vbox容器添加到窗口，同时成为window的对类对象。
        self.setLayout(hbox)#将hbox容器添加到窗口，同时成为window的对类对象。


        lineEdit = QLineEdit()
        textEdit = QTextEdit()
        button1 = QPushButton("&Send")
        button2 = QPushButton("&Clear")
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        form = QFormLayout(self)
        form.addRow("&Name:", lineEdit)
        form.addRow("&Description:", textEdit)
        form.addRow(hbox)
    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText("Received data: {0}".format(e.get_data()))
    def dragEnterEvent(self, e):
        e.accept()
    def dropEvent(self, e):
        position=e.pos()
        self.btnQuit2.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()
        self.setAcceptDrops(True)
    def on_clicked(self):
        self.line1.setFocus()#获取焦点
    def clearfocus(self):
        self.line1.clearFocus()#获取焦点
    def onclick_btn1(self):
        self.timer_id=self.startTimer(1000,timerType=Qt.VeryCoarseTimer)
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(True)
    def onclick_btn2(self):
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id=0
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(False)
    def timerEvent(self,event):
        self.label.setText(time.strftime("%H:%M:%S"))
    # def event(self, e):
    #     if e.type()==QEvent.KeyPress:
    #         print("按下键盘按键")
    #         print("ASCII码：",e.key,"字母：",e.text())
    #     elif e.type()==QEvent.Close:
    #         print("窗口关闭了")
    #     elif e.type()==QEvent.MouseButtonPress:
    #         print("点鼠标的坐标值：",e.x(),e.y())
    #     return QWidget.event(self,e)
    # def changeEvent(self, e):
    #     if e.type() == QEvent.WindowStateChange:
    #         if self.isMinimized():
    #             print("窗口最小化")
    #         elif self.isMaximized():
    #             print("窗口最大化")
    #         elif self.isFullScreen():
    #             print("全屏显示")
    #         elif self.isActiveWindow():
    #             print("活动窗口")
    #     QWidget.changeEvent(self, e)
    # def showEvent(self, e):
    #     print("窗口显示")
    #     QWidget.showEvent(self, e)
    # def hideEvent(self, e):
    #     print("窗口隐藏")
    #     QWidget.hideEvent(self, e)
    def enterEvent(self, e):
        self.line1.setCursor(Qt.ClosedHandCursor)
        self.line2.setCursor(Qt.WaitCursor)
        self.line3.setCursor(Qt.CrossCursor)
    # def leaveEvent(self, e):
    #     self.line1.setCursor(Qt.ArrowCursor)
    #     self.line2.setCursor(Qt.ForbiddenCursor)
    #     self.line3.setCursor(Qt.BitmapCursor)
    # def moveEvent(self, e):
    #     print("x = {0}; y = {1}".format(e.pos().x(), e.pos().y()))
    #     QWidget.moveEvent(self, e)
    # def resizeEvent(self, e):
    #     print("w = {0}; h = {1}".format(e.size().width(), e.size().height()))
    #     QWidget.resizeEvent(self, e)
    def closeEvent(self, e):
        result = QMessageBox.question(self,"关闭确认","你是否真的要关闭窗口?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if result == QMessageBox.Yes:
            e.accept()
            QWidget.closeEvent(self, e)
        else:e.ignore()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())