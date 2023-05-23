


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from Proyecto.Interfaces import vw_Cliente
from Proyecto.Datos import dt_cliente
from Proyecto.Entidades import clientes
from Proyecto.Datos import Conexion




class cliente_Window(QMainWindow, vw_Cliente.Ui_MainWindow):

    def __init__(self, parent=None):
        super(cliente_Window, self).__init__(parent)
        self.setupUi(self)

        #Tabla
        self.llenarTablaCliente(dt_cliente.Dt_Clientes.listarClientes())
        self.tb_Cliente.itemSelectionChanged.connect(self.obtenerDatosTablaCliente)

        #Botones
        self.bt_Guardar_Cliente.clicked.connect(self.guardarCliente)
        self.bt_Vaciar_Cliente.clicked.connect(self.limpiarCampos)


    def limpiarCampos(self):
        self.line_Cliente_Nombre.setText("")
        self.line_Cliente_Apellido_5.setText("")
        self.line_Cliente_Apellido_4.setText("")
        self.line_Cliente_Apellido_3.setText("")
        self.line_Cliente_Apellido_2.setText("")
        self.line_Cliente_Apellido.setText("")
        self.line_Cliente_Direccion.setText("")

    def obtenerDatosTablaCliente(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Cliente.currentRow()

        id = self.tb_Cliente.item(filaSeleccionada, 0).text()
        nombre = self.tb_Cliente.item(filaSeleccionada, 1).text()
        apellido = self.tb_Cliente.item(filaSeleccionada, 2).text()
        cedula = self.tb_Cliente.item(filaSeleccionada, 3).text()
        email = self.tb_Cliente.item(filaSeleccionada, 4).text()
        telefono = self.tb_Cliente.item(filaSeleccionada, 5).text()
        id_tienda = self.tb_Cliente.item(filaSeleccionada, 6).text()
        estado = self.tb_Cliente.item(filaSeleccionada, 6).text()

        self.line_Cliente_Nombre.setText(id)
        self.line_Cliente_Apellido_5.setText(nombre)
        self.line_Cliente_Apellido.setText(apellido)
        self.line_Cliente_Apellido_2.setText(cedula)
        self.line_Cliente_Apellido_4.setText(email)
        self.line_Cliente_Apellido_3.setText(telefono)
        self.line_Cliente_Direccion.setText(id_tienda)
        self.line_Cliente_Direccion.setText(estado)
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
            self.tb_Cliente.setItem(tablerow, 0, QTableWidgetItem(str(row["id"])))
            self.tb_Cliente.setItem(tablerow, 1, QTableWidgetItem(str(row["nombre"])))
            self.tb_Cliente.setItem(tablerow, 2, QTableWidgetItem((row["apellido"])))
            self.tb_Cliente.setItem(tablerow, 3, QTableWidgetItem(str(row["cedula"])))
            self.tb_Cliente.setItem(tablerow, 4, QTableWidgetItem(str(row["email"])))
            self.tb_Cliente.setItem(tablerow, 5, QTableWidgetItem((row["telefono"])))
            self.tb_Cliente.setItem(tablerow, 6, QTableWidgetItem(str(row["id_tienda"])))
            tablerow = tablerow + 1

    def guardarCliente(self):

        try:
            clientes.id = self.line_Cliente_Nombre.text()
            clientes.nombre = self.line_Cliente_Apellido_5.text()
            clientes.apellido = self.line_Cliente_Apellido.text()
            clientes.cedula = self.line_Cliente_Apellido_2.text()
            clientes.email = self.line_Cliente_Apellido_4.text()
            clientes.telefono = self.line_Cliente_Apellido_3.text()
            clientes.id_tienda = self.line_Cliente_Direccion.text()
            clientes.estado = self.line_Cliente_Direccion.text()



            if self.line_Cliente_Nombre.text() == "" and not self.line_Cliente_Apellido_5.text() == "" and not self.line_Cliente_Apellido.text() == "" and not self.line_Cliente_Apellido_2.text() == "" and not self.line_Cliente_Apellido_4.text() == "" and not self.line_Cliente_Apellido_3.text() == "" and not self.line_Cliente_Direccion.text() == "" and not self.line_Cliente_Direccion.text() == "":
                indicador = dt_cliente.Dt_Clientes.guardarClientes(clientes)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Guardados")

                self.limpiarCampos()

                self.llenarTablaUsuario(dt_cliente.Dt_Clientes.listarCliente())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en GuardarCliente: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = cliente_Window()
    mw.show()
    app.exec()