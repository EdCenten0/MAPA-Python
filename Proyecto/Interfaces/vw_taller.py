# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vw_taller.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mw_taller(object):
    def setupUi(self, mw_taller):
        mw_taller.setObjectName("mw_taller")
        mw_taller.resize(800, 600)
        mw_taller.setStyleSheet("background-color: rgb(63, 73, 100);")
        self.centralwidget = QtWidgets.QWidget(mw_taller)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditar.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnEditar.setObjectName("btnEditar")
        self.gridLayout_3.addWidget(self.btnEditar, 1, 0, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout_3.addWidget(self.btnGuardar, 0, 0, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_3.addWidget(self.btnEliminar, 2, 0, 1, 1)
        self.btnVaciarCampos = QtWidgets.QPushButton(self.centralwidget)
        self.btnVaciarCampos.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnVaciarCampos.setObjectName("btnVaciarCampos")
        self.gridLayout_3.addWidget(self.btnVaciarCampos, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 2, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.txtNombre.setObjectName("txtNombre")
        self.gridLayout.addWidget(self.txtNombre, 0, 1, 1, 1)
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout.addWidget(self.lblNombre, 0, 0, 1, 1)
        self.txtDireccion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDireccion.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.txtDireccion.setObjectName("txtDireccion")
        self.gridLayout.addWidget(self.txtDireccion, 1, 1, 1, 1)
        self.lblTelefono = QtWidgets.QLabel(self.centralwidget)
        self.lblTelefono.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.lblTelefono.setObjectName("lblTelefono")
        self.gridLayout.addWidget(self.lblTelefono, 2, 0, 1, 1)
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.gridLayout.addWidget(self.txtTelefono, 2, 1, 1, 1)
        self.lblDIreccion = QtWidgets.QLabel(self.centralwidget)
        self.lblDIreccion.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.lblDIreccion.setObjectName("lblDIreccion")
        self.gridLayout.addWidget(self.lblDIreccion, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout_2.addWidget(self.txtEmail, 0, 1, 1, 1)
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout_2.addWidget(self.lblEmail, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tw_taller = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_taller.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"border-color: rgb(61, 56, 70);")
        self.tw_taller.setObjectName("tw_taller")
        self.tw_taller.setColumnCount(4)
        self.tw_taller.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_taller.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_taller.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_taller.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_taller.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tw_taller)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 2, 0, 1, 3)
        mw_taller.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mw_taller)
        self.statusbar.setObjectName("statusbar")
        mw_taller.setStatusBar(self.statusbar)

        self.retranslateUi(mw_taller)
        QtCore.QMetaObject.connectSlotsByName(mw_taller)

    def retranslateUi(self, mw_taller):
        _translate = QtCore.QCoreApplication.translate
        mw_taller.setWindowTitle(_translate("mw_taller", "Taller"))
        self.label.setText(_translate("mw_taller", "Taller"))
        self.btnEditar.setText(_translate("mw_taller", "Editar"))
        self.btnGuardar.setText(_translate("mw_taller", "Guardar"))
        self.btnEliminar.setText(_translate("mw_taller", "Eliminar"))
        self.btnVaciarCampos.setText(_translate("mw_taller", "Vaciar Campos"))
        self.lblNombre.setText(_translate("mw_taller", "Nombre:"))
        self.lblTelefono.setText(_translate("mw_taller", "Telefono:"))
        self.lblDIreccion.setText(_translate("mw_taller", "Direccion:"))
        self.lblEmail.setText(_translate("mw_taller", "Email:"))
        item = self.tw_taller.horizontalHeaderItem(0)
        item.setText(_translate("mw_taller", "Nombre"))
        item = self.tw_taller.horizontalHeaderItem(1)
        item.setText(_translate("mw_taller", "Direccion"))
        item = self.tw_taller.horizontalHeaderItem(2)
        item.setText(_translate("mw_taller", "Telefono"))
        item = self.tw_taller.horizontalHeaderItem(3)
        item.setText(_translate("mw_taller", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_taller = QtWidgets.QMainWindow()
    ui = Ui_mw_taller()
    ui.setupUi(mw_taller)
    mw_taller.show()
    sys.exit(app.exec_())
