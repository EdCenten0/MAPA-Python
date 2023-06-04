# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'materiales.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mw_materiales(object):
    def setupUi(self, mw_materiales):
        mw_materiales.setObjectName("mw_materiales")
        mw_materiales.resize(802, 600)
        mw_materiales.setStyleSheet("background-color: rgb(63, 73, 100);")
        self.centralwidget = QtWidgets.QWidget(mw_materiales)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 2, 4, 0)
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.setVerticalSpacing(51)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblProveedores = QtWidgets.QLabel(self.centralwidget)
        self.lblProveedores.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.lblProveedores.setObjectName("lblProveedores")
        self.gridLayout_2.addWidget(self.lblProveedores, 2, 0, 1, 1)
        self.cbPedidos = QtWidgets.QComboBox(self.centralwidget)
        self.cbPedidos.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cbPedidos.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.cbPedidos.setMaxVisibleItems(25)
        self.cbPedidos.setObjectName("cbPedidos")
        self.gridLayout_2.addWidget(self.cbPedidos, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.cbUnidadesMedida = QtWidgets.QComboBox(self.centralwidget)
        self.cbUnidadesMedida.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbUnidadesMedida.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbUnidadesMedida.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.cbUnidadesMedida.setEditable(False)
        self.cbUnidadesMedida.setMaxVisibleItems(10)
        self.cbUnidadesMedida.setMaxCount(2147483647)
        self.cbUnidadesMedida.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cbUnidadesMedida.setObjectName("cbUnidadesMedida")
        self.cbUnidadesMedida.addItem("")
        self.cbUnidadesMedida.addItem("")
        self.cbUnidadesMedida.addItem("")
        self.cbUnidadesMedida.addItem("")
        self.cbUnidadesMedida.addItem("")
        self.cbUnidadesMedida.addItem("")
        self.cbUnidadesMedida.addItem("")
        self.gridLayout_2.addWidget(self.cbUnidadesMedida, 0, 2, 1, 1)
        self.txtCantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCantidad.setObjectName("txtCantidad")
        self.gridLayout_2.addWidget(self.txtCantidad, 0, 1, 1, 1)
        self.txtPrecioTotal = QtWidgets.QLabel(self.centralwidget)
        self.txtPrecioTotal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPrecioTotal.setText("")
        self.txtPrecioTotal.setObjectName("txtPrecioTotal")
        self.gridLayout_2.addWidget(self.txtPrecioTotal, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 25, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout_3.addWidget(self.btnEliminar, 3, 0, 1, 1)
        self.btnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditar.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnEditar.setObjectName("btnEditar")
        self.gridLayout_3.addWidget(self.btnEditar, 2, 0, 1, 1)
        self.btnVaciarCampos = QtWidgets.QPushButton(self.centralwidget)
        self.btnVaciarCampos.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnVaciarCampos.setObjectName("btnVaciarCampos")
        self.gridLayout_3.addWidget(self.btnVaciarCampos, 4, 0, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout_3.addWidget(self.btnGuardar, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 19, 0, 12)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.txtPrecioUnidadMedida = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecioUnidadMedida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPrecioUnidadMedida.setObjectName("txtPrecioUnidadMedida")
        self.gridLayout.addWidget(self.txtPrecioUnidadMedida, 2, 1, 1, 1)
        self.lblId = QtWidgets.QLabel(self.centralwidget)
        self.lblId.setStyleSheet("color: rgb(63, 73, 100);")
        self.lblId.setText("")
        self.lblId.setObjectName("lblId")
        self.gridLayout.addWidget(self.lblId, 3, 0, 1, 1)
        self.txtNombreMaterial = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombreMaterial.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNombreMaterial.setObjectName("txtNombreMaterial")
        self.gridLayout.addWidget(self.txtNombreMaterial, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtDescripcion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDescripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.gridLayout.addWidget(self.txtDescripcion, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tw_materiales = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_materiales.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tw_materiales.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tw_materiales.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tw_materiales.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tw_materiales.setObjectName("tw_materiales")
        self.tw_materiales.setColumnCount(8)
        self.tw_materiales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_materiales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_materiales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_materiales.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_materiales.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_materiales.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_materiales.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_materiales.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_materiales.setHorizontalHeaderItem(7, item)
        self.tw_materiales.horizontalHeader().setVisible(True)
        self.tw_materiales.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_materiales.horizontalHeader().setDefaultSectionSize(113)
        self.tw_materiales.horizontalHeader().setSortIndicatorShown(True)
        self.tw_materiales.horizontalHeader().setStretchLastSection(False)
        self.tw_materiales.verticalHeader().setCascadingSectionResizes(False)
        self.tw_materiales.verticalHeader().setDefaultSectionSize(60)
        self.tw_materiales.verticalHeader().setHighlightSections(True)
        self.tw_materiales.verticalHeader().setMinimumSectionSize(21)
        self.tw_materiales.verticalHeader().setSortIndicatorShown(False)
        self.tw_materiales.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tw_materiales)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 0, 1, 3)
        mw_materiales.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mw_materiales)
        self.statusbar.setObjectName("statusbar")
        mw_materiales.setStatusBar(self.statusbar)

        self.retranslateUi(mw_materiales)
        self.cbPedidos.setCurrentIndex(-1)
        self.cbUnidadesMedida.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mw_materiales)

    def retranslateUi(self, mw_materiales):
        _translate = QtCore.QCoreApplication.translate
        mw_materiales.setWindowTitle(_translate("mw_materiales", "Materiales"))
        self.lblProveedores.setText(_translate("mw_materiales", "Pedidos"))
        self.label_5.setText(_translate("mw_materiales", "Precio total"))
        self.label_4.setText(_translate("mw_materiales", "Cantidad"))
        self.cbUnidadesMedida.setItemText(0, _translate("mw_materiales", "lbs"))
        self.cbUnidadesMedida.setItemText(1, _translate("mw_materiales", "ltrs"))
        self.cbUnidadesMedida.setItemText(2, _translate("mw_materiales", "mts"))
        self.cbUnidadesMedida.setItemText(3, _translate("mw_materiales", "pulg"))
        self.cbUnidadesMedida.setItemText(4, _translate("mw_materiales", "galon"))
        self.cbUnidadesMedida.setItemText(5, _translate("mw_materiales", "unidad"))
        self.cbUnidadesMedida.setItemText(6, _translate("mw_materiales", "simpl"))
        self.btnEliminar.setText(_translate("mw_materiales", "Eliminar"))
        self.btnEditar.setText(_translate("mw_materiales", "Editar"))
        self.btnVaciarCampos.setText(_translate("mw_materiales", "Vaciar Campos"))
        self.btnGuardar.setText(_translate("mw_materiales", "Guardar"))
        self.label_3.setText(_translate("mw_materiales", "Precio*UMedida"))
        self.label_2.setText(_translate("mw_materiales", "Descripcion"))
        self.label.setText(_translate("mw_materiales", "Material"))
        item = self.tw_materiales.horizontalHeaderItem(0)
        item.setText(_translate("mw_materiales", "Id"))
        item = self.tw_materiales.horizontalHeaderItem(1)
        item.setText(_translate("mw_materiales", "Material"))
        item = self.tw_materiales.horizontalHeaderItem(2)
        item.setText(_translate("mw_materiales", "Descripcion"))
        item = self.tw_materiales.horizontalHeaderItem(3)
        item.setText(_translate("mw_materiales", "Precio*UnidadMedida"))
        item = self.tw_materiales.horizontalHeaderItem(4)
        item.setText(_translate("mw_materiales", "Cantidad"))
        item = self.tw_materiales.horizontalHeaderItem(5)
        item.setText(_translate("mw_materiales", "unidad_de_medida"))
        item = self.tw_materiales.horizontalHeaderItem(6)
        item.setText(_translate("mw_materiales", "Precio Total"))
        item = self.tw_materiales.horizontalHeaderItem(7)
        item.setText(_translate("mw_materiales", "Pedido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_materiales = QtWidgets.QMainWindow()
    ui = Ui_mw_materiales()
    ui.setupUi(mw_materiales)
    mw_materiales.show()
    sys.exit(app.exec_())
