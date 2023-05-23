


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from Proyecto.Datos import dt_cliente
from Proyecto.Entidades import clientes



class cliente_Window(QMainWindow, vw_cliente.Ui_Cliente):

    def __init__(self, parent=None):
        super(cliente_Window, self).__init__(parent)
        self.setupUi(self)

        #Tabla
        self.llenarTablaCliente(dt_cliente.Dt_cliente.listarCliente())
        self.tb_cliente.itemSelectionChanged.connect(self.obtenerDatosTablaCliente)

        #Botones
        self.bt_Guardar_Cliente.clicked.connect(self.guardarCliente)
        self.bt_Vaciar_Cliente.clicked.connect(self.limpiarCampos)


    def limpiarCampos(self):
        self.line_Cliente_Nombre.setText("")
        self.line_Cliente_Apellido.setText("")
        self.line_Cliente_Cedula.setText("")
        self.line_Cliente_Direccion.setText("")
        self.line_Cliente_Correo.setText("")
        self.line_Cliente_Telefono.setText("")

    def obtenerDatosTablaCliente(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Cliente.currentRow()


        nombre = self.tb_Cliente.item(filaSeleccionada, 1).text()
        apellido = self.tb_Cliente.item(filaSeleccionada, 2).text()
        cedula = self.tb_Cliente.item(filaSeleccionada, 3).text()
        direccion = self.tb_Cliente.item(filaSeleccionada, 4).text()
        correo = self.tb_Cliente.item(filaSeleccionada, 5).text()
        telefono = self.tb_Cliente.item(filaSeleccionada, 6).text()


        self.line_Cliente_Nombre.setText(nombre)
        self.line_Cliente_Apellido.setText(apellido)
        self.line_Cliente_Cedula.setText(cedula)
        self.line_Cliente_Direccion.setText(direccion)
        self.line_Cliente_Correo.setText(correo)
        self.line_Cliente_Telefono.setText(telefono)

    def notifMensaje(self, indicador, resultado):

        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Error", "Ha Ocurrido un Error")



    def llenarTablaCliente(self, datos):
        print("\nDatos de la Tabla Proveedor")
        i = len(datos)
        self.tb_Cliente.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Cliente.setItem(tablerow, 0, QTableWidgetItem(str(row["nombre"])))
            self.tb_Cliente.setItem(tablerow, 1, QTableWidgetItem((row["apellido"])))
            self.tb_Cliente.setItem(tablerow, 2, QTableWidgetItem(str(row["cedula"])))
            self.tb_Cliente.setItem(tablerow, 3, QTableWidgetItem((row["direccion"])))
            self.tb_Cliente.setItem(tablerow, 4, QTableWidgetItem(str(row["correo"])))
            self.tb_Cliente.setItem(tablerow, 5, QTableWidgetItem((row["telefono"])))
            tablerow = tablerow + 1

    def guardarCliente(self):

        try:
            clientes.nombre = self.line_Nombre.text()
            clientes.apellido = self.line_Correo.text()
            clientes.cedula = self.line_Direccion.toPlainText()
            clientes.direccion = self.line_Catalogo.toPlainText()
            clientes.correo = self.line_Ruc.text()
            clientes.telefono = self.line_Telefono.text()


            if self.line_Cliente_Nombre.text() == "" and not self.line_Cliente_Apellido.text() == "" and not self.line_Cliente_Cedula.text() == "" and not self.line_Cliente_Direccion.text() == "" and not self.line_Cliente_Correo.toPlainText() == "" and not self.line_Cliente_Telefono.toPlainText() == "":
                indicador = dt_cliente.Dt_Cliente.guardarCliente(clientes)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaUsuario(dt_cliente.Dt_cliente.listarCliente())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en GuardarProveedor: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = cliente_Window()
    mw.show()
    app.exec()