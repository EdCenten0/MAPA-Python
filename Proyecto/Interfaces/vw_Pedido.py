# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pedidos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing
#
# #Francisco de Jesus Melendez Simplina


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pedidos(object):
    def setupUi(self, Pedidos):
        Pedidos.setObjectName("Pedidos")
        Pedidos.resize(811, 600)
        Pedidos.setStyleSheet("background-color: rgb(63, 73, 100);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Pedidos)
        self.centralwidget.setObjectName("centralwidget")
        self.tb_Pedidos = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_Pedidos.setGeometry(QtCore.QRect(20, 320, 761, 251))
        self.tb_Pedidos.setObjectName("tb_Pedidos")
        self.tb_Pedidos.setColumnCount(5)
        self.tb_Pedidos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Pedidos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Pedidos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Pedidos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Pedidos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Pedidos.setHorizontalHeaderItem(4, item)
        self.tb_Pedidos.horizontalHeader().setDefaultSectionSize(151)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 31))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 30, 791, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.dt_pedido = QtWidgets.QDateEdit(self.centralwidget)
        self.dt_pedido.setGeometry(QtCore.QRect(470, 60, 111, 22))
        self.dt_pedido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dt_pedido.setObjectName("dt_pedido")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.line_Id = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Id.setEnabled(False)
        self.line_Id.setGeometry(QtCore.QRect(120, 64, 81, 21))
        self.line_Id.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Id.setObjectName("line_Id")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 71, 21))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.line_Nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Nombre.setEnabled(True)
        self.line_Nombre.setGeometry(QtCore.QRect(120, 140, 461, 25))
        self.line_Nombre.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Nombre.setObjectName("line_Nombre")
        self.line_Descripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.line_Descripcion.setGeometry(QtCore.QRect(120, 190, 461, 101))
        self.line_Descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Descripcion.setObjectName("line_Descripcion")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 91, 21))
        self.label_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 60, 131, 21))
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.bt_Guardar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Guardar.setGeometry(QtCore.QRect(630, 50, 141, 41))
        self.bt_Guardar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_Guardar.setObjectName("bt_Guardar")
        self.bt_Eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Eliminar.setGeometry(QtCore.QRect(630, 190, 141, 41))
        self.bt_Eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_Eliminar.setObjectName("bt_Eliminar")
        self.bt_Editar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Editar.setGeometry(QtCore.QRect(630, 120, 141, 41))
        self.bt_Editar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_Editar.setObjectName("bt_Editar")
        self.bt_Vaciar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Vaciar.setGeometry(QtCore.QRect(630, 260, 141, 41))
        self.bt_Vaciar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_Vaciar.setObjectName("bt_Vaciar")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.cb_cliente = QtWidgets.QComboBox(self.centralwidget)
        self.cb_cliente.setGeometry(QtCore.QRect(120, 100, 181, 22))
        self.cb_cliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_cliente.setObjectName("cb_cliente")
        Pedidos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Pedidos)
        self.statusbar.setObjectName("statusbar")
        Pedidos.setStatusBar(self.statusbar)

        self.retranslateUi(Pedidos)
        QtCore.QMetaObject.connectSlotsByName(Pedidos)

    def retranslateUi(self, Pedidos):
        _translate = QtCore.QCoreApplication.translate
        Pedidos.setWindowTitle(_translate("Pedidos", "Pedidos"))
        item = self.tb_Pedidos.horizontalHeaderItem(0)
        item.setText(_translate("Pedidos", "ID"))
        item = self.tb_Pedidos.horizontalHeaderItem(1)
        item.setText(_translate("Pedidos", "ID_Cliente"))
        item = self.tb_Pedidos.horizontalHeaderItem(2)
        item.setText(_translate("Pedidos", "Nombre"))
        item = self.tb_Pedidos.horizontalHeaderItem(3)
        item.setText(_translate("Pedidos", "Fecha del Pedido"))
        item = self.tb_Pedidos.horizontalHeaderItem(4)
        item.setText(_translate("Pedidos", "Descripcion"))
        self.label.setText(_translate("Pedidos", "Pedidos"))
        self.label_6.setText(_translate("Pedidos", "ID:"))
        self.label_7.setText(_translate("Pedidos", "Nombre:"))
        self.label_8.setText(_translate("Pedidos", "Descripción:"))
        self.label_9.setText(_translate("Pedidos", "Fecha del pedido:"))
        self.bt_Guardar.setText(_translate("Pedidos", "Guardar"))
        self.bt_Eliminar.setText(_translate("Pedidos", "Eliminar"))
        self.bt_Editar.setText(_translate("Pedidos", "Editar"))
        self.bt_Vaciar.setText(_translate("Pedidos", "Vaciar Campos"))
        self.label_10.setText(_translate("Pedidos", "Cliente:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pedidos = QtWidgets.QMainWindow()
    ui = Ui_Pedidos()
    ui.setupUi(Pedidos)
    Pedidos.show()
    sys.exit(app.exec_())