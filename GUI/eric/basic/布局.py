from PyQt5.QtWidgets import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5布局示例')
        # 全局布局（注意参数 self）
        wl = QVBoxLayout(self)
        # 局部布局
        vl = QVBoxLayout()
        hl = QHBoxLayout()
        gl = QGridLayout()
        # 这里向局部布局内添加部件
        hl.addWidget(QPushButton('1'))
        hl.addWidget(QPushButton('2'))
        vl.addWidget(QPushButton('3'))
        vl.addWidget(QPushButton('4'))
        vl.addWidget(QPushButton('5'))
        gl.addWidget(QPushButton('6'), 0, 0)
        gl.addWidget(QPushButton('7'), 0, 1)
        gl.addWidget(QPushButton('8'), 1, 0)
        gl.addWidget(QPushButton('9'), 1, 1)

        # 加到全局布局
        wl.addLayout(hl)
        wl.addLayout(vl)
        wl.addLayout(gl)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())