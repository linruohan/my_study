#coding=utf-8
import sys,os,threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import webbrowser,docx,time
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.load_data(QSplashScreen(QPixmap("./img/fmale_male.gif")))  # 加载动画
        self.initUI()
        self.end()
    def load_data(self, sp):
        for i in range(1, 11):  # 模拟主程序加载过程
            time.sleep(0.1)  # 加载数据
            sp.showMessage("Onloading... {0}%".format(i * 10), Qt.AlignRight | Qt.AlignBottom, Qt.black)
            qApp.processEvents()  # 允许主进程处理事件
            sp.show()
    def end(self):
        # self.setFont(None)
        file = QFile('./css/css.qss')
        file.open(QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        self.setStyleSheet(styleSheet)
        self.statusBar()
        self.setGeometry(800, 300, 600, 400)  # x,y,w,h
        self.setWindowTitle('水寒是')
        self.setWindowIcon(QIcon('./ico/bug.ico'))
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
        self.mytimmer()
        self.vbox = QVBoxLayout(self)

        self.menutool()
        self.toolbar()
        self.dockwidget()
        self.H_V_buju()
        # self.mdi_area()
    def mytimmer(self):
        self.timer = QTimer()
        self.timer.start(1)
        self.timer.timeout.connect(self.flush)  # 使用了计时器
        '''
        创建计时器->设置1ms刷新间隔->每次刷新执行flush函数
        '''
    def menutool(self):
        #file
        openFile = self.addMenu1('./ico/read.ico', '打开文件', 'Ctrl+O', 'Open new File', self.showDialog)
        openFileBox = self.addMenu1('./ico/snake.ico', '打开文件夹', 'Ctrl+F', 'Open new Filebox', self.showDialog_Box)
        save = self.addMenu1('./ico/snake.ico', '保存', 'Ctrl+S', 'save the File', self.saveFile)
        saveas = self.addMenu1('./ico/snake.ico', '保存', 'Ctrl+S', 'save the File', self.saveAsFile)
        exit = self.addMenu1('./ico/little_sanke.ico', '退出', 'Ctrl+X', 'close the window', QCoreApplication.instance().quit)
        #edit
        New = self.addMenu1('./ico/read.ico', 'New', 'Ctrl+N', '新建子窗口:create the window', self.mdi_new)
        cascade = self.addMenu1('./ico/snake.ico', 'cascade', 'Ctrl+M', '层叠子窗口:cascade the window', self.mdi_cascade)
        Tiled = self.addMenu1('./ico/little_sanke.ico', 'Tiled', 'Ctrl+P', '平铺子窗口:Tiled the window', self.mdi_tile)
        font = self.addMenu1('./ico/little_sanke.ico', 'font', 'Ctrl+P', 'setting the font', self.myFont)
        color = self.addMenu1('./ico/little_sanke.ico', 'color', 'Ctrl+P', 'setting the font', self.myColor)
        #tool
        lcd = self.addMenu1('./ico/little_sanke.ico', 'time', 'Ctrl+T', '显示时间:show the time', self.lcd_action)
        #Help
        about = self.addMenu1('./ico/little_sanke.ico', '关于软件', 'Ctrl+I', '本软件相关信息', self.about)

        self.addMenu0('File', (openFile, openFileBox, save,saveas, exit))
        self.addMenu0('Edit', (New,cascade, Tiled,font,color))
        self.addMenu0('Tools', (lcd))
        self.addMenu0('Window', ( openFileBox))
        self.addMenu0('Help?', (about))

    def toolbar(self):
        toolbar = self.addToolBar('文件')
        toolbar.addAction(QAction(QIcon("./ico/read.ico"), "新建", self, triggered=qApp.quit))  # 带图标，文字
        toolbar.addAction(QAction(QIcon("./ico/read.ico"), "打开", self, triggered=qApp.quit))
        toolbar.addSeparator()
        toolbar = self.addToolBar("编辑")
        toolbar.addAction(QAction("撤销", self, triggered=qApp.quit))  # 不带图标
        toolbar.addAction(QAction("剪切", self, triggered=qApp.quit))
    def H_V_buju(self):
        self.text=QTextEdit('123')
        self.lcd()
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.lcd)

    def dockwidget(self):
        # 创建可停靠的窗口
        self.items = QDockWidget("可停靠的窗口", self)

        # 在停靠窗口内添加QListWidget对象
        self.listWidget = QListWidget()
        for i in ("item1","item2","item3"):
            self.listWidget.addItem(i)

        self.items.setWidget(self.listWidget)
        # 是否将可停靠窗口置于浮动状态，默认是False，下面这句删掉不影响显示结果
        self.items.setFloating(False)
        # 将停靠窗口放在中央控件的右侧
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
    def mdi_area(self):
        # 创建MdiArea控件
        self.mdi = QMdiArea()
        self.mdi_count=0
        self.setCentralWidget(self.mdi)
    def mdi_new(self):
        # 选择“New”则新建一个子窗口并显示，每创建一个子窗口则子窗口名称数增加1
        self.mdi_count = self.mdi_count + 1
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("subwindow" + str(self.mdi_count))
        self.mdi.addSubWindow(sub)
        sub.show()
    def mdi_cascade(self):
        # 选择“cascade”则将创建的子窗口层叠显示
        self.mdi.cascadeSubWindows()
    def mdi_tile(self):
        # 选择“Tiled”则将创建的子窗口平铺显示
        self.mdi.tileSubWindows()

    def lcd(self):
        self.lcd = QLCDNumber(self.text)  # 设置数字类
        self.lcd.setDigitCount(8)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet("border: 0px solid green; color: white; background: black;")  # 设置显示的颜色样式
        self.lcd.setVisible(False)

    def lcd_action(self):
        self.lcd.setVisible(True)
    def flush(self):
        # 获取系统当前时间
        dateTime = QDateTime.currentDateTime()
        # 显示的内容
        self.lcd.display(dateTime.toString("yyyy-MM-dd HH:mm:ss"))

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
        content=""
        if filename and os.path.isdir(filename) and os.listdir(filename):
            list=os.listdir(filename)
            for i in range(0, len(list)):
                path = os.path.join(filename, list[i])
                if os.path.isfile(path):
                    content+=(list[i]+"\n")
            self.textEdit.setText(content)
    def saveFile(self):
        file_, ok = QFileDialog.getSaveFileName(self,
                                                "保存：",
                                                "C:/",
                                                "All Files (*);;Text Files (*.txt)")
    def saveAsFile(self):
        file_, ok = QFileDialog.getSaveFileName(self,
                                                "另存为：",
                                                "C:/",
                                                "All Files (*);;Text Files (*.txt)")
    def myFont(self):
        font, ok = QFontDialog.getFont()
    def myColor(self):
        color = QColorDialog.getColor(Qt.blue, self, "Select Color")
    def about(self):
        QMessageBox.about(self,
                                  "关于软件",
                                  "这是关于本软件的说明。")
    # def closeEvent(self, event):  # 关闭窗口触发以下事件
    #     reply = QMessageBox.question(self, '退出提示', '确定要退出吗?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()  # 接受关闭事件
    #     else:
    #         event.ignore()  # 忽略关闭事件
    # 打包进线程（耗时的操作）
    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()  # 启动
        # t.join()          # 阻塞--会卡死界面！
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())