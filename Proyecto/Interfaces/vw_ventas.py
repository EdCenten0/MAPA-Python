# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventas(object):
    def setupUi(self, Ventas):
        Ventas.setObjectName("Ventas")
        Ventas.resize(749, 447)
        self.centralwidget = QtWidgets.QWidget(Ventas)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
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
"\n"
"QLabel{\n"
"        font-weight:500;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line_Ventas_Id = QtWidgets.QLineEdit(self.frame)
        self.line_Ventas_Id.setEnabled(False)
        self.line_Ventas_Id.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Ventas_Id.setObjectName("line_Ventas_Id")
        self.gridLayout_5.addWidget(self.line_Ventas_Id, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font-size:15px;")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("font-size:15px;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.line_Ventas_Descripcion = QtWidgets.QLineEdit(self.frame)
        self.line_Ventas_Descripcion.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Ventas_Descripcion.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_Ventas_Descripcion.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_Ventas_Descripcion.setObjectName("line_Ventas_Descripcion")
        self.gridLayout_5.addWidget(self.line_Ventas_Descripcion, 2, 1, 1, 1)
        self.line_Ventas_Cantidad = QtWidgets.QLineEdit(self.frame)
        self.line_Ventas_Cantidad.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Ventas_Cantidad.setObjectName("line_Ventas_Cantidad")
        self.gridLayout_5.addWidget(self.line_Ventas_Cantidad, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("font-size:15px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font-size:15px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 1)
        self.line_Ventas_Nfactura = QtWidgets.QLineEdit(self.frame)
        self.line_Ventas_Nfactura.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Ventas_Nfactura.setObjectName("line_Ventas_Nfactura")
        self.gridLayout_5.addWidget(self.line_Ventas_Nfactura, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(63)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:15px;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 0, 1, 1)
        self.Ventas_idTienda_line = QtWidgets.QLineEdit(self.frame)
        self.Ventas_idTienda_line.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.Ventas_idTienda_line.setObjectName("Ventas_idTienda_line")
        self.gridLayout_5.addWidget(self.Ventas_idTienda_line, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tb_Ventas = QtWidgets.QTableWidget(self.frame)
        self.tb_Ventas.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tb_Ventas.setStyleSheet("QTableView QHeaderView::section {\n"
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
        self.tb_Ventas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Ventas.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_Ventas.setObjectName("tb_Ventas")
        self.tb_Ventas.setColumnCount(5)
        self.tb_Ventas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Ventas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Ventas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Ventas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Ventas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Ventas.setHorizontalHeaderItem(4, item)
        self.tb_Ventas.horizontalHeader().setDefaultSectionSize(111)
        self.tb_Ventas.horizontalHeader().setStretchLastSection(True)
        self.tb_Ventas.verticalHeader().setDefaultSectionSize(25)
        self.tb_Ventas.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_3.addWidget(self.tb_Ventas)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bt_Guardar_Ventas = QtWidgets.QPushButton(self.frame)
        self.bt_Guardar_Ventas.setStyleSheet("QPushButton {\n"
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
"}")
        self.bt_Guardar_Ventas.setObjectName("bt_Guardar_Ventas")
        self.verticalLayout_2.addWidget(self.bt_Guardar_Ventas)
        self.bt_Editar_Ventas = QtWidgets.QPushButton(self.frame)
        self.bt_Editar_Ventas.setStyleSheet("QPushButton {\n"
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
"}")
        self.bt_Editar_Ventas.setObjectName("bt_Editar_Ventas")
        self.verticalLayout_2.addWidget(self.bt_Editar_Ventas)
        self.bt_Eliminar_Ventas = QtWidgets.QPushButton(self.frame)
        self.bt_Eliminar_Ventas.setStyleSheet("QPushButton {\n"
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
"}")
        self.bt_Eliminar_Ventas.setObjectName("bt_Eliminar_Ventas")
        self.verticalLayout_2.addWidget(self.bt_Eliminar_Ventas)
        self.bt_Vaciar_Ventas = QtWidgets.QPushButton(self.frame)
        self.bt_Vaciar_Ventas.setStyleSheet("QPushButton {\n"
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
"}")
        self.bt_Vaciar_Ventas.setObjectName("bt_Vaciar_Ventas")
        self.verticalLayout_2.addWidget(self.bt_Vaciar_Ventas)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 7)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font-family:\"Inter\", sans-serif;\n"
"font-size:30px;\n"
"font-weight:500;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        Ventas.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ventas)
        QtCore.QMetaObject.connectSlotsByName(Ventas)

    def retranslateUi(self, Ventas):
        _translate = QtCore.QCoreApplication.translate
        Ventas.setWindowTitle(_translate("Ventas", "Ventas.ui"))
        self.label.setText(_translate("Ventas", "ID:"))
        self.label_3.setText(_translate("Ventas", "No. Factura"))
        self.label_4.setText(_translate("Ventas", "Descripcion:"))
        self.label_2.setText(_translate("Ventas", "Cantidad:"))
        self.label_5.setText(_translate("Ventas", "ID Tienda:"))
        item = self.tb_Ventas.horizontalHeaderItem(0)
        item.setText(_translate("Ventas", "ID"))
        item = self.tb_Ventas.horizontalHeaderItem(1)
        item.setText(_translate("Ventas", "ID Tienda"))
        item = self.tb_Ventas.horizontalHeaderItem(2)
        item.setText(_translate("Ventas", "Factura No."))
        item = self.tb_Ventas.horizontalHeaderItem(3)
        item.setText(_translate("Ventas", "Descripcion"))
        item = self.tb_Ventas.horizontalHeaderItem(4)
        item.setText(_translate("Ventas", "Cantidad"))
        self.bt_Guardar_Ventas.setText(_translate("Ventas", "Guardar"))
        self.bt_Editar_Ventas.setText(_translate("Ventas", "Editar"))
        self.bt_Eliminar_Ventas.setText(_translate("Ventas", "Eliminar"))
        self.bt_Vaciar_Ventas.setText(_translate("Ventas", "Vaciar Campos"))
        self.label_6.setText(_translate("Ventas", "Ventas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventas = QtWidgets.QMainWindow()
    ui = Ui_Ventas()
    ui.setupUi(Ventas)
    Ventas.show()
    sys.exit(app.exec_())
