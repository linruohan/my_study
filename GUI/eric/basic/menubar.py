# QMainWindow + QtabWidget
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QApplication
class Example(QMainWindow):
    '''QtabWidget 实现 菜单栏 和 标签'''
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        #添加菜单栏
        menuBar = self.menuBar()
        toolBar=self.toolTip()
        # 添加菜单
        orderMenu = QMenu("订货管理", self)
        filemenu = QMenu('&File', self)
        menuBar.addMenu(orderMenu)
        menuBar.addMenu(filemenu)
        # 添加分割线
        orderMenu.addSeparator()
        #添加功能
        action1 = QAction("文件管理", self, enabled=True,
                          checkable=True, shortcut="Ctrl+F", triggered=self.triggerFun)
        order_action = QAction("供应商订货", self, enabled=True,
                          checkable=True, shortcut="Ctrl+O", triggered=self.triggerFun)
        orderMenu.addAction(order_action)
        filemenu.addAction(action1)


        tabWidget = QTabWidget(self)
        # QMainWindow.setCentralWidget函数一旦被注释,出现的界面很怪异的
        self.setCentralWidget(tabWidget)
        # tabWidget上出现关闭的叉号,但是点击标签的关闭叉号并不会关闭对应的标签页
        # 而是会触发 void    tabCloseRequested(int index) 的Signals
        # 如果想要在点击关闭的叉号后对应的标签页会关闭,需要执行 tabWidget.removeTab(int index)
        # tabWidget.tabCloseRequested.connect(tabWidget.removeTab)
        tabWidget.setTabsClosable(True)
        tabWidget.tabCloseRequested.connect(tabWidget.removeTab)
    def triggerFun(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
