# Francisco de Jesús Melendez Simplina

import sys
from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from Proyecto.Datos import dt_usuario, dt_rol, dt_opcion, dt_rol_opcion, dt_usuario_rol
from Proyecto.Entidades import usuario_rol
from Proyecto.Entidades.rol_opcion import Rol_opcion
from Proyecto.Entidades.usuarios import Usuarios
from Proyecto.Entidades.roles import Rol
from Proyecto.Entidades.opciones import Opcion

from PyQt5.QtWidgets import QApplication, QMainWindow

from Proyecto.Interfaces import vw_seguridad


class seguridad_Window(QMainWindow, vw_seguridad.Ui_Seguridad):
    def __init__(self, parent=None):
        super(seguridad_Window, self).__init__(parent)
        self.setupUi(self)


        # Acciones de botones

        # Botones de Usuario
        self.bt_Guardar_Usuario.clicked.connect(self.guardarUsuario)
        self.bt_Editar_Usuario.clicked.connect(self.editarUsuario)
        self.bt_Eliminar_Usuario.clicked.connect(self.eliminarUsuario)
        self.bt_Vaciar_Usuario.clicked.connect(self.limpiarCampos)

        # Botones de Rol
        self.bt_Guardar_Rol.clicked.connect(self.guardarRol)
        self.bt_Editar_Rol.clicked.connect(self.editarRol)
        self.bt_Eliminar_Rol.clicked.connect(self.eliminarRol)
        self.bt_Vaciar_Rol.clicked.connect(self.limpiarCampos)

        # Botones de Opcion
        self.bt_Guardar_Opcion.clicked.connect(self.guardarOpcion)
        self.bt_Editar_Opcion.clicked.connect(self.editarOpcion)
        self.bt_Eliminar_Opcion.clicked.connect(self.eliminarOpcion)
        self.bt_Vaciar_Opcion.clicked.connect(self.limpiarCampos)

        # Botones de UsuarioRol
        self.bt_Guardar_Usuario_rol.clicked.connect(self.guardarUsuarioRol)

        # Botones de RolOpcion
        self.bt_Guardar_Rol_opcion.clicked.connect(self.guardarRolOpcion)

        # Acciones de las tablas

        # Usuarios
        self.llenarTablaUsuario(dt_usuario.Dt_Usuarios.listarUsuarios())
        self.tb_Usuario.itemSelectionChanged.connect(self.obtenerDatosTablaUsuario)

        # Roles
        self.llenarTablaRol(dt_rol.Dt_Rol.listarRol())
        self.tb_Rol.itemSelectionChanged.connect(self.obtenerDatosTablaRol)

        # Opciones
        self.llenarTablaOpcion(dt_opcion.Dt_Opcion.listarOpcion())
        self.tb_Opcion.itemSelectionChanged.connect(self.obtenerDatosTablaOpcion)

        #Asignar Rol
        self.llenarTablaUsuarioRol(dt_usuario_rol.Dt_Usuario_rol.listarUsuario_rol())
        self.llenarTablaRolOpcion(dt_rol_opcion.Dt_rol_opcion.listarRolOpcion())

        #Combo Box
        self.llenarComboxRoles(dt_rol.Dt_Rol.listarRol())
        self.llenarComboxUsuarios(dt_usuario.Dt_Usuarios.listarUsuarios())
        self.llenarComboxOpcion(dt_opcion.Dt_Opcion.listarOpcion())



    '''***********************************************  Funciones reutilizables   ******************************************'''


    def limpiarCampos(self):

        if not self.line_Usuario_Nombre.text() == "" or not self.line_Usuario_Apellido.text() == "" or not self.line_Usuario_User.text() == "" or not self.line_Usuario_Password.text() == "":
            print("\n Datos limpiados de la ventana Usuario")
            self.line_Usuario_Id.clear()
            self.line_Usuario_Nombre.clear()
            self.line_Usuario_Apellido.clear()
            self.line_Usuario_User.clear()
            self.line_Usuario_Password.clear()

        # Rol
        if not self.line_Rol_Id.text() == "" or not self.line_Rol.text() == "":
            print("\nDatos limpiados de la ventana Rol")
            self.line_Rol_Id.clear()
            self.line_Rol.clear()

        # Opcion
        if not self.line_Opcion_Id.text() == "" or not self.line_Opcion.text() == "":
            print("\nDatos limpiados de la ventana Opcion")
            self.line_Opcion_Id.clear()
            self.line_Opcion.clear()


    def notifMensaje(self, indicador, resultado):

        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Error", "Ha Ocurrido un Error")

        '''***********************************************  Usuario   ******************************************'''


    def guardarUsuario(self):

        try:
            # Transformar fecha en formato "yyyy-MM-dd" para hacer la consulta al sql
            fecha = self.line_Usuario_Fecha.text()
            fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
            fechaTransformada = fecha_objeto.strftime("%Y-%m-%d")

            # Programación orientada a objetos

            Usuarios.nombre = self.line_Usuario_Nombre.text()
            Usuarios.apellido = self.line_Usuario_Apellido.text()
            Usuarios.user = self.line_Usuario_User.text()
            Usuarios.password = self.line_Usuario_Password.text()
            Usuarios.fechaCreacion = fechaTransformada

            if self.line_Usuario_Id.text() == "" and not self.line_Usuario_Nombre.text() == "" and not self.line_Usuario_Apellido.text() == "" and not self.line_Usuario_User.text() == "" and not self.line_Usuario_Password.text() == "" and not self.line_Usuario_Fecha.text() == "":

                indicador = dt_usuario.Dt_Usuarios.guardarUsuario(Usuarios)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaUsuario(
                    dt_usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")


    def editarUsuario(self):

        try:

            # Transformar fecha en formato "yyyy-MM-dd" para hacer la consulta al sql
            fecha = self.line_Usuario_Fecha.text()
            fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
            fechaTransformada = fecha_objeto.strftime("%Y-%m-%d")

            Usuarios.id_usuario = self.line_Usuario_Id.text()
            Usuarios.nombre = self.line_Usuario_Nombre.text()
            Usuarios.apellido = self.line_Usuario_Apellido.text()
            Usuarios.user = self.line_Usuario_User.text()
            Usuarios.password = self.line_Usuario_Password.text()
            Usuarios.fechaCreacion = fechaTransformada

            if not self.line_Usuario_Id.text() == "" and not self.line_Usuario_Nombre.text() == "" and not self.line_Usuario_Apellido.text() == "" and not self.line_Usuario_User.text() == "" and not self.line_Usuario_Password.text() == "" and not self.line_Usuario_Fecha.text() == "":

                indicador = dt_usuario.Dt_Usuarios.editarUsuario(
                    Usuarios)  # Recoge los datos en los "Lines" de Qt Desinger para editarlos en la base de datos

                self.notifMensaje(indicador, "Editados")

                self.limpiarCampos()

                self.llenarTablaUsuario(
                    dt_usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()


        except Exception as e:
            print(f"Error: {e}")


    def eliminarUsuario(self):

        try:

            Usuarios.id_usuario = self.line_Usuario_Id.text()

            if not self.line_Usuario_Id.text() == "" and not self.line_Usuario_Nombre.text() == "" and not self.line_Usuario_Apellido.text() == "" and not self.line_Usuario_User.text() == "" and not self.line_Usuario_Password.text() == "" and not self.line_Usuario_Fecha.text() == "":

                indicador = dt_usuario.Dt_Usuarios.eliminarUsuario(Usuarios)

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaUsuario(
                    dt_usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()


        except Exception as e:
            print(f"Error: {e}")


    def obtenerDatosTablaUsuario(self):

        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Usuario.currentRow()
        id = self.tb_Usuario.item(filaSeleccionada, 0).text()
        nombre = self.tb_Usuario.item(filaSeleccionada, 1).text()
        apellido = self.tb_Usuario.item(filaSeleccionada, 2).text()
        username = self.tb_Usuario.item(filaSeleccionada, 3).text()
        clave = self.tb_Usuario.item(filaSeleccionada, 4).text()
        fecha = self.tb_Usuario.item(filaSeleccionada, 5).text()

        # Tramsformar la fecha en formato "yyyy-MM-dd"
        fechaTransformada = QDate.fromString(fecha, "yyyy-MM-dd")

        # Asigna el contenido de la tabla seleccionada a los Edits Lines Correspondientes
        self.line_Usuario_Id.setText(id)
        self.line_Usuario_Nombre.setText(nombre)
        self.line_Usuario_Apellido.setText(apellido)
        self.line_Usuario_User.setText(username)
        self.line_Usuario_Password.setText(clave)
        self.line_Usuario_Fecha.setDate(fechaTransformada)


    def llenarTablaUsuario(self, datos):

        vacio = ""
        print("\nDatos de la Tablas Usuarios")
        i = len(datos)
        self.tb_Usuario.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.tb_Usuario.setItem(tablerow, 0, QTableWidgetItem(str(row["id_usuario"])))
            self.tb_Usuario.setItem(tablerow, 1, QTableWidgetItem((row["nombre"])))
            self.tb_Usuario.setItem(tablerow, 2, QTableWidgetItem((row["apellido"])))
            self.tb_Usuario.setItem(tablerow, 3, QTableWidgetItem((row["user"])))
            self.tb_Usuario.setItem(tablerow, 4, QTableWidgetItem((row["clave"])))
            self.tb_Usuario.setItem(tablerow, 5, QTableWidgetItem(str(row["fecha_creacion"])))
            self.tb_Usuario.setItem(tablerow, 6, QTableWidgetItem(str(row["estado"])))
            tablerow = tablerow + 1


        '''******************************************  Rol   ******************************************'''


    def guardarRol(self):

        try:

            Rol.rol = self.line_Rol.text()

            if self.line_Rol_Id.text() == "" and not self.line_Rol.text() == "":

                indicador = dt_rol.Dt_Rol.guardarRol(Rol)

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaRol(
                    dt_rol.Dt_Rol.listarRol())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error: {e}")


    def editarRol(self):

        try:
            Rol.id_rol = self.line_Rol_Id.text()
            Rol.rol = self.line_Rol.text()

            if not self.line_Rol_Id.text() == "" and not self.line_Rol.text() == "":

                indicador = dt_rol.Dt_Rol.editarRol(Rol)

                self.notifMensaje(indicador, "Editados")

                self.limpiarCampos()

                self.llenarTablaRol(
                    dt_rol.Dt_Rol.listarRol())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()


        except Exception as e:
            print(f"Error: {e}")


    def eliminarRol(self):

        try:
            Rol.id_rol = self.line_Rol_Id.text()

            if not self.line_Rol_Id.text() == "" and not self.line_Rol.text() == "":

                indicador = dt_rol.Dt_Rol.eliminarRol(Rol)

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaRol(
                    dt_rol.Dt_Rol.listarRol())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()


        except Exception as e:
            print(f"Error: {e}")


    def obtenerDatosTablaRol(self):

        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Rol.currentRow()
        id = self.tb_Rol.item(filaSeleccionada, 0).text()
        rol = self.tb_Rol.item(filaSeleccionada, 1).text()

        # Asigna el contenido de la tabla seleccionada a los Edits Lines Correspondientes
        self.line_Rol_Id.setText(id)
        self.line_Rol.setText(rol)


    def llenarTablaRol(self, datos):

        print("\nDatos de la Tabla rol")
        i = len(datos)
        self.tb_Rol.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Rol.setItem(tablerow, 0, QTableWidgetItem(str(row["id_rol"])))
            self.tb_Rol.setItem(tablerow, 1, QTableWidgetItem((row["descripcion"])))
            tablerow = tablerow + 1


        '''******************************************  Opcion   ******************************************'''


    def guardarOpcion(self):

        try:

            Opcion.opcion = self.line_Opcion.text()

            if self.line_Opcion_Id.text() == "" and not self.line_Opcion.text() == "":

                indicador = dt_opcion.Dt_Opcion.guardarOpcion(Opcion)

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaOpcion(
                    dt_opcion.Dt_Opcion.listarOpcion())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error: {e}")


    def editarOpcion(self):

        try:
            Opcion.idOpcion = self.line_Opcion_Id.text()
            Opcion.opcion = self.line_Opcion.text()

            if not self.line_Opcion_Id.text() == "" and not self.line_Opcion.text() == "":

                indicador = dt_opcion.Dt_Opcion.editarOpcion(Opcion)

                self.notifMensaje(indicador, "Editados")

                self.limpiarCampos()

                self.llenarTablaOpcion(
                    dt_opcion.Dt_Opcion.listarOpcion())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")


    def eliminarOpcion(self):

        try:
            Opcion.idOpcion = self.line_Opcion_Id.text()

            if not self.line_Opcion_Id.text() == "" and not self.line_Opcion.text() == "":

                indicador = dt_opcion.Dt_Opcion.eliminarOpcion(Opcion)

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaOpcion(
                    dt_opcion.Dt_Opcion.listarOpcion())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")


    def obtenerDatosTablaOpcion(self):

        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Opcion.currentRow()
        id = self.tb_Opcion.item(filaSeleccionada, 0).text()
        opcion = self.tb_Opcion.item(filaSeleccionada, 1).text()

        # Asigna el contenido de la tabla seleccionada a los Edits Lines Correspondientes
        self.line_Opcion_Id.setText(id)
        self.line_Opcion.setText(opcion)


    def llenarTablaOpcion(self, datos):

        print("\nDatos de la Tabla opcion")
        i = len(datos)
        self.tb_Opcion.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Opcion.setItem(tablerow, 0, QTableWidgetItem(str(row["idopcion"])))
            self.tb_Opcion.setItem(tablerow, 1, QTableWidgetItem((row["descripcion"])))
            tablerow = tablerow + 1

        '''******************************************  Asignar Rol y Opcion   ******************************************'''

    def llenarComboxRoles(self, datos):
        print("\nDatos de la combo box Rol")
        i = len(datos)

        for registro in datos:
            print(registro)
            self.cb_Asignar_Rol_idRol.addItem(registro["descripcion"],registro["id_rol"])
            self.cb_Asignar_Opcion_idRol.addItem(registro["descripcion"], registro["id_rol"])


    def llenarComboxUsuarios(self, datos):
        print("\nDatos de la Combo Box Usuarios")
        i = len(datos)

        for registro in datos:
            print(registro)
            self.cb_Asignar_Rol_idUsuario.addItem(registro["user"],registro["id_usuario"])


    def llenarComboxOpcion(self, datos):
        print("\nDatos de la combo box Opcion")

        for registro in datos:
            print(registro)
            self.cb_Asignar_Opcion_idOpcion.addItem(registro["descripcion"],registro["idopcion"])


    # Tablas

    def llenarTablaUsuarioRol(self, datos):
        print("\nDatos de la Tabla Asignar Rol")
        i = len(datos)
        self.tb_Asignar_Rol.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Asignar_Rol.setItem(tablerow, 0, QTableWidgetItem(str(row["usuario_rol_id"])))

            self.tb_Asignar_Rol.setItem(tablerow, 1, QTableWidgetItem(str(row["id_usuario"])))

            self.tb_Asignar_Rol.setItem(tablerow, 2, QTableWidgetItem(str(row["id_rol"])))
            tablerow = tablerow + 1

    def llenarTablaRolOpcion(self, datos):
        print("\nDatos de la Tabla Asignar Opcion")
        i = len(datos)
        self.tb_Asignar_Opcion.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Asignar_Opcion.setItem(tablerow, 0, QTableWidgetItem(str(row["rol_opcion_id"])))

            self.tb_Asignar_Opcion.setItem(tablerow, 1, QTableWidgetItem(str(row["id_rol"])))

            self.tb_Asignar_Opcion.setItem(tablerow, 2, QTableWidgetItem(str(row["id_opcion"])))
            tablerow = tablerow + 1

    def guardarUsuarioRol(self):
        try:

            usuario_rol.id_rol = self.cb_Asignar_Rol_idRol.itemData(self.cb_Asignar_Rol_idRol.currentIndex())

            usuario_rol.id_usuario = self.cb_Asignar_Rol_idUsuario.itemData(self.cb_Asignar_Rol_idUsuario.currentIndex())

            indicador = dt_usuario_rol.Dt_Usuario_rol.guardarUsuarioRol(usuario_rol)


            self.llenarTablaUsuarioRol(dt_usuario_rol.Dt_Usuario_rol.listarUsuario_rol())


        except Exception as e:
            print(f"ERROR en guardarUsuarioRol: {e}")

    def guardarRolOpcion(self):
        try:

            Rol_opcion.id_rol = self.cb_Asignar_Opcion_idRol.itemData(self.cb_Asignar_Opcion_idRol.currentIndex())

            Rol_opcion.id_opcion = self.cb_Asignar_Opcion_idOpcion.itemData(
                    self.cb_Asignar_Opcion_idOpcion.currentIndex())

            indicador = dt_rol_opcion.Dt_rol_opcion.guardarRolOpcion(Rol_opcion)

            self.llenarTablaRolOpcion(dt_rol_opcion.Dt_rol_opcion.listarRolOpcion())


        except Exception as e:
            print(f"ERROR en guardarRolOpcion: {e}")

        '''******************************************  Menu Principal   ******************************************'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = seguridad_Window()
    mw.show()
    app.exec()
