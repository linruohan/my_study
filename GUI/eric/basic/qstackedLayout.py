#coding =utf-8
import sys
from PyQt5 import QtWidgets, QtCore

#多页面切换的布局，一次只能看到一个界面。
class MyWidget(QtWidgets.QWidget):
    def __init__(self, i=0):
        super().__init__()
        self.setWindowTitle('小部件 ' + str(i))
        # label = QtWidgets.QLabel('小部件' + str(i) + '可见')
        label = QtWidgets.QLabel( str(i) + '可见')
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(label)


class TeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('')
        layout = QtWidgets.QVBoxLayout(self)
        stack = QtWidgets.QStackedLayout()  # ② Layout
        list = QtWidgets.QListWidget(self)
        list.setDragEnabled(True)
        list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        layout.addWidget(list)
        layout.addLayout(stack)  # ② 对应 addLayout
        for i in range(10):
            stack.addWidget(MyWidget(i))
            list.addItem("小部件%s" %i)

        list.currentRowChanged.connect(stack.setCurrentIndex)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = TeWidget()
    # widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())