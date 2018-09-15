import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import (QDate, QDateTime, QFile, QVariant, Qt)
from PyQt5.QtWidgets import (QApplication, QDataWidgetMapper,QComboBox,
                             QDateTimeEdit, QDialog, QGridLayout, QHBoxLayout, QLabel,
                             QLineEdit, QMessageBox, QPushButton, QVBoxLayout)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlRelation,
        QSqlRelationalDelegate, QSqlRelationalTableModel)


DATETIME_FORMAT = "yyyy-MM-dd hh:mm"

class PhoneLogDlg(QDialog):

    FIRST, PREV, NEXT, LAST = range(4)

    def __init__(self, parent=None):
        super(PhoneLogDlg, self).__init__(parent)

        callerLabel = QLabel("&Caller:")
        self.callerEdit = QLineEdit()
        callerLabel.setBuddy(self.callerEdit)
        today = QDate.currentDate()
        startLabel = QLabel("&Start:")
        self.startDateTime = QDateTimeEdit()
        startLabel.setBuddy(self.startDateTime)
        self.startDateTime.setDateRange(today, today)
        self.startDateTime.setDisplayFormat(DATETIME_FORMAT)
        endLabel = QLabel("&End:")
        self.endDateTime = QDateTimeEdit()
        endLabel.setBuddy(self.endDateTime)
        self.endDateTime.setDateRange(today, today)
        self.endDateTime.setDisplayFormat(DATETIME_FORMAT)
        topicLabel = QLabel("&Topic:")
        topicEdit = QLineEdit()
        topicLabel.setBuddy(topicEdit)
        outcomeLabel = QLabel("&Outcome:")
        self.outcomeComboBox = QComboBox()
        outcomeLabel.setBuddy(self.outcomeComboBox)
        firstButton = QPushButton("第一条")
        prevButton = QPushButton("前一条")
        nextButton = QPushButton("后一条")
        lastButton = QPushButton("最后一条")
        adon = QPushButton("&Add")
        deleteButton = QPushButton("&Delete")
        quitButton = QPushButton("&Quit")
        adon.setFocusPolicy(Qt.NoFocus)
        deleteButton.setFocusPolicy(Qt.NoFocus)

        fieldLayout = QGridLayout()
        fieldLayout.addWidget(callerLabel, 0, 0)
        fieldLayout.addWidget(self.callerEdit, 0, 1, 1, 3)
        fieldLayout.addWidget(startLabel, 1, 0)
        fieldLayout.addWidget(self.startDateTime, 1, 1)
        fieldLayout.addWidget(endLabel, 1, 2)
        fieldLayout.addWidget(self.endDateTime, 1, 3)
        fieldLayout.addWidget(topicLabel, 2, 0)
        fieldLayout.addWidget(topicEdit, 2, 1, 1, 3)
        fieldLayout.addWidget(outcomeLabel, 3, 0)
        fieldLayout.addWidget(self.outcomeComboBox, 3, 1, 1, 3)
        navigationLayout = QHBoxLayout()
        navigationLayout.addWidget(firstButton)
        navigationLayout.addWidget(prevButton)
        navigationLayout.addWidget(nextButton)
        navigationLayout.addWidget(lastButton)
        fieldLayout.addLayout(navigationLayout, 4, 0, 1, 2)
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(adon)
        buttonLayout.addWidget(deleteButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(quitButton)
        layout = QHBoxLayout()
        layout.addLayout(fieldLayout)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("jc_violist")
        self.model.setRelation(5,
                QSqlRelation("jc_diction", "name", "name"))
        self.model.setSort(2, Qt.AscendingOrder)
        self.model.select()

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.callerEdit, 1)
        self.mapper.addMapping(self.startDateTime, 2)
        self.mapper.addMapping(self.endDateTime, 3)
        self.mapper.addMapping(topicEdit, 4)
        relationModel = self.model.relationModel(5)
        self.outcomeComboBox.setModel(relationModel)
        self.outcomeComboBox.setModelColumn(relationModel.fieldIndex("name"))
        self.mapper.addMapping(self.outcomeComboBox, 5)
        self.mapper.toFirst()

        firstButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.FIRST))
        prevButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.PREV))
        nextButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.NEXT))
        lastButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.LAST))
        adon.clicked.connect(self.addRecord)
        deleteButton.clicked.connect(self.deleteRecord)
        quitButton.clicked.connect(self.done)
        self.setWindowTitle("Phone Log")


    def done(self, result=None):
        self.mapper.submit()
        QDialog.done(self, True)


    def addRecord(self):
        row = self.model.rowCount()
        self.mapper.submit()
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        now = QDateTime.currentDateTime()
        self.startDateTime.setDateTime(now)
        self.endDateTime.setDateTime(now)
        self.outcomeComboBox.setCurrentIndex(
                self.outcomeComboBox.findText("Unresolved"))
        self.callerEdit.setFocus()


    def deleteRecord(self):
        caller = self.callerEdit.text()
        starttime = self.startDateTime.dateTime().toString(
                                            DATETIME_FORMAT)
        if (QMessageBox.question(self,
                "Delete",
                "Delete call made by{0}on{1}?".format(caller,starttime),
                QMessageBox.Yes|QMessageBox.No) ==QMessageBox.No):
            return
        row = self.mapper.currentIndex()
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()
        if row + 1 >= self.model.rowCount():
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)


    def saveRecord(self, where):
        row = self.mapper.currentIndex()
        self.mapper.submit()
        if where == PhoneLogDlg.FIRST:
            row = 0
        elif where == PhoneLogDlg.PREV:
            row = 0 if row <= 1 else row - 1
        elif where == PhoneLogDlg.NEXT:
            row += 1
            if row >= self.model.rowCount():
                row = self.model.rowCount() - 1
        elif where == PhoneLogDlg.LAST:
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)


def main():
    app = QApplication(sys.argv)
    # 创建数据库连接
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName("127.0.0.1")
    db.setDatabaseName("itis")
    db.setUserName("root")
    db.setPassword("123456")
    if not db.open():
        QMessageBox.warning(None, "Phone Log",("Database Error: {1}").format(db.lastError().text()))
        sys.exit(1)

    form = PhoneLogDlg()
    form.show()
    sys.exit(app.exec_())

main()