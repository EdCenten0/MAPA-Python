import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from Datos import dt_cliente
from Entidades import clientes
from Interfaces import vw_Cliente
from Datos import dt_cliente
from Entidades.clientes import Cliente




class Cliente_Window(QMainWindow, vw_Cliente.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Cliente_Window, self).__init__(parent)
        self.setupUi(self)

        #Tabla
        self.llenarTablaCliente(dt_cliente.Dt_Clientes.listarClientes())
        self.tb_Cliente.itemSelectionChanged.connect(self.obtenerDatosTablaCliente)

        #Botones
        self.bt_Guardar_Cliente.clicked.connect(self.guardarCliente)
        self.bt_Vaciar_Cliente.clicked.connect(self.limpiarCampos)
        self.bt_Editar_Cliente.clicked.connect(self.editarCliente)
        self.bt_Eliminar_Cliente.clicked.connect(self.eliminarCliente)
        self.bt_Buscar.clicked.connect(self.buscarCliente)

    def limpiarCampos(self):
        self.line_Cliente_Apellido.setText("")
        self.line_Cliente_Nombre.setText("")
        self.line_Cliente_Direccion.setText("")
        self.line_Cliente_Apellido_2.setText("")
        self.line_Cliente_Apellido_3.setText("")
        self.line_Cliente_Apellido_4.setText("")
        self.line_Cliente_Apellido_5.setText("")

    def obtenerDatosTablaCliente(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Cliente.currentRow()

        id = self.tb_Cliente.item(filaSeleccionada, 0).text()
        nombre = self.tb_Cliente.item(filaSeleccionada, 1).text()
        apellido = self.tb_Cliente.item(filaSeleccionada, 2).text()
        cedula = self.tb_Cliente.item(filaSeleccionada, 3).text()
        telefono = self.tb_Cliente.item(filaSeleccionada, 4).text()
        email = self.tb_Cliente.item(filaSeleccionada, 5).text()
        id_tienda = self.tb_Cliente.item(filaSeleccionada, 6).text()


        self.line_Cliente_Nombre.setText(id)
        self.line_Cliente_Apellido_5.setText(nombre)
        self.line_Cliente_Apellido.setText(apellido)
        self.line_Cliente_Apellido_2.setText(cedula)
        self.line_Cliente_Apellido_3.setText(telefono)
        self.line_Cliente_Apellido_4.setText(email)
        self.line_Cliente_Direccion.setText(id_tienda)


    def notifMensaje(self, indicador, resultado):

        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Error", "Ha Ocurrido un Error")



    def llenarTablaCliente(self, datos):
        print("\nDatos de la Tabla Cliente")
        i = len(datos)
        self.tb_Cliente.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Cliente.setItem(tablerow, 0, QTableWidgetItem(str(row["id_cliente"])))
            self.tb_Cliente.setItem(tablerow, 1, QTableWidgetItem((row["nombre"])))
            self.tb_Cliente.setItem(tablerow, 2, QTableWidgetItem(str(row["apellido"])))
            self.tb_Cliente.setItem(tablerow, 3, QTableWidgetItem((row["cedula"])))
            self.tb_Cliente.setItem(tablerow, 4, QTableWidgetItem(str(row["email"])))
            self.tb_Cliente.setItem(tablerow, 5, QTableWidgetItem((row["telefono"])))
            self.tb_Cliente.setItem(tablerow, 6, QTableWidgetItem(str(row["id_tienda"])))
            tablerow = tablerow + 1

    def guardarCliente(self):
        try:
            clientes.nombre = self.line_Cliente_Apellido_5.text()
            clientes.apellido = self.line_Cliente_Apellido.text()
            clientes.cedula = self.line_Cliente_Apellido_2.text()
            clientes.email = self.line_Cliente_Apellido_3.text()
            clientes.telefono = self.line_Cliente_Apellido_4.text()

            if not self.line_Cliente_Apellido_5.text() == "" and not self.line_Cliente_Apellido.text() == "" and not self.line_Cliente_Apellido_2.text() == "" and not self.line_Cliente_Apellido_3.text() == "" and not self.line_Cliente_Apellido_4.text() == "" and not self.line_Cliente_Direccion.text() == "":

                indicador = dt_cliente.Dt_Clientes.guardarClientes(clientes)
                self.notifMensaje(indicador, "Guardados")
                self.limpiarCampos()
                self.llenarTablaCliente(dt_cliente.Dt_Clientes.listarClientes())


        except Exception as e:
            print(f"Error en guardarCliente: {e}")

    def editarCliente(self):
        try:
            clientes.id_cliente = self.line_Cliente_Nombre.text()
            clientes.nombre = self.line_Cliente_Apellido_5.text()
            clientes.apellido = self.line_Cliente_Apellido.text()
            clientes.cedula = self.line_Cliente_Apellido_2.text()
            clientes.email = self.line_Cliente_Apellido_3.text()
            clientes.telefono = self.line_Cliente_Apellido_4.text()
            clientes.id_tienda = self.line_Cliente_Direccion.text()

            if not self.line_Cliente_Nombre.text() == "" and not self.line_Cliente_Apellido_5.text() == "" and not self.line_Cliente_Apellido.text() == "" and not self.line_Cliente_Apellido_2.text() == "" and not self.line_Cliente_Apellido_3.text() == "" and not self.line_Cliente_Apellido_4.text() == "" and not self.line_Cliente_Direccion.text() == "":
                if len(self.line_Cliente_Apellido_5.text()) <= 50:
                    if len(self.line_Cliente_Apellido.text()) <= 50:
                        if len(self.line_Cliente_Apellido_2.text()) <= 15:
                            if len(self.line_Cliente_Apellido_4.text()) <= 12:
                                if len(self.line_Cliente_Apellido_3.text()) <= 50:
                                    if len(self.line_Cliente_Direccion.text()) <= 300:
                                        indicador = dt_cliente.Dt_Clientes.editarClientes(clientes)
                                        self.notifMensaje(indicador, "Editados")
                                        self.limpiarCampos()
                                        self.llenarTablaCliente(dt_cliente.Dt_Clientes.listarClientes())
                                    else:
                                        QMessageBox.about(self, "Error",
                                                          "La dirección debe tener menos de 300 caracteres")
                                else:
                                    QMessageBox.about(self, "Error",
                                                      "El correo electrónico debe tener menos de 50 caracteres")
                            else:
                                QMessageBox.about(self, "Error", "El teléfono debe tener menos de 12 caracteres")
                        else:
                            QMessageBox.about(self, "Error", "La cédula debe tener menos de 15 caracteres")
                    else:
                        QMessageBox.about(self, "Error", "El apellido debe tener menos de 50 caracteres")
                else:
                    QMessageBox.about(self, "Error", "El nombre debe tener menos de 50 caracteres")
            else:
                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en EditarCliente: {e}")

    def eliminarCliente(self):

        try:
            clientes.id_cliente = self.line_Cliente_Nombre.text()

            if not self.line_Cliente_Nombre.text() == "" :
                indicador = dt_cliente.Dt_Clientes.eliminarClientes(clientes)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaCliente(dt_cliente.Dt_Clientes.listarClientes())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en EliminarCliente: {e}")


    def buscarCliente(self):
        datos = dt_cliente.Dt_Clientes.busqueda(self.line_Cliente_Buscar.text())
        i = len(datos)
        self.tb_Cliente.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.tb_Cliente.setItem(tablerow, 0, QTableWidgetItem(str(row["id_cliente"])))
            self.tb_Cliente.setItem(tablerow, 1, QTableWidgetItem((row["nombre"])))
            self.tb_Cliente.setItem(tablerow, 2, QTableWidgetItem((row["apellido"])))
            self.tb_Cliente.setItem(tablerow, 3, QTableWidgetItem((row["cedula"])))
            self.tb_Cliente.setItem(tablerow, 4, QTableWidgetItem((row["email"])))
            self.tb_Cliente.setItem(tablerow, 5, QTableWidgetItem(str(row["telefono"])))
            self.tb_Cliente.setItem(tablerow, 6, QTableWidgetItem(str(row["id_tienda"])))
            tablerow = tablerow + 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Cliente_Window()
    mw.show()
    app.exec()