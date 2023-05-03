# Francisco de Jesús Melendez Simplina

import sys
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

from Datos import dt_Usuario, dt_Rol, dt_Opcion


# Indicador obtiende de las carpeta de las clases de Datos, un valor verdadero o falso para asi poder mostrar un mensaje de confirmación ya se ha guardar, editar o eliminar datos


class Form_Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Form_Principal,self).__init__()
        loadUi("./VentanaPrincipal.ui",self)

        #Acciones de botones

        #Botones de Usuario
        self.bt_Guardar_Usuario.clicked.connect(self.guardarUsuario)
        self.bt_Editar_Usuario.clicked.connect(self.editarUsuario)
        self.bt_Eliminar_Usuario.clicked.connect(self.eliminarUsuario)
        self.bt_Vaciar_Usuario.clicked.connect(self.limpiarCampos)

        #Botones de Rol
        self.bt_Guardar_Rol.clicked.connect(self.guardarRol)
        self.bt_Editar_Rol.clicked.connect(self.editarRol)
        self.bt_Eliminar_Rol.clicked.connect(self.eliminarRol)
        self.bt_Vaciar_Rol.clicked.connect(self.limpiarCampos)

        #Botones de Opcion
        self.bt_Guardar_Opcion.clicked.connect(self.guardarOpcion)
        self.bt_Editar_Opcion.clicked.connect(self.editarOpcion)
        self.bt_Eliminar_Opcion.clicked.connect(self.eliminarOpcion)
        self.bt_Vaciar_Opcion.clicked.connect(self.limpiarCampos)


        #Acciones de las tablas

        #Usuarios
        self.llenarTablaUsuario(dt_Usuario.Dt_Usuarios.listarUsuarios())
        self.tb_Usuario.itemSelectionChanged.connect(self.obtenerDatosTablaUsuario)

        #Roles
        self.llenarTablaRol(dt_Rol.Dt_Rol.listarRol())
        self.tb_Rol.itemSelectionChanged.connect(self.obtenerDatosTablaRol)

        # Opciones
        self.llenarTablaOpcion(dt_Opcion.Dt_Opcion.listarOpcion())
        self.tb_Opcion.itemSelectionChanged.connect(self.obtenerDatosTablaOpcion)


    '''***********************************************  Funciones reutilizables   ******************************************'''


    def limpiarCampos(self):

        if not self.line_Usuario_Nombre.text() == "" or not self.line_Usuario_Apellido.text() == "" or not self.line_Usuario_User.text() == "" or not self.line_Usuario_Password.text() == "" :
            print("Datos limpiados de la ventana Usuario")
            self.line_Usuario_Id.clear()
            self.line_Usuario_Nombre.clear()
            self.line_Usuario_Apellido.clear()
            self.line_Usuario_User.clear()
            self.line_Usuario_Password.clear()

        #Rol
        if not self.line_Rol_Id.text() == "" or not self.line_Rol.text() == "":
            print("Datos limpiados de la ventana Rol")
            self.line_Rol_Id.clear()
            self.line_Rol.clear()

        #Opcion
        if not self.line_Opcion_Id.text() == "" or not self.line_Opcion.text() == "":
            print("Datos limpiados de la ventana Opcion")
            self.line_Opcion_Id.clear()
            self.line_Opcion.clear()




    def notifMensaje(self, indicador, resultado):

        if indicador == True: #Se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:#No se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Error", "Ha Ocurrido un Error")


        '''***********************************************  Usuario   ******************************************'''

    def guardarUsuario(self):

        try:
            #Transformar fecha en formato "yyyy-MM-dd" para hacer la consulta al sql
            fecha = self.line_Usuario_Fecha.text()
            fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
            fechaTransformada = fecha_objeto.strftime("%Y-%m-%d")

            if self.line_Usuario_Id.text()== "" and not self.line_Usuario_Nombre.text()== "" and not self.line_Usuario_Apellido.text()== "" and not self.line_Usuario_User.text()== "" and not self.line_Usuario_Password.text()== "" and not self.line_Usuario_Fecha.text()== "":

                indicador = dt_Usuario.Dt_Usuarios.guardarUsuario(self.line_Usuario_Nombre.text(),self.line_Usuario_Apellido.text(),self.line_Usuario_User.text(),self.line_Usuario_Password.text(), fechaTransformada)  # Recoge los datos en los "Lines" de Qt Desinger para editarlos en la base de datos

                self.notifMensaje(indicador,"Guardados")

                self.limpiarCampos()

                self.llenarTablaUsuario(dt_Usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")



    def editarUsuario(self):

        try:

            #Transformar fecha en formato "yyyy-MM-dd" para hacer la consulta al sql
            fecha = self.line_Usuario_Fecha.text()
            fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
            fechaTransformada = fecha_objeto.strftime("%Y-%m-%d")

            if not self.line_Usuario_Id.text()== "" and not self.line_Usuario_Nombre.text()== "" and not self.line_Usuario_Apellido.text()== "" and not self.line_Usuario_User.text()== "" and not self.line_Usuario_Password.text()== "" and not self.line_Usuario_Fecha.text()== "":

                indicador = dt_Usuario.Dt_Usuarios.editarUsuario(self.line_Usuario_Id.text(),self.line_Usuario_Nombre.text(),self.line_Usuario_Apellido.text(),self.line_Usuario_User.text(),self.line_Usuario_Password.text(), fechaTransformada)  # Recoge los datos en los "Lines" de Qt Desinger para editarlos en la base de datos

                self.notifMensaje(indicador,"Editados")

                self.limpiarCampos()

                self.llenarTablaUsuario(dt_Usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")



    def eliminarUsuario(self):

        try:

            if not self.line_Usuario_Id.text()== "" and not self.line_Usuario_Nombre.text()== "" and not self.line_Usuario_Apellido.text()== "" and not self.line_Usuario_User.text()== "" and not self.line_Usuario_Password.text()== "" and not self.line_Usuario_Fecha.text()== "":

                indicador = dt_Usuario.Dt_Usuarios.eliminarUsuario(self.line_Usuario_Id.text())

                self.notifMensaje(indicador,"Eliminados")

                self.limpiarCampos()

                self.llenarTablaUsuario(dt_Usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")



    def obtenerDatosTablaUsuario(self):

        #Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Usuario.currentRow()
        id = self.tb_Usuario.item(filaSeleccionada, 0).text()
        nombre = self.tb_Usuario.item(filaSeleccionada, 1).text()
        apellido = self.tb_Usuario.item(filaSeleccionada, 2).text()
        username = self.tb_Usuario.item(filaSeleccionada, 3).text()
        clave = self.tb_Usuario.item(filaSeleccionada, 4).text()
        fecha = self.tb_Usuario.item(filaSeleccionada, 5).text()

        #Tramsformar la fecha en formato "yyyy-MM-dd"
        fechaTransformada = QDate.fromString(fecha, "yyyy-MM-dd")

        #Asigna el contenido de la tabla seleccionada a los Edits Lines Correspondientes
        self.line_Usuario_Id.setText(id)
        self.line_Usuario_Nombre.setText(nombre)
        self.line_Usuario_Apellido.setText(apellido)
        self.line_Usuario_User.setText(username)
        self.line_Usuario_Password.setText(clave)
        self.line_Usuario_Fecha.setDate(fechaTransformada)



    def llenarTablaUsuario(self, datos):

        print("Datos de la Tablas Usuarios")
        i = len(datos)
        self.tb_Usuario.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Usuario.setItem(tablerow, 0, QTableWidgetItem(str(row["idusuario"])))
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

            if self.line_Rol_Id.text() == "" and not self.line_Rol.text() == "":

                indicador = dt_Rol.Dt_Rol.guardarRol(self.line_Rol.text())

                self.notifMensaje(indicador,"Guardados")

                self.limpiarCampos()

                self.llenarTablaRol(dt_Rol.Dt_Rol.listarRol())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")

        except Exception as e:
            print(f"Error: {e}")



    def editarRol(self):

        try:

            if not self.line_Rol_Id.text() == "" and not self.line_Rol.text() == "":

                indicador = dt_Rol.Dt_Rol.editarRol(self.line_Rol_Id.text(),self.line_Rol.text())

                self.notifMensaje(indicador,"Editados")

                self.limpiarCampos()

                self.llenarTablaRol(dt_Rol.Dt_Rol.listarRol())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")



    def eliminarRol(self):

        try:

            if not self.line_Rol_Id.text() == "" and not self.line_Rol.text() == "":

                indicador = dt_Rol.Dt_Rol.eliminarRol(self.line_Rol_Id.text())

                self.notifMensaje(indicador,"Eliminados")

                self.limpiarCampos()

                self.llenarTablaRol(dt_Rol.Dt_Rol.listarRol())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")



    def obtenerDatosTablaRol(self):

        #Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Rol.currentRow()
        id = self.tb_Rol.item(filaSeleccionada, 0).text()
        rol = self.tb_Rol.item(filaSeleccionada, 1).text()

        #Asigna el contenido de la tabla seleccionada a los Edits Lines Correspondientes
        self.line_Rol_Id.setText(id)
        self.line_Rol.setText(rol)



    def llenarTablaRol(self, datos):

        print("Datos de la Tabla rol")
        i = len(datos)
        self.tb_Rol.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Rol.setItem(tablerow, 0, QTableWidgetItem(str(row["idrol"])))
            self.tb_Rol.setItem(tablerow, 1, QTableWidgetItem((row["descripcion"])))
            tablerow = tablerow + 1

        '''******************************************  Opcion   ******************************************'''

    def guardarOpcion(self):

        try:

            if self.line_Opcion_Id.text() == "" and not self.line_Opcion.text() == "":

                indicador = dt_Opcion.Dt_Opcion.guardarOpcion(self.line_Opcion.text())

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaOpcion(dt_Opcion.Dt_Opcion.listarOpcion())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")

        except Exception as e:
            print(f"Error: {e}")



    def editarOpcion(self):

        try:

            if not self.line_Opcion_Id.text() == "" and not self.line_Opcion.text() == "":

                indicador = dt_Opcion.Dt_Opcion.editarOpcion(self.line_Opcion_Id.text(), self.line_Opcion.text())

                self.notifMensaje(indicador, "Editados")

                self.limpiarCampos()

                self.llenarTablaOpcion(dt_Opcion.Dt_Opcion.listarOpcion())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")


        except Exception as e:
            print(f"Error: {e}")



    def eliminarOpcion(self):

        try:

            if not self.line_Opcion_Id.text() == "" and not self.line_Opcion.text() == "":

                indicador = dt_Opcion.Dt_Opcion.eliminarOpcion(self.line_Opcion_Id.text())

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaOpcion(dt_Opcion.Dt_Opcion.listarOpcion())  # Se reinicia la tabla para poder recargar los datos guardados

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

        print("Datos de la Tabla opcion")
        i = len(datos)
        self.tb_Opcion.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Opcion.setItem(tablerow, 0, QTableWidgetItem(str(row["idopcion"])))
            self.tb_Opcion.setItem(tablerow, 1, QTableWidgetItem((row["descripcion"])))
            tablerow = tablerow + 1



        '''******************************************  Menu Principal   ******************************************'''



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aplicacion = Form_Principal()
    aplicacion.show()
    app.exec()