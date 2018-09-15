import sys
from PyQt5.QtWidgets import *

'''MDI(Multiple Document Interface, 多文档界面)应用程序占用较少的内存资源，
子窗口都可以放在主窗口容器(QMdiArea)中，QMdiArea通常占据在QMainWindow对象的中央位置，
子窗口在这个区域是QMdiSubWindow类的实例，
可以设置任何QWidget作为子窗口对象的内部控件，'''
class MainWindow(QMainWindow):
    count = 0
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 创建MdiArea控件
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # 创建菜单栏
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")

        # 当单机菜单控件时触发triggered信号，连接到槽函数windowaction()
        file.triggered.connect(self.windowaction)

        self.setWindowTitle("MDI demo")

    def windowaction(self, q):

        # 选择“New”则新建一个子窗口并显示，每创建一个子窗口则子窗口名称数增加1
        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow" + str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        # 选择“cascade”则将创建的子窗口层叠显示
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()

        # 选择“Tiled”则将创建的子窗口平铺显示
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())