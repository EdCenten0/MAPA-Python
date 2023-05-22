# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bodega.ui'
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
        MainWindow.setStyleSheet("background-color: rgb(11, 36, 71);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 801, 601))
        self.tabWidget.setMinimumSize(QtCore.QSize(22, 0))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.Bodega = QtWidgets.QWidget()
        self.Bodega.setObjectName("Bodega")
        self.tb_Bodega = QtWidgets.QTableWidget(self.Bodega)
        self.tb_Bodega.setGeometry(QtCore.QRect(10, 260, 791, 321))
        self.tb_Bodega.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tb_Bodega.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tb_Bodega.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Bodega.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_Bodega.setObjectName("tb_Bodega")
        self.tb_Bodega.setColumnCount(4)
        self.tb_Bodega.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Bodega.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Bodega.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Bodega.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Bodega.setHorizontalHeaderItem(3, item)
        self.tb_Bodega.horizontalHeader().setDefaultSectionSize(111)
        self.tb_Bodega.verticalHeader().setDefaultSectionSize(25)
        self.tb_Bodega.verticalHeader().setMinimumSectionSize(23)
        self.label = QtWidgets.QLabel(self.Bodega)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.label.setStyleSheet("font: 14pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Bodega)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 101, 21))
        self.label_2.setStyleSheet("font: 14pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Bodega)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.label_3.setStyleSheet("font: 14pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.bt_Guardar_Bodega = QtWidgets.QPushButton(self.Bodega)
        self.bt_Guardar_Bodega.setGeometry(QtCore.QRect(670, 70, 101, 31))
        self.bt_Guardar_Bodega.setStyleSheet("background-color: rgb(165, 215, 232);")
        self.bt_Guardar_Bodega.setObjectName("bt_Guardar_Bodega")
        self.bt_Editar_Bodega = QtWidgets.QPushButton(self.Bodega)
        self.bt_Editar_Bodega.setGeometry(QtCore.QRect(670, 20, 101, 31))
        self.bt_Editar_Bodega.setStyleSheet("background-color: rgb(165, 215, 232);")
        self.bt_Editar_Bodega.setObjectName("bt_Editar_Bodega")
        self.bt_Eliminar_Bodega = QtWidgets.QPushButton(self.Bodega)
        self.bt_Eliminar_Bodega.setGeometry(QtCore.QRect(670, 120, 101, 31))
        self.bt_Eliminar_Bodega.setStyleSheet("background-color: rgb(165, 215, 232);")
        self.bt_Eliminar_Bodega.setObjectName("bt_Eliminar_Bodega")
        self.bt_Vaciar_Bodega = QtWidgets.QPushButton(self.Bodega)
        self.bt_Vaciar_Bodega.setGeometry(QtCore.QRect(670, 170, 101, 31))
        self.bt_Vaciar_Bodega.setStyleSheet("background-color: rgb(165, 215, 232);")
        self.bt_Vaciar_Bodega.setObjectName("bt_Vaciar_Bodega")
        self.line_Bodega_Nombre = QtWidgets.QLineEdit(self.Bodega)
        self.line_Bodega_Nombre.setGeometry(QtCore.QRect(100, 20, 471, 25))
        self.line_Bodega_Nombre.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Bodega_Nombre.setObjectName("line_Bodega_Nombre")
        self.line_Bodega_Apellido = QtWidgets.QLineEdit(self.Bodega)
        self.line_Bodega_Apellido.setGeometry(QtCore.QRect(110, 140, 461, 71))
        self.line_Bodega_Apellido.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Bodega_Apellido.setObjectName("line_Bodega_Apellido")
        self.line_Bodega_Direccion = QtWidgets.QLineEdit(self.Bodega)
        self.line_Bodega_Direccion.setGeometry(QtCore.QRect(100, 70, 471, 41))
        self.line_Bodega_Direccion.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.line_Bodega_Direccion.setObjectName("line_Bodega_Direccion")
        self.tabWidget.addTab(self.Bodega, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Principal"))
        item = self.tb_Bodega.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tb_Bodega.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tienda"))
        item = self.tb_Bodega.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tb_Bodega.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Descripcion"))
        self.label.setText(_translate("MainWindow", "Tienda:"))
        self.label_2.setText(_translate("MainWindow", "Descripcion:"))
        self.label_3.setText(_translate("MainWindow", "Nombre:"))
        self.bt_Guardar_Bodega.setText(_translate("MainWindow", "Guardar"))
        self.bt_Editar_Bodega.setText(_translate("MainWindow", "Editar"))
        self.bt_Eliminar_Bodega.setText(_translate("MainWindow", "Eliminar"))
        self.bt_Vaciar_Bodega.setText(_translate("MainWindow", "Vaciar Campos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bodega), _translate("MainWindow", "Bodega"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())