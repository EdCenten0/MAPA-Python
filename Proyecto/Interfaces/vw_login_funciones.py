# Francisco de Jesús Melendez Simplina

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget

from Datos.dt_usuario import Dt_Usuarios
from Interfaces.vw_registrar_funciones import registrar_Window
from Entidades.usuarios import Usuarios

from Interfaces import vw_login
from Interfaces.vw_ventana_principal_funciones import VentanaPrincipal


class login_Window(QMainWindow, vw_login.Ui_Login):
    def __init__(self):
        super(login_Window, self).__init__()
        self.setupUi(self)
        self.bt_ingresar.clicked.connect(self.iniciarSesion)
        self.bt_crear_usuario.clicked.connect(self.abrirRegistrar)


    def abrirRegistrar(self):
        try:
            self.registrar_window = registrar_Window()
            self.registrar_window.show()

        except Exception as e:
            print(f"ERROR: {e}")


    def abrirMainWindow(self):
        try:
            self.close()
            self.main_window = VentanaPrincipal()
            self.main_window.show()
            #Llamar ventan principal

        except Exception as e:
            print(f"ERROR: {e}")

    def iniciarSesion(self):
        Usuarios.user = self.line_Usuario.text()
        Usuarios.password = self.line_Clave.text()

        if Dt_Usuarios.ExisteUsuario(Usuarios):
            QMessageBox.about(self, "Inicio de sesión exitoso!", f"Ingreso de sesión completado, Bienvenido {Usuarios.user}")
            #Llamar ventana principal del programa
            self.abrirMainWindow()

        else:

            QMessageBox.about(self, "Error Inicio de sesión!", "El usuario y contraseña que ingreso no son validos")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = login_Window()
    mw.show()
    sys.exit(app.exec_())
