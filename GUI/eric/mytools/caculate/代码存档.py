from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.animation as animation
import threading
import numpy as np


# 动作
class MyQAction(QAction):
    def __init__(self, parent, text='', triggered=None, shortcut=None, icon=None, tip=None, checkable=False):
        super().__init__(parent)
        self.setText(text)
        if icon is not None:
            self.setIcon(QIcon("ico/%s.ico" % icon))
        if shortcut is not None:
            self.setShortcut(shortcut)
        if tip is not None:
            # self.setToolTip(tip)
            self.setStatusTip(tip)
        if triggered is not None:
            self.triggered.connect(triggered)
        if checkable:
            self.setCheckable(True)

# Canvas
class mainGraphCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure((width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(self.fig)
    def plot(self, fig):
        pass


# 界面
class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(1234, 669)
        Form.setWindowTitle("彩票助手")
        frame = QFrame()
        # frame.setPalette(QPalette(Qt.blue)) ################################ 蓝色
        layout = QHBoxLayout(frame)
        # layout.setContentsMargins(2,2,2,2)
        # =========================================================
        # 左侧TabWidget
        # =========================================================
        toolbox = QToolBox()
        toolbox.addItem(QFrame(), "图")
        toolbox.addItem(QFrame(), "表")
        toolbox.addItem(QFrame(), "数")
        # toolbox.setFixedWidth(150)
        groupbox = QGroupBox()
        groupbox.setFixedWidth(150)
        vlayout = QVBoxLayout(groupbox)
        vlayout.setContentsMargins(2, 2, 2, 2)
        # vlayout.setAlignment(Qt.AlignCenter)
        vlayout.addWidget(toolbox)
        tab = QTabWidget()
        tab.addTab(groupbox, '正常')
        tab.addTab(QFrame(), '其他')
        # =========================================================
        # 右侧TabWidget
        # =========================================================
        stack = QStackedWidget()
        # 页面1
        page1 = QTableWidget(6, 4)
        page1.setHorizontalHeaderLabels(['This', 'is', 'a', 'TableWidget!'])
        page1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 表宽度自适应
        # self.page1.resizeColumnsToContents()# 列宽度自适应
        for i in range(page1.rowCount()):
            for j in range(page1.columnCount()):
                page1.setItem(i, j, QTableWidgetItem('(%d,%d)' % (i, j)))
        stack.addWidget(page1)

        # 页面2
        page2 = mainGraphCanvas(stack)
        stack.addWidget(page2)

        # 页面3
        page3 = QTextEdit()
        stack.addWidget(page3)

        layout.addWidget(tab)
        layout.addWidget(stack)

        toolbox.currentChanged.connect(stack.setCurrentIndex)

        Form.setCentralWidget(frame)  # 设置居中

        # =================================================
        # # 动作
        # =================================================
        # 数据
        self.update_action = MyQAction(Form, "更新", triggered=qApp.quit, shortcut="Ctrl+U", icon="update", tip='？？')
        self.view_action = MyQAction(Form, "查看", triggered=qApp.quit, shortcut="Ctrl+V", icon="view", tip='？？')
        self.exit_action = MyQAction(Form, "退出", triggered=qApp.quit, shortcut="Ctrl+Q", tip='？？')
        # 指标
        self.tema_action = MyQAction(Form, "特码", triggered=qApp.quit, icon="tema", tip='？？')
        self.pingte_action = MyQAction(Form, "平特", triggered=qApp.quit, icon="pingte", tip='？？')
        self.formula_action = MyQAction(Form, "公式", triggered=qApp.quit, shortcut="Ctrl+F", icon="formula", tip='？？')
        self.setup_action = MyQAction(Form, "设置", triggered=qApp.quit, shortcut="Ctrl+S", icon="setup", tip='？？')
        # 图表
        self.kline_action = MyQAction(Form, "K 线", triggered=qApp.quit, shortcut="Ctrl+K", icon="kline", tip='？？')
        self.tline_action = MyQAction(Form, "T 线", triggered=qApp.quit, shortcut="Ctrl+T", icon="tline", tip='？？')
        self.pie_action = MyQAction(Form, "饼图", triggered=qApp.quit, shortcut="Ctrl+P", icon="pie", tip='？？')
        # 预测
        self.bpnn_action = MyQAction(Form, "神经网络", triggered=qApp.quit, shortcut="Ctrl+N", icon="bpnn", tip='？？')
        self.svm_action = MyQAction(Form, "支持向量机", triggered=qApp.quit, icon="svm", tip='？？')
        self.randomforest_action = MyQAction(Form, "随机森林", triggered=qApp.quit, icon="randomforest", tip='？？')
        self.embled_action = MyQAction(Form, "集成", triggered=qApp.quit, shortcut="Ctrl+E", icon="embled", tip='？？')
        # 回测
        self.policy_action = MyQAction(Form, "策略", triggered=qApp.quit, icon="policy", tip='？？')
        self.skill_action = MyQAction(Form, "技术", triggered=qApp.quit, icon="skill", tip='？？')
        self.scheme_action = MyQAction(Form, "方案", triggered=qApp.quit, icon="scheme", tip='？？')
        self.fund_action = MyQAction(Form, "资金", triggered=qApp.quit, icon="fund", tip='？？')
        # 选号
        self.indexpool_action = MyQAction(Form, "根据指标池", triggered=qApp.quit, shortcut="Ctrl+O", icon="indexpool",
                                          tip='？？')
        self.indexcustom_action = MyQAction(Form, "根据自定义指标", triggered=qApp.quit, icon="indexcustom", tip='？？')
        self.interunion_action = MyQAction(Form, "交集并集", triggered=qApp.quit, shortcut="Ctrl+I", icon="interunion",
                                           tip='？？')
        self.other_action = MyQAction(Form, "其他", triggered=qApp.quit, icon="other", tip='？？')
        # 统计
        self.limit_action = MyQAction(Form, "极限", triggered=qApp.quit, shortcut="Ctrl+L", icon="limit", tip='？？')
        self.custom_action = MyQAction(Form, "自定义", triggered=qApp.quit, icon="custom", tip='？？')
        # 帮助
        self.manual_action = MyQAction(Form, "手册", triggered=qApp.quit, icon="manual", tip='？？')
        self.author_action = MyQAction(Form, "作者", triggered=qApp.quit, icon="author", tip='？？')
        self.about_action = MyQAction(Form, "关于", triggered=qApp.quit, icon="about", tip='？？')

        # =================================================
        # 状态栏
        # =================================================
        # Form.statusBar()

        # =================================================
        # 菜单栏
        # =================================================
        # menubar = QMenuBar(self)
        menubar = Form.menuBar()
        menu = menubar.addMenu("数据(&D)")
        menu.addAction(self.update_action)
        menu.addAction(self.view_action)
        menu.addSeparator()
        menu.addAction(self.exit_action)

        menu = menubar.addMenu("指标(&I)")
        menu.addAction(self.tema_action)
        menu.addAction(self.pingte_action)
        menu.addAction(self.formula_action)
        menu.addAction(self.setup_action)

        menu = menubar.addMenu("图表(&C)")
        menu.addAction(self.kline_action)
        menu.addAction(self.tline_action)
        menu.addAction(self.pie_action)

        menu = menubar.addMenu("预测(&P)")
        menu.addAction(self.bpnn_action)
        menu.addAction(self.svm_action)
        menu.addAction(self.randomforest_action)
        menu.addAction(self.embled_action)

        menu = menubar.addMenu("回测(&B)")
        menu.addAction(self.policy_action)
        menu.addAction(self.skill_action)
        menu.addAction(self.scheme_action)
        menu.addAction(self.fund_action)

        menu = menubar.addMenu("统计(&S)")
        menu.addAction(self.limit_action)
        menu.addAction(self.custom_action)

        menu = menubar.addMenu("选号(&X)")
        menu.addAction(self.indexpool_action)
        menu.addAction(self.indexcustom_action)
        menu.addAction(self.interunion_action)
        menu.addAction(self.other_action)

        menu = menubar.addMenu("帮助(&H)")
        menu.addAction(self.manual_action)
        menu.addAction(self.author_action)
        menu.addAction(self.about_action)

        # =================================================
        # 工具栏
        # =================================================
        toolbar = Form.addToolBar('文件')
        toolbar.addAction(self.update_action)
        toolbar.addAction(self.view_action)
        toolbar.addSeparator()
        toolbar.addAction(self.tema_action)

        toolbar = Form.addToolBar("编辑")
        toolbar.addAction(self.pingte_action)
        toolbar.addAction(self.formula_action)

        toolbar.addAction(self.kline_action)
        toolbar.addAction(self.tline_action)
        toolbar.addAction(self.pie_action)

        toolbar.addAction(self.bpnn_action)
        toolbar.addAction(self.svm_action)
        toolbar.addAction(self.randomforest_action)
        toolbar.addAction(self.embled_action)

        toolbar.addAction(self.policy_action)
        toolbar.addAction(self.skill_action)
        toolbar.addAction(self.scheme_action)
        toolbar.addAction(self.fund_action)

        toolbar.addAction(self.indexpool_action)

        toolbar.addAction(self.limit_action)

    # 打包进线程（耗时的操作）
    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)  # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()  # 启动
        # t.join()          # 阻塞--会卡死界面！


# 方式一
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_Form()
        ui.setupUi(self)


# 方式二
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
