# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Factura.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("border-radius: 6px;\n"
"font-family:\"Inter\", sans-serif;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font-family:\"Inter\", sans-serif;\n"
"font-size:30px;\n"
"font-weight:500;")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(222, 221, 218);\n"
"    border:none;\n"
"}\n"
"QPushButton {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border:1px solid rgb(100,100,100);\n"
"    color:rgb(50,50,50);\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"\n"
"QLabel{\n"
"        font-weight:500;\n"
"}\n"
"\n"
"*{\n"
"        font-family:\"Inter\", sans-serif;\n"
"        \n"
"}\n"
"\n"
"QFrame{\n"
"        background-color: rgb(222, 221, 218);\n"
"        border-radius:10%;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    padding: 4px;\n"
"    border-radius: 6px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #3daee9;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    padding: 4px;\n"
"    border-radius: 6px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-color: #3daee9;\n"
"    outline: none;\n"
"}\n"
"\n"
"QTextEdit::hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("QLabel{\n"
"        font-weight:500;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setStyleSheet("font-weight:500;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setStyleSheet("font-weight:500;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setStyleSheet("font-weight:500;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setStyleSheet("font-weight:500;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setStyleSheet("font-weight:500;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setStyleSheet("font-weight:500;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_4)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 2, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border:1px solid rgb(100,100,100);\n"
"    color:rgb(50,50,50);\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border:1px solid rgb(100,100,100);\n"
"    color:rgb(50,50,50);\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border:1px solid rgb(100,100,100);\n"
"    color:rgb(50,50,50);\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border:1px solid rgb(100,100,100);\n"
"    color:rgb(50,50,50);\n"
"    padding: 8px 16px;\n"
"    border-radius: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.horizontalLayout.addWidget(self.frame_5)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setStyleSheet("QTableView QHeaderView::section {\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    background-color: lightgray;\n"
"    padding: 4px;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QTableView QScrollBar:vertical {\n"
"    width: 14px;\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background-color: gray;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-line:vertical,\n"
"QTableView QScrollBar::sub-line:vertical {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-page:vertical,\n"
"QTableView QScrollBar::sub-page:vertical {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableView QScrollBar:horizontal {\n"
"    height: 14px;\n"
"    background-color: lightgray;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal {\n"
"    background-color: gray;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-line:horizontal,\n"
"QTableView QScrollBar::sub-line:horizontal {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-page:horizontal,\n"
"QTableView QScrollBar::sub-page:horizontal {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_4.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Facturas"))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.label_3.setText(_translate("MainWindow", "Pedido:"))
        self.label_4.setText(_translate("MainWindow", "Mano de obra:"))
        self.label_5.setText(_translate("MainWindow", "Precio de materiales:"))
        self.label_7.setText(_translate("MainWindow", "Fecha:"))
        self.label_6.setText(_translate("MainWindow", "Precio Total:"))
        self.pushButton.setText(_translate("MainWindow", "Guardar Ventas"))
        self.pushButton_2.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_3.setText(_translate("MainWindow", "Vaciar Campos"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Factura ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Precio Material"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mano de obra"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio total"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pedido ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())