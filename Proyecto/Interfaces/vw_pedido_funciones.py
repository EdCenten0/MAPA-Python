# Francisco de Jesus Melendez Simplina

import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import Proyecto
from Proyecto.Datos import dt_cliente, dt_Pedidos
from Proyecto.Entidades import pedidos
from Proyecto.Entidades.pedidos import Pedido
from Proyecto.Interfaces import vw_pedido


class pedido_Window(QMainWindow, vw_pedido.Ui_Pedidos):

    def __init__(self, parent=None):
        super(pedido_Window, self).__init__(parent)
        self.setupUi(self)
        self.llenarTablaPedidos(dt_Pedidos.Dt_Pedidos.listarPedidos())

        self.llenarComboCliente()
        self.limpiarCampos()
        self.obtenerDatosTablaPedidos()

        self.bt_Guardar.clicked.connect(self.guardarPedido)
        self.bt_Editar.clicked.connect(self.editarPedido)
        self.bt_Eliminar.clicked.connect(self.editarPedido)
        self.bt_Vaciar.clicked.connect(self.limpiarCampos())

    def llenarComboCliente(self):
        self.cb_cliente.clear()

        clientes = dt_cliente.Dt_Clientes.listarClientes()

        try:
            for i in clientes:
                self.cb_cliente.addItem(i['nombre_cliente'], i['id_cliente'])
        except Exception as ex:
            print(ex)

        j = self.cb_cliente.currentData()
        print(j)

    def limpiarCampos(self):
        self.line_Id.setText("")
        self.line_Nombre.setText("")
        self.line_Descripcion.setText("")
        self.cb_cliente.setCurrentIndex(0)

    def obtenerDatosTablaPedidos(self):
        filaActual = self.tb_Pedidos.currentRow()

        id_cliente = self.tb_Pedidos.item(filaActual, 1).text()
        id = self.tb_Pedidos.setItem(filaActual, 0).text()
        nombre = self.tb_Pedidos.setItem(filaActual, 2).text()
        descripcion = self.tb_Pedidos.setItem(filaActual, 4).text()
        fecha = self.tb_Pedidos.setItem(filaActual, 3).text()
        cliente = dt_cliente.Dt_Clientes.buscarIndexCliente(int(id_cliente))

        self.line_Nombre.setText(nombre)
        self.line_Id.setText(id)
        self.line_Descripcion.setText(descripcion)
        self.cb_cliente.setCurrentIndex(cliente)

    def notifMensaje(self, indicador, resultado):
        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            PyQt5.QtWidgets.QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            PyQt5.QtWidgets.QMessageBox.about(self, "Error", "Ha Ocurrido un Error")

    def llenarTablaPedidos(self, datos):
        print("\nDatos de la tabla pedidos")
        i = len(datos)
        self.tb_Pedidos.setRowCount(i)

        tbRow = 0
        for row in datos:
            print(row)

            self.tb_Pedidos.setItem(tbRow, 0, QTableWidgetItem(str(row["id_pedido"])))
            self.tb_Pedidos.setItem(tbRow, 1, QTableWidgetItem(str(row["id_cliente"])))
            self.tb_Pedidos.setItem(tbRow, 2, QTableWidgetItem(row["nombre"]))
            self.tb_Pedidos.setItem(tbRow, 3, QTableWidgetItem(str(row["fecha"])))
            self.tb_Pedidos.setItem(tbRow, 4, QTableWidgetItem(row["descripcion"]))
            tbRow += 1

    def guardarPedido(self, index):

        if (
                not self.line_Id == "" and not self.line_Nombre == "" and not self.line_Descripcion == 0 and not self.cb_cliente == "" and not self.dt_pedido == ""):
            try:
                Pedido.id_pedido = self.line_Id.text()
                Pedido.id_cliente = self.cb_cliente.itemData(index)
                Pedido.descripcion = self.line_Descripcion.text()
                Pedido.fecha_Pedido = self.dt_pedido.text()
                Pedido.nombre = self.line_Nombre.text()

                dt_Pedidos.Dt_Pedidos.guardarPedido(Pedido)


            except Exception as ex:
                print(f"Error al guardar pedido: {ex}")

        else:
            QMessageBox.about("Todos los campos deben ser rellenados")

    def editarPedido(self, index):

        if (
                not self.line_Id == "" and not self.line_Nombre == "" and not self.line_Descripcion == 0 and not self.cb_cliente == "" and not self.dt_pedido == ""):

            try:
                Pedido.id_pedido = self.line_Id.text()
                Pedido.id_cliente = self.cb_cliente.itemData(index)
                Pedido.descripcion = self.line_Descripcion.text()
                Pedido.fecha_Pedido = self.dt_pedido.text()
                Pedido.nombre = self.line_Nombre.text()

                dt_Pedidos.Dt_Pedidos.editarPedido(Pedido)

            except Exception as ex:
                print(f"Error al editar pedido: {ex}")
        else:
            QMessageBox.about("Todos los campos deben ser rellenados")

    def eliminarPedido(self):

        try:
            if not self.line_Id == "":
                Pedido.id_pedido = self.line_Id.text()

                dt_Pedidos.Dt_Pedidos.eliminarPedido(Pedido)

                QMessageBox.about("El pedido se ha eliminado con exito")
                self.limpiarCampos()
                self.llenarTablaPedidos()
                self.llenarComboCliente()


            else:
                QMessageBox.about("Seleccione un registro de pedido para eliminar")
        except Exception as ex:
            print(f"Error al eliminar pedido: {ex}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = pedido_Window()
    mw.show()
    app.exec()
