import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Datos import dt_rol
from Interfaces import vw_registrar_usuario_login
from Interfaces.vw_login import Ui_Login


class registrar_Window(QMainWindow, vw_registrar_usuario_login.Ui_Registrar):
    def __init__(self):
        super(registrar_Window, self).__init__()
        self.setupUi(self)

        self.bt_registrar.clicked.connect(self.registrarUsuario)
        self.cb_rol.addItem(self.llenarComboxRol(dt_rol.Dt_Rol.listarRol()))

    def registrarUsuario(self):
        try:
            if not self.line_usuario.text() == "" and not self.line_clave.text() == "" and not self.line_nombre.text() == "" and not self.line_apellido.text() == "" and not self.cb_rol.itemText():
                pass

            else:
                pass

            self.close()

        except Exception as e:
            print(f"ERROR: {e}")


    def llenarComboxRol(self, datos):
        try:
            index = 0
            print("\nDatos de la combo box Rol")
            for registro in datos:
                print(registro)
                self.cb_rol.addItem(registro["descripcion"],registro["id_rol"])

            print(self.cb_rol.itemData(index))
            print(self.cb_rol.itemText(index))


        except Exception as e:
            print(f"ERROR: {e}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = registrar_Window()
    mw.show()
    sys.exit(app.exec_())


