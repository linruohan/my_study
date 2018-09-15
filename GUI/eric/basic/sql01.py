from PyQt5 import QtCore, QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
label=QtWidgets.QLabel("查询结果显示标题栏")
label.setAlignment(QtCore.Qt.AlignCenter)
vbox = QtWidgets.QVBoxLayout()
window = QtWidgets.QWidget()
tabel = QtWidgets.QTableView()

window.setWindowTitle("QSqlQueryModel")
# 创建数据库连接
con2 = QtSql.QSqlDatabase.addDatabase('QMYSQL')
con2.setHostName("127.0.0.1")
con2.setDatabaseName("itis")
con2.setUserName("root")
con2.setPassword("123456")
con2.open()
# 创建SQL模型
sqm = QtSql.QSqlQueryModel(parent = window)
sqm.setQuery('select * from jc_violist')
# 设置模型的标题栏
# sqm.setHeaderData(1, QtCore.Qt.Horizontal, '名字')
# sqm.setHeaderData(2, QtCore.Qt.Horizontal, '数量')
# 将查询结果与表组件关联
tabel.setModel(sqm)
#隐藏第一列
# window.hideColumn(0)
tabel.setRowHeight(1, 10)
# tabel.setColumnWidth(1, 10)
# tabel.setColumnWidth(2, 60)

vbox.addWidget(label)
vbox.addWidget(tabel)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())