# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Materiales_por_proveedor_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_background(object):
    def setupUi(self, background):
        background.setObjectName("background")
        background.resize(800, 599)
        background.setMouseTracking(False)
        background.setAutoFillBackground(False)
        background.setStyleSheet("background-color: rgb(63, 73, 100);")
        background.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(background)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cb_material = QtWidgets.QComboBox(self.centralwidget)
        self.cb_material.setObjectName("cb_material")
        self.gridLayout_3.addWidget(self.cb_material, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.cb_proveedor = QtWidgets.QComboBox(self.centralwidget)
        self.cb_proveedor.setObjectName("cb_proveedor")
        self.gridLayout_3.addWidget(self.cb_proveedor, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.bt_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_guardar.setObjectName("bt_guardar")
        self.verticalLayout_8.addWidget(self.bt_guardar)
        self.bt_editar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_editar.setObjectName("bt_editar")
        self.verticalLayout_8.addWidget(self.bt_editar)
        self.bt_borrar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_borrar.setObjectName("bt_borrar")
        self.verticalLayout_8.addWidget(self.bt_borrar)
        self.bt_vaciar_campos = QtWidgets.QPushButton(self.centralwidget)
        self.bt_vaciar_campos.setObjectName("bt_vaciar_campos")
        self.verticalLayout_8.addWidget(self.bt_vaciar_campos)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_materiales_requeridos_por_pedido = QtWidgets.QTableWidget(self.centralwidget)
        self.table_materiales_requeridos_por_pedido.setFocusPolicy(QtCore.Qt.TabFocus)
        self.table_materiales_requeridos_por_pedido.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_materiales_requeridos_por_pedido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_materiales_requeridos_por_pedido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_materiales_requeridos_por_pedido.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_materiales_requeridos_por_pedido.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_materiales_requeridos_por_pedido.setTextElideMode(QtCore.Qt.ElideNone)
        self.table_materiales_requeridos_por_pedido.setShowGrid(True)
        self.table_materiales_requeridos_por_pedido.setWordWrap(True)
        self.table_materiales_requeridos_por_pedido.setCornerButtonEnabled(True)
        self.table_materiales_requeridos_por_pedido.setRowCount(0)
        self.table_materiales_requeridos_por_pedido.setObjectName("table_materiales_requeridos_por_pedido")
        self.table_materiales_requeridos_por_pedido.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(2, item)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setVisible(True)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setCascadingSectionResizes(True)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setDefaultSectionSize(258)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setHighlightSections(True)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setMinimumSectionSize(39)
        self.table_materiales_requeridos_por_pedido.verticalHeader().setDefaultSectionSize(23)
        self.table_materiales_requeridos_por_pedido.verticalHeader().setMinimumSectionSize(16)
        self.verticalLayout_2.addWidget(self.table_materiales_requeridos_por_pedido)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        background.setCentralWidget(self.centralwidget)

        self.retranslateUi(background)
        QtCore.QMetaObject.connectSlotsByName(background)

    def retranslateUi(self, background):
        _translate = QtCore.QCoreApplication.translate
        background.setWindowTitle(_translate("background", "Materiales por pedido"))
        self.label_5.setText(_translate("background", "Proveedor"))
        self.label_4.setText(_translate("background", "Material"))
        self.bt_guardar.setText(_translate("background", "Guardar"))
        self.bt_editar.setText(_translate("background", "Editar"))
        self.bt_borrar.setText(_translate("background", "Borrar"))
        self.bt_vaciar_campos.setText(_translate("background", "Vaciar Campos"))
        self.table_materiales_requeridos_por_pedido.setSortingEnabled(False)
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(0)
        item.setText(_translate("background", "ID"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(1)
        item.setText(_translate("background", "Material"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(2)
        item.setText(_translate("background", "Proveedor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background = QtWidgets.QMainWindow()
    ui = Ui_background()
    ui.setupUi(background)
    background.show()
    sys.exit(app.exec_())
