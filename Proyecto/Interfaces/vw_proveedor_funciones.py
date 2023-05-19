#Francisco de Jesús Meléndez Simplina


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from Datos import dt_proveedor
from Entidades.proveedores import Proveedor
from Interfaces import vw_proveedor


class proveedor_Window(QMainWindow, vw_proveedor.Ui_Proveedores):

    def __init__(self, parent=None):
        super(proveedor_Window, self).__init__(parent)
        self.setupUi(self)

        #Tabla
        self.llenarTablaProveedor(dt_proveedor.Dt_Proveedor.listarProveedor())
        self.tb_Proveedor.itemSelectionChanged.connect(self.obtenerDatosTablaProveedor)

        #Botones
        self.bt_Guardar.clicked.connect(self.guardarProveedor)
        self.bt_Vaciar.clicked.connect(self.limpiarCampos)
        self.bt_Editar.clicked.connect(self.editarProveedor)
        self.bt_Eliminar.clicked.connect(self.eliminarProveedor)



    def limpiarCampos(self):
        self.line_Id.setText("")
        self.line_Nombre.setText("")
        self.line_Ruc.setText("")
        self.line_Correo.setText("")
        self.line_Catalogo.setText("")
        self.line_Direccion.setText("")
        self.line_Telefono.setText("")

    def obtenerDatosTablaProveedor(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Proveedor.currentRow()

        id = self.tb_Proveedor.item(filaSeleccionada, 0).text()
        nombre = self.tb_Proveedor.item(filaSeleccionada, 1).text()
        email = self.tb_Proveedor.item(filaSeleccionada, 2).text()
        telefono = self.tb_Proveedor.item(filaSeleccionada, 3).text()
        catalogo = self.tb_Proveedor.item(filaSeleccionada, 4).text()
        ruc = self.tb_Proveedor.item(filaSeleccionada, 5).text()
        direccion = self.tb_Proveedor.item(filaSeleccionada, 6).text()

        self.line_Id.setText(id)
        self.line_Nombre.setText(nombre)
        self.line_Correo.setText(email)
        self.line_Telefono.setText(telefono)
        self.line_Catalogo.setText(catalogo)
        self.line_Ruc.setText(ruc)
        self.line_Direccion.setText(direccion)

    def notifMensaje(self, indicador, resultado):

        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Error", "Ha Ocurrido un Error")



    def llenarTablaProveedor(self, datos):
        print("\nDatos de la Tabla Proveedor")
        i = len(datos)
        self.tb_Proveedor.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Proveedor.setItem(tablerow, 0, QTableWidgetItem(str(row["id_proveedor"])))
            self.tb_Proveedor.setItem(tablerow, 1, QTableWidgetItem((row["nombre"])))
            self.tb_Proveedor.setItem(tablerow, 2, QTableWidgetItem(str(row["ruc"])))
            self.tb_Proveedor.setItem(tablerow, 3, QTableWidgetItem((row["email"])))
            self.tb_Proveedor.setItem(tablerow, 4, QTableWidgetItem(str(row["catalogo"])))
            self.tb_Proveedor.setItem(tablerow, 5, QTableWidgetItem((row["telefono"])))
            self.tb_Proveedor.setItem(tablerow, 6, QTableWidgetItem(str(row["direccion"])))
            tablerow = tablerow + 1

    def guardarProveedor(self):

        try:
            Proveedor.nombre = self.line_Nombre.text()
            Proveedor.correo = self.line_Correo.text()
            Proveedor.direccion = self.line_Direccion.toPlainText()
            Proveedor.catalogo = self.line_Catalogo.toPlainText()
            Proveedor.ruc = self.line_Ruc.text()
            Proveedor.telefono = self.line_Telefono.text()


            if self.line_Id.text() == "" and not self.line_Nombre.text() == "" and not self.line_Correo.text() == "" and not self.line_Ruc.text() == "" and not self.line_Telefono.text() == "" and not self.line_Direccion.toPlainText() == "" and not self.line_Catalogo.toPlainText() == "":
                indicador = dt_proveedor.Dt_Proveedor.guardarProveedor(Proveedor)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaProveedor(dt_proveedor.Dt_Proveedor.listarProveedor())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en GuardarProveedor: {e}")


    def editarProveedor(self):

        try:
            Proveedor.id_proveedor = self.line_Id.text()
            Proveedor.nombre = self.line_Nombre.text()
            Proveedor.correo = self.line_Correo.text()
            Proveedor.direccion = self.line_Direccion.toPlainText()
            Proveedor.catalogo = self.line_Catalogo.toPlainText()
            Proveedor.ruc = self.line_Ruc.text()
            Proveedor.telefono = self.line_Telefono.text()


            if not self.line_Id.text() == "" and not self.line_Nombre.text() == "" and not self.line_Correo.text() == "" and not self.line_Ruc.text() == "" and not self.line_Telefono.text() == "" and not self.line_Direccion.toPlainText() == "" and not self.line_Catalogo.toPlainText() == "":
                indicador = dt_proveedor.Dt_Proveedor.editarProveedor(Proveedor)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Editados")

                self.limpiarCampos()

                self.llenarTablaProveedor(dt_proveedor.Dt_Proveedor.listarProveedor())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en EditarProveedor: {e}")


    def eliminarProveedor(self):

        try:
            Proveedor.id_proveedor = self.line_Id.text()

            if not self.line_Id.text() == "" :
                indicador = dt_proveedor.Dt_Proveedor.eliminarProveedor(Proveedor)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaProveedor(dt_proveedor.Dt_Proveedor.listarProveedor())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en EliminarProveedor: {e}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = proveedor_Window()
    mw.show()
    app.exec()