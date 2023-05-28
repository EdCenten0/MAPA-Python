# Francisco de Jesús Melendez Simplina

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from Proyecto.Datos import dt_rol, dt_usuario, dt_usuario_rol
from Proyecto.Entidades.usuario_rol import Usuario_rol
from Proyecto.Entidades.usuarios import Usuarios
from Proyecto.Interfaces import  vw_registrar


class registrar_Window(QMainWindow, vw_registrar.Ui_Registrar):
    def __init__(self):
        super(registrar_Window, self).__init__()
        self.setupUi(self)

        self.bt_registrar.clicked.connect(self.registrarUsuario)
        self.cb_rol.addItem(self.llenarComboxRol(dt_rol.Dt_Rol.listarRol()))

    def registrarUsuario(self):

        try:
            if not self.line_usuario.text() == "" and not self.line_clave.text() == "" and not self.line_nombre.text() == "" and not self.line_apellido.text() == "" :
                Usuarios.nombre = self.line_nombre.text()
                Usuarios.user = self.line_usuario.text()
                Usuarios.apellido = self.line_apellido.text()
                Usuarios.password = self.line_clave.text()

                dt_usuario.Dt_Usuarios.guardarUsuario(Usuarios)

                QMessageBox.about(self, "Exito!", "Los Datos Fueron Guardados Correctamente")

                listaUsuarios = dt_usuario.Dt_Usuarios.listarUsuarios()
                for row in listaUsuarios:
                    print(row)
                    id_user = row["id_usuario"]

                Usuario_rol.id_usuario = int(id_user)
                Usuario_rol.id_rol = self.cb_rol.itemData(self.cb_rol.currentIndex())

                dt_usuario_rol.Dt_Usuario_rol.guardarUsuarioRol(Usuario_rol)

                self.close()

            else:


                QMessageBox.about(self,"Error", "Faltan campos por llenar")


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


