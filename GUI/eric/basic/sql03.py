from PyQt5 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QRelationalSqlTableModel")
# 创建数据库连接
con = QtSql.QSqlDatabase.addDatabase('QMYSQL')
con.setHostName("127.0.0.1")
con.setDatabaseName("itis")
con.setUserName("root")
con.setPassword("123456")
con.open()
stm = QtSql.QSqlRelationalTableModel(parent = window)
stm.setTable('jc_violist')
stm.setSort(2, QtCore.Qt.AscendingOrder)
#将good表中的category字段设置为到category表的链接
stm.setRelation(7, QtSql.QSqlRelation('jc_dictionary', 'name', 'name'))
stm.select()
# stm.setHeaderData(1, QtCore.Qt.Horizontal, '名称')
# stm.setHeaderData(2, QtCore.Qt.Horizontal, '数量')
# stm.setHeaderData(3, QtCore.Qt.Horizontal, '类别')
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
# tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
tv.setColumnWidth(3, 150)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("添加记录(&A)")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("删除记录(&A)")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(430, 250)
window.show()
sys.exit(app.exec_())