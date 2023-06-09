# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Recursos import Recursos


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1481, 950)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(242, 242, 241);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("* {\n"
"        border:none;\n"
"font-family:\"Inter\", sans-serif;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("QComboBox{\n"
"        background-color:rgb(255, 255, 255);\n"
"        border:1px solid rgb(100,100,100);\n"
"        color:rgb(50,50,50);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"        background-color: rgb(255, 255, 255);    \n"
"        border:1px solid #c7c7c7;\n"
"        border-radius:7px;\n"
"        background-color:rgb(246, 245, 244);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background-color:#c7c7c7;\n"
"        border:1px solid rgb(255,255,255);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ly_contenedor = QtWidgets.QVBoxLayout()
        self.ly_contenedor.setObjectName("ly_contenedor")
        self.gridLayout_4.addLayout(self.ly_contenedor, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: rgb(240, 213, 209);\n"
"\n"
"}\n"
"\n"
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
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(63)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-bottom-color:1px solid rgb(119, 118, 123);\n"
"font-weight:500;\n"
"font-size:22px;")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 170))
        self.label_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_2.setStyleSheet("border-image: url(:/Imagenes/mapalogo.ico);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../../../../../../../../../../../../../../Recursos/Logo-MAPA.ico"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(12, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.bt_vista_previa_pedidos = QtWidgets.QPushButton(self.frame_2)
        self.bt_vista_previa_pedidos.setMinimumSize(QtCore.QSize(0, 44))
        self.bt_vista_previa_pedidos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_vista_previa_pedidos.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.bt_vista_previa_pedidos.setObjectName("bt_vista_previa_pedidos")
        self.verticalLayout.addWidget(self.bt_vista_previa_pedidos)
        self.bt_clientes = QtWidgets.QPushButton(self.frame_2)
        self.bt_clientes.setMinimumSize(QtCore.QSize(0, 44))
        self.bt_clientes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_clientes.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}")
        self.bt_clientes.setObjectName("bt_clientes")
        self.verticalLayout.addWidget(self.bt_clientes)
        self.bt_proveedores = QtWidgets.QPushButton(self.frame_2)
        self.bt_proveedores.setMinimumSize(QtCore.QSize(0, 44))
        self.bt_proveedores.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_proveedores.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.bt_proveedores.setObjectName("bt_proveedores")
        self.verticalLayout.addWidget(self.bt_proveedores)
        self.bt_materiales = QtWidgets.QPushButton(self.frame_2)
        self.bt_materiales.setEnabled(True)
        self.bt_materiales.setMinimumSize(QtCore.QSize(44, 44))
        self.bt_materiales.setSizeIncrement(QtCore.QSize(0, 0))
        self.bt_materiales.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_materiales.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"\n"
"")
        self.bt_materiales.setIconSize(QtCore.QSize(19, 19))
        self.bt_materiales.setFlat(False)
        self.bt_materiales.setObjectName("bt_materiales")
        self.verticalLayout.addWidget(self.bt_materiales)
        self.bt_materiales_por_proveedor = QtWidgets.QPushButton(self.frame_2)
        self.bt_materiales_por_proveedor.setEnabled(True)
        self.bt_materiales_por_proveedor.setMinimumSize(QtCore.QSize(44, 44))
        self.bt_materiales_por_proveedor.setSizeIncrement(QtCore.QSize(0, 0))
        self.bt_materiales_por_proveedor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_materiales_por_proveedor.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"\n"
"")
        self.bt_materiales_por_proveedor.setIconSize(QtCore.QSize(19, 19))
        self.bt_materiales_por_proveedor.setFlat(False)
        self.bt_materiales_por_proveedor.setObjectName("bt_materiales_por_proveedor")
        self.verticalLayout.addWidget(self.bt_materiales_por_proveedor)
        self.bt_facturas = QtWidgets.QPushButton(self.frame_2)
        self.bt_facturas.setEnabled(True)
        self.bt_facturas.setMinimumSize(QtCore.QSize(44, 44))
        self.bt_facturas.setSizeIncrement(QtCore.QSize(0, 0))
        self.bt_facturas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_facturas.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"")
        self.bt_facturas.setIconSize(QtCore.QSize(19, 19))
        self.bt_facturas.setFlat(False)
        self.bt_facturas.setObjectName("bt_facturas")
        self.verticalLayout.addWidget(self.bt_facturas)
        self.bt_ventas = QtWidgets.QPushButton(self.frame_2)
        self.bt_ventas.setEnabled(True)
        self.bt_ventas.setMinimumSize(QtCore.QSize(44, 44))
        self.bt_ventas.setSizeIncrement(QtCore.QSize(0, 0))
        self.bt_ventas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_ventas.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"\n"
"")
        self.bt_ventas.setIconSize(QtCore.QSize(19, 19))
        self.bt_ventas.setFlat(False)
        self.bt_ventas.setObjectName("bt_ventas")
        self.verticalLayout.addWidget(self.bt_ventas)
        self.bt_taller = QtWidgets.QPushButton(self.frame_2)
        self.bt_taller.setEnabled(True)
        self.bt_taller.setMinimumSize(QtCore.QSize(44, 44))
        self.bt_taller.setSizeIncrement(QtCore.QSize(0, 0))
        self.bt_taller.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_taller.setStyleSheet("QPushButton:hover {\n"
"    background-color: #D6D2D1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #52c7ff;\n"
"}\n"
"\n"
"")
        self.bt_taller.setIconSize(QtCore.QSize(19, 19))
        self.bt_taller.setFlat(False)
        self.bt_taller.setObjectName("bt_taller")
        self.verticalLayout.addWidget(self.bt_taller)
        self.bt_tienda = QtWidgets.QPushButton(self.frame_2)
        self.bt_tienda.setStyleSheet("QPushButton {\n"
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
        self.bt_tienda.setObjectName("bt_tienda")
        self.verticalLayout.addWidget(self.bt_tienda)
        self.bt_seguridad = QtWidgets.QPushButton(self.frame_2)
        self.bt_seguridad.setMinimumSize(QtCore.QSize(0, 44))
        self.bt_seguridad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_seguridad.setStyleSheet("QPushButton {\n"
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
        self.bt_seguridad.setObjectName("bt_seguridad")
        self.verticalLayout.addWidget(self.bt_seguridad)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("font-family:\"Inter\", sans-serif;\n"
"font-weight:300;\n"
"color: rgb(42, 40, 40);\n"
"font-size:17px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("font-family:\"Inter\", sans-serif;\n"
"font-weight:300;\n"
"color: rgb(154, 153, 150);\n"
"font-size:13px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MAPA Furniture"))
        self.bt_vista_previa_pedidos.setText(_translate("MainWindow", "Pedidos"))
        self.bt_clientes.setText(_translate("MainWindow", "Clientes"))
        self.bt_proveedores.setText(_translate("MainWindow", "Proveedores"))
        self.bt_materiales.setText(_translate("MainWindow", "Materiales"))
        self.bt_materiales_por_proveedor.setText(_translate("MainWindow", "Materiales Por Proved."))
        self.bt_facturas.setText(_translate("MainWindow", "Facturas"))
        self.bt_ventas.setText(_translate("MainWindow", "Ventas"))
        self.bt_taller.setText(_translate("MainWindow", "Taller"))
        self.bt_tienda.setText(_translate("MainWindow", "Tienda"))
        self.bt_seguridad.setText(_translate("MainWindow", "Seguridad"))
        self.label_3.setText(_translate("MainWindow", "Usuario"))
        self.label_4.setText(_translate("MainWindow", "Rol"))
        Recursos



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
