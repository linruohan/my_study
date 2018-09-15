from PyQt5 import QtCore, QtWidgets, QtSql
import sys
#添加和删除记录
def addRecord ():
    # 插入空记录，用户可手动输入
    stm.insertRow (stm.rowCount ())

def delRecord ():
    # 从模型中删除记录
    stm.removeRow (tv.currentIndex (). row ())
    # 重新加载数据到模型中
    stm.select ()

app = QtWidgets.QApplication (sys.argv)
window = QtWidgets.QWidget ()
window.setWindowTitle ("QSqlTableModel")
# Establish a connection to the database
# 创建数据库连接
con = QtSql.QSqlDatabase.addDatabase('QMYSQL')
con.setHostName("127.0.0.1")
con.setDatabaseName("itis")
con.setUserName("root")
con.setPassword("123456")
con.open()
# Create a model
stm = QtSql.QSqlTableModel (parent = window)
stm.setTable ('jc_violist')
stm.setSort (1, QtCore.Qt.AscendingOrder)
stm.select ()
# Set the headers for the columns of the model
stm.setHeaderData (1, QtCore.Qt.Horizontal, 'id')
stm.setHeaderData (2, QtCore.Qt.Horizontal, 'Qty')
# Set the table just created for the table
vbox = QtWidgets.QVBoxLayout ()
tv = QtWidgets.QTableView ()
tv.setModel (stm)
# 隐藏第一列
tv.hideColumn (0)
tv.setColumnWidth (1, 150)
tv.setColumnWidth (2, 60)
vbox.addWidget (tv)
btnAdd = QtWidgets.QPushButton ("添加记录(&A)")
btnAdd.clicked.connect (addRecord)
vbox.addWidget (btnAdd)
btnDel = QtWidgets.QPushButton ("删除记录(&A")
btnDel.clicked.connect (delRecord)
vbox.addWidget (btnDel)
window.setLayout (vbox)
window.resize (300, 250)
window.show ()
sys.exit (app.exec_ ())