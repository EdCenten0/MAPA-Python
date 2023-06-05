#Francisco de Jesús Meléndez Simplina


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from Proyecto.Datos import dt_proveedor
from Proyecto.Entidades.proveedores import Proveedor
from Proyecto.Interfaces import vw_proveedor


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
        self.line_id.setText("")
        self.line_nombre.setText("")
        self.line_ruc.setText("")
        self.line_correo.setText("")
        self.line_catalogo.setText("")
        self.line_direccion.setText("")
        self.line_telefono.setText("")

    def obtenerDatosTablaProveedor(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Proveedor.currentRow()

        id = self.tb_Proveedor.item(filaSeleccionada, 0).text()
        nombre = self.tb_Proveedor.item(filaSeleccionada, 1).text()
        ruc = self.tb_Proveedor.item(filaSeleccionada, 2).text()
        email = self.tb_Proveedor.item(filaSeleccionada, 3).text()
        catalogo = self.tb_Proveedor.item(filaSeleccionada, 4).text()
        telefono = self.tb_Proveedor.item(filaSeleccionada, 5).text()
        direccion = self.tb_Proveedor.item(filaSeleccionada, 6).text()

        self.line_id.setText(id)
        self.line_nombre.setText(nombre)
        self.line_correo.setText(email)
        self.line_telefono.setText(telefono)
        self.line_catalogo.setText(catalogo)
        self.line_ruc.setText(ruc)
        self.line_direccion.setText(direccion)

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

        #Validaciones de entrada de datos

        if self.line_id.text() == "":

            if self.validacionCampos():

                try:
                    Proveedor.nombre = self.line_nombre.text()
                    Proveedor.correo = self.line_correo.text()
                    Proveedor.direccion = self.line_direccion.toPlainText()
                    Proveedor.catalogo = self.line_catalogo.toPlainText()
                    Proveedor.ruc = self.line_ruc.text()
                    Proveedor.telefono = self.line_telefono.text()

                    dt_proveedor.Dt_Proveedor.guardarProveedor(
                        Proveedor)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                    QMessageBox.about(self, "Registro Exitoso", "Se guardo correctamente el proveedor")

                    self.limpiarCampos()

                    self.llenarTablaProveedor(
                        dt_proveedor.Dt_Proveedor.listarProveedor())  # Se reinicia la tabla para poder recargar los datos guardados

                except Exception as e:
                    print(f"Error en GuardarProveedor: {e}")

        else:
            QMessageBox.about(self,"Error" ,"No se pudo guardar a este proveedor con un id existente")






    def editarProveedor(self):

        if not self.line_id.text() == "":

            if self.validacionCampos():
                try:
                    Proveedor.id_proveedor = self.line_id.text()
                    Proveedor.nombre = self.line_nombre.text()
                    Proveedor.correo = self.line_correo.text()
                    Proveedor.direccion = self.line_direccion.toPlainText()
                    Proveedor.catalogo = self.line_catalogo.toPlainText()
                    Proveedor.ruc = self.line_ruc.text()
                    Proveedor.telefono = self.line_telefono.text()

                    dt_proveedor.Dt_Proveedor.editarProveedor(
                        Proveedor)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                    QMessageBox.about(self, "Registro Exitoso", "Se edito correctamente el proveedor")

                    self.limpiarCampos()

                    self.llenarTablaProveedor(
                        dt_proveedor.Dt_Proveedor.listarProveedor())  # Se reinicia la tabla para poder recargar los datos guardados

                except Exception as e:
                    print(f"Error en EditarProveedor: {e}")

        else:
            QMessageBox.about(self,"Error" ,"Seleccione al proveedor a editar")





    def eliminarProveedor(self):

        try:

            if not self.line_id.text() == "" :

                Proveedor.id_proveedor = self.line_id.text()

                dt_proveedor.Dt_Proveedor.eliminarProveedor(Proveedor)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                QMessageBox.about(self, "Registro Exitoso", "Se elimino correctamente el proveedor")

                self.limpiarCampos()

                self.llenarTablaProveedor(dt_proveedor.Dt_Proveedor.listarProveedor())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                QMessageBox.about(self, "Error", "Seleccione al proveedor a eliminar")


        except Exception as e:
            print(f"Error en EliminarProveedor: {e}")


    def validacionCampos(self):
        validacion = False

        if (not self.line_nombre.text() == "" and not self.line_correo.text() == "" and not self.line_direccion.toPlainText() == "" and not self.line_catalogo.toPlainText() == "" and not self.line_ruc.text() == "" and not self.line_telefono.text() == ""):

            if len(self.line_nombre.text()) <= 50:

                if len(self.line_correo.text()) <= 50:

                    if len(self.line_ruc.text()) <= 15:

                        if len(self.line_telefono.text()) <= 12:

                            if len(self.line_catalogo.toPlainText()) <= 100:

                                if len(self.line_direccion.toPlainText()) <= 300:
                                    validacion = True

                                else:
                                    QMessageBox.about(self, "Error", "La direccion debe tener menos de 300 caracteres")

                            else:
                                QMessageBox.about(self, "Error", "El catalogo debe tener menos de 100 caracteres")

                        else:
                            QMessageBox.about(self, "Error", "El telefono debe tener menos de 12 caracteres")

                    else:
                        QMessageBox.about(self, "Error", "El ruc debe tener menos de 15 caracteres")

                else:
                    QMessageBox.about(self, "Error", "El correo electronico debe tener menos de 50 caracteres")

            else:
                QMessageBox.about(self, "Error", "El nombre del proveedor debe tener menos de 50 caracteres")

        else:
            QMessageBox.about(self, "Error", "Llene los campos vacios")

        return validacion




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = proveedor_Window()
    mw.show()
    app.exec()