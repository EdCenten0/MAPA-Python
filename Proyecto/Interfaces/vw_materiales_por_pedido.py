# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Materiales_por_pedido_window.ui'
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
        self.line_cantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.line_cantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_cantidad.setObjectName("line_cantidad")
        self.gridLayout_3.addWidget(self.line_cantidad, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.combobox_cantidad = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_cantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combobox_cantidad.setObjectName("combobox_cantidad")
        self.gridLayout_3.addWidget(self.combobox_cantidad, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.line_precio_total = QtWidgets.QLineEdit(self.centralwidget)
        self.line_precio_total.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_precio_total.setObjectName("line_precio_total")
        self.gridLayout_3.addWidget(self.line_precio_total, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(-1, 50, -1, 50)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.line_material = QtWidgets.QLineEdit(self.centralwidget)
        self.line_material.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_material.setObjectName("line_material")
        self.gridLayout_4.addWidget(self.line_material, 0, 1, 1, 1)
        self.line_precio_por_unidad = QtWidgets.QLineEdit(self.centralwidget)
        self.line_precio_por_unidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_precio_por_unidad.setObjectName("line_precio_por_unidad")
        self.gridLayout_4.addWidget(self.line_precio_por_unidad, 2, 1, 1, 1)
        self.line_descripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.line_descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_descripcion.setObjectName("line_descripcion")
        self.gridLayout_4.addWidget(self.line_descripcion, 1, 1, 1, 1)
        self.gridLayout_4.setColumnMinimumWidth(1, 1)
        self.gridLayout_4.setRowMinimumHeight(0, 1)
        self.gridLayout_4.setRowMinimumHeight(1, 2)
        self.gridLayout_4.setRowMinimumHeight(2, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 2)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.bt_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_guardar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_guardar.setObjectName("bt_guardar")
        self.verticalLayout_3.addWidget(self.bt_guardar)
        self.bt_editar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_editar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_editar.setObjectName("bt_editar")
        self.verticalLayout_3.addWidget(self.bt_editar)
        self.bt_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_eliminar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bt_eliminar.setObjectName("bt_eliminar")
        self.verticalLayout_3.addWidget(self.bt_eliminar)
        self.bt_vaciar_campos = QtWidgets.QPushButton(self.centralwidget)
        self.bt_vaciar_campos.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.bt_vaciar_campos.setObjectName("bt_vaciar_campos")
        self.verticalLayout_3.addWidget(self.bt_vaciar_campos)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
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
        self.table_materiales_requeridos_por_pedido.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_materiales_requeridos_por_pedido.setTextElideMode(QtCore.Qt.ElideNone)
        self.table_materiales_requeridos_por_pedido.setWordWrap(True)
        self.table_materiales_requeridos_por_pedido.setCornerButtonEnabled(True)
        self.table_materiales_requeridos_por_pedido.setRowCount(0)
        self.table_materiales_requeridos_por_pedido.setObjectName("table_materiales_requeridos_por_pedido")
        self.table_materiales_requeridos_por_pedido.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_materiales_requeridos_por_pedido.setHorizontalHeaderItem(5, item)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setVisible(True)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setCascadingSectionResizes(True)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setDefaultSectionSize(134)
        self.table_materiales_requeridos_por_pedido.horizontalHeader().setHighlightSections(False)
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
        self.label_4.setText(_translate("background", "Cantidad"))
        self.label_5.setText(_translate("background", "Precio Total"))
        self.label_2.setText(_translate("background", "Descripcion"))
        self.label.setText(_translate("background", "Material"))
        self.label_3.setText(_translate("background", "Precio por Unidad"))
        self.bt_guardar.setText(_translate("background", "Guardar"))
        self.bt_editar.setText(_translate("background", "Editar"))
        self.bt_eliminar.setText(_translate("background", "Eliminar"))
        self.bt_vaciar_campos.setText(_translate("background", "Vaciar Campos"))
        self.table_materiales_requeridos_por_pedido.setSortingEnabled(False)
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(0)
        item.setText(_translate("background", "ID"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(1)
        item.setText(_translate("background", "Material"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(2)
        item.setText(_translate("background", "Descripcion"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(3)
        item.setText(_translate("background", "Precio por Unidad"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(4)
        item.setText(_translate("background", "Cantidad"))
        item = self.table_materiales_requeridos_por_pedido.horizontalHeaderItem(5)
        item.setText(_translate("background", "Precio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background = QtWidgets.QMainWindow()
    ui = Ui_background()
    ui.setupUi(background)
    background.show()
    sys.exit(app.exec_())