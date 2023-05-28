# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def __init__(self):
        self.widgetcentral = None

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1000, 800)
        Login.setMinimumSize(QtCore.QSize(1000, 800))
        Login.setMaximumSize(QtCore.QSize(1000, 800))
        Login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widgetcentral = QtWidgets.QWidget(Login)
        self.widgetcentral.setStyleSheet("font-family:\"Inter\", sans-serif;")
        self.widgetcentral.setObjectName("widgetcentral")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetcentral)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Background_Login = QtWidgets.QFrame(self.widgetcentral)
        self.Background_Login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background_Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background_Login.setObjectName("Background_Login")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Background_Login)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_fondo = QtWidgets.QFrame(self.Background_Login)
        self.frame_fondo.setStyleSheet("")
        self.frame_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fondo.setObjectName("frame_fondo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_fondo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_fondo)
        self.label_6.setStyleSheet("border-image: url(:/Imagenes/Fondo MAPA.jpeg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.frame_fondo)
        self.frame_registrar = QtWidgets.QFrame(self.Background_Login)
        self.frame_registrar.setStyleSheet("font-family:\"Inter\", sans-serif;")
        self.frame_registrar.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_registrar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_registrar.setObjectName("frame_registrar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_registrar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_registrar)
        self.frame_4.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 221, 16))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(50, 10, 231, 41))
        self.label.setStyleSheet("font-weight:500;\n"
"font-size:35px;\n"
"")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(90, 90, 87, 25))
        self.label_4.setStyleSheet("font-weight:500;\n"
"font-size:22px;")
        self.label_4.setObjectName("label_4")
        self.line_Clave = QtWidgets.QLineEdit(self.frame_4)
        self.line_Clave.setGeometry(QtCore.QRect(190, 80, 411, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Clave.sizePolicy().hasHeightForWidth())
        self.line_Clave.setSizePolicy(sizePolicy)
        self.line_Clave.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_Clave.setStyleSheet("QLineEdit {\n"
"    border: 3px solid rgba(246, 143, 137, 255);\n"
"    border-radius:    10%;\n"
"    text-align: left;\n"
"    font-weight:100;\n"
"}")
        self.line_Clave.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_Clave.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_Clave.setObjectName("line_Clave")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 141, 61))
        self.label_2.setStyleSheet("font-weight:500;\n"
"font-size:22px;")
        self.label_2.setObjectName("label_2")
        self.line_Usuario = QtWidgets.QLineEdit(self.frame_4)
        self.line_Usuario.setGeometry(QtCore.QRect(190, 140, 411, 40))
        self.line_Usuario.setStyleSheet("QLineEdit {\n"
"    border: 3px solid rgba(246, 143, 137, 255);\n"
"    border-radius:10%;\n"
"    font-weight:100;\n"
"}")
        self.line_Usuario.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_Usuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_Usuario.setObjectName("line_Usuario")
        self.lb_crear_Usuario = QtWidgets.QLabel(self.frame_4)
        self.lb_crear_Usuario.setGeometry(QtCore.QRect(190, 250, 114, 21))
        self.lb_crear_Usuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lb_crear_Usuario.setStyleSheet("QLabel:hover {\n"
"    color: blue;\n"
"}")
        self.lb_crear_Usuario.setObjectName("lb_crear_Usuario")
        self.bt_ingresar = QtWidgets.QPushButton(self.frame_4)
        self.bt_ingresar.setGeometry(QtCore.QRect(190, 200, 411, 40))
        self.bt_ingresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_ingresar.setStyleSheet("QPushButton{\n"
"        background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.0170455, stop:0.261364 rgba(246, 143, 137,             255), stop:1 rgba(128, 74, 70, 255));\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius:10%;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.0170455, stop:0.261364 rgba(200, 90, 90,             255), stop:1 rgba(155, 90, 100, 255));\n"
"}\n"
"")
        self.bt_ingresar.setObjectName("bt_ingresar")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(270, 50, 131, 16))
        self.label_5.setStyleSheet("font-weight:500;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_registrar)
        self.horizontalLayout.addWidget(self.Background_Login)
        Login.setCentralWidget(self.widgetcentral)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "Inicia sesión con tu usuario de "))
        self.label.setText(_translate("Login", "Iniciar Sesión"))
        self.label_4.setText(_translate("Login", "Usuario:"))
        self.line_Clave.setPlaceholderText(_translate("Login", "Ingrese su nombre de usuario"))
        self.label_2.setText(_translate("Login", "Contraseña:"))
        self.line_Usuario.setPlaceholderText(_translate("Login", "Ingrese su contraseña"))
        self.lb_crear_Usuario.setText(_translate("Login", "Crear un cuenta"))
        self.bt_ingresar.setText(_translate("Login", "Ingresar"))
        self.label_5.setText(_translate("Login", "MAPA Interface"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
