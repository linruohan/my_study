from PyQt5 import QtWidgets,QtCore
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()              # 父窗口
window.setWindowTitle("QHBoxLayout")
window.resize(300, 60)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
hbox = QtWidgets.QHBoxLayout()            # 创建容器
hbox.addWidget(button1)                   # 添加组件
hbox.addWidget(button2)
# hbox.setContentsMargins (20, 40, 20, 40)
m = QtCore.QMargins (4, 2, 4, 2)
hbox.setContentsMargins (m)
window.setLayout(hbox)                    # 指定父组件
window.show()
sys.exit(app.exec_())