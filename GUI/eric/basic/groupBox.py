from PyQt5 import QtWidgets,QtCore
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QGroupBox")
window.resize(200, 80)
mainbox = QtWidgets.QVBoxLayout()
label=QtWidgets.QLabel("&12312312")
radio1 = QtWidgets.QRadioButton("&Yes")
radio2 = QtWidgets.QRadioButton("&No")
radio3 = QtWidgets.QRadioButton("&what?")
fram=QtWidgets.QFrame()
fram.setFrameShape(5)
fram.setFrameShadow(0x020)
label.setFrameShape(fram.frameShape())

box = QtWidgets.QGroupBox("&Do you know Python?") # 创建QGroupBox
box.setCheckable(True)#有可用选择框
box.setChecked(True)#默认为选中
box.setFlat(True)#边框线显示，true为上边框显示，false为所有



hbox = QtWidgets.QHBoxLayout() # 放到box中的QHBoxLayout容器

hbox.addWidget(radio1)         # 添加要成组的组件radio1
hbox.addWidget(radio2)          # 添加要成组的组件radio2
hbox.addWidget(radio3)          # 添加要成组的组件radio3
hbox.addWidget(label)          # 添加要成组的组件radio3
box.setLayout(hbox)            # 将hbox布局到box
mainbox.addWidget(box)         # 将box添加到主窗口
window.setLayout(mainbox)      # 将mainbox布局到窗口
radio1.setChecked(True)        # 设置radio1为选中状态
window.show()
sys.exit(app.exec_())