from PyQt5 import QtWidgets, QtSql
import sys
# #创建一个应用程序对象，否则数据库支持将不起作用
app = QtWidgets.QApplication(sys.argv)

#打开SQLite数据库
# con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
# con1.setDatabaseName('c：//work//data.sqlite')
# con1.open()
# con1.close()

#打开MySQL数据库
con2 = QtSql.QSqlDatabase.addDatabase('QMYSQL')
con2.setHostName("127.0.0.1")
con2.setDatabaseName("itis")
con2.setUserName("root")
con2.setPassword("123456")
con2.open()
if con2.isOpen:
    print(con2.connectionName())
    print(con2.tables ())
    # print(con2.record ("jc_acquisition").count())
    # print(con2.record ("jc_acquisition").fieldName(1))
    # print(con2.record ("jc_acquisition").field(1))
    # print(con2.record ("jc_acquisition").indexOf("site_id"))
    # print(con2.record ("jc_acquisition").contains("site_id"))
    # print(con2.record ("jc_acquisition").isEmpty())
    # print(con2.record ("jc_acquisition").field(1).name())
    # print(con2.record ("jc_acquisition").field(1).type())
    # print(con2.record ("jc_acquisition").field(1).length())
    # print(con2.record ("jc_acquisition").field(1).precision())
    # print(con2.record ("jc_acquisition").field(1).defaultValue())
    # print(con2.record ("jc_acquisition").field(1).requiredStatus())
    # print(con2.record ("jc_acquisition").field(1).isAutoValue())
    # print(con2.record ("jc_acquisition").field(1).isReadOnly())
    q=QtSql.QSqlQuery()
    q.prepare("select * from jc_violist")
    q.setForwardOnly(True)
    q.exec_()
    lst = []
    if q.isActive():
        print("数据条数为：%s 条"%q.size())
        q.first()
        q.finish()
        # while q.isValid():
        #     lst.append(q.value('id') + ': ' + str(q.value('car_num')) + '')
        #     q.next()
        # for p in lst: print(p)
    #清空查询的结果
    q.finish()
    q.exec("select count(*) as cnt from jc_violist")

    #开始新的查询
    if q.isActive():
        q.first()
        print("数据条数为：%s 条" % q.value("cnt"))
con2.close()

#通过ODBC打开Access数据库
# con3 = QtSql.QSqlDatabase.addDatabase("QODBC")
# con3.setDatabaseName("DRIVER = {Microsoft Access Driver(* .mdb)}"
#                      "FIL = {MS Access} "
#                      "DBQ = c：/work/data.mdb")
# con3.open()
# con3.close()