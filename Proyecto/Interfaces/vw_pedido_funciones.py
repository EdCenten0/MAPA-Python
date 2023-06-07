# Francisco de Jesus Melendez Simplina

import sys
from datetime import datetime

import PyQt5
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from pymysql import Date

from Datos import dt_cliente, dt_Pedidos
from Entidades import pedidos
from Entidades.pedidos import Pedido
from Interfaces import vw_pedido


class pedido_Window(QMainWindow, vw_pedido.Ui_Pedidos):

    def __init__(self, parent=None):
        super(pedido_Window, self).__init__(parent)
        self.setupUi(self)
        self.llenarTablaPedidos(dt_Pedidos.Dt_Pedidos.listarPedidos())
        self.llenarComboCliente()

        self.tb_Pedidos.itemSelectionChanged.connect(self.obtenerDatosTablaPedidos)
        self.bt_Guardar.clicked.connect(self.guardarPedido)
        self.bt_Editar.clicked.connect(self.editarPedido)
        self.bt_Eliminar.clicked.connect(self.eliminarPedido)
        self.bt_Vaciar.clicked.connect(self.limpiarCampos)

    def llenarComboCliente(self):
        self.cb_cliente.clear()

        clientes = dt_cliente.Dt_Clientes.listarClientes()

        try:
            for i in clientes:
                self.cb_cliente.addItem(i['nombre'], i['id_cliente'])
        except Exception as ex:
            print(ex)

        j = self.cb_cliente.currentData()
        print(j)
        self.cb_cliente.setCurrentIndex(-1)

    def limpiarCampos(self):
        self.line_Id.setText("")
        self.line_Descripcion.setText("")
        self.cb_cliente.setCurrentIndex(-1)
        fecha = QDate.fromString(datetime.today().strftime('%Y-%m-%d'), "yyyy-MM-dd")
        self.dt_pedido.setDate(fecha)


    def obtenerDatosTablaPedidos(self):
        filaActual = self.tb_Pedidos.currentRow()

        id_pedido = self.tb_Pedidos.item(filaActual, 0).text()
        descripcion = self.tb_Pedidos.item(filaActual, 1).text()
        fecha_pedidio = self.tb_Pedidos.item(filaActual, 2).text()
        id_cliente = self.tb_Pedidos.item(filaActual, 3).text()

        cliente = dt_cliente.Dt_Clientes.buscarIndexCliente(int(id_cliente))

        self.line_Id.setText(id_pedido)
        self.line_Descripcion.setText(descripcion)
        fecha = QDate.fromString(fecha_pedidio, "yyyy-MM-dd")
        self.dt_pedido.setDate(fecha)

        if cliente is None:
            print(cliente)
            print(f"Efectivamente, es None")
            self.listarMaterialesPorProveedor()
        else:
            self.cb_cliente.setCurrentIndex(cliente - 1)

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
            self.tb_Pedidos.setItem(tbRow, 1, QTableWidgetItem(str(row["descripcion"])))
            self.tb_Pedidos.setItem(tbRow, 2, QTableWidgetItem(str(row["fecha_pedido"])))
            self.tb_Pedidos.setItem(tbRow, 3, QTableWidgetItem(str(row["id_cliente"])))
            tbRow += 1

    def guardarPedido(self, index):

        if (
                self.line_Id.text() == "" and self.line_Descripcion.toPlainText() !="" and self.cb_cliente.currentData() !=  None and self.dt_pedido.text() != ""):
            try:
                pedido = None
                id_cliente = self.cb_cliente.currentData()
                descripcion = self.line_Descripcion.toPlainText()
                fecha_Pedido = self.dt_pedido.text()
                pedido = Pedido(None, id_cliente, descripcion, fecha_Pedido)

                dt_Pedidos.Dt_Pedidos.guardarPedido(pedido)
                self.llenarTablaPedidos(dt_Pedidos.Dt_Pedidos.listarPedidos())


            except Exception as ex:
                print(f"Error al guardar pedido: {ex}")
                QMessageBox.about(self, f"Error al guardar su registro", f"Por favor, revise los datos propocionados, como lo son {id_cliente}, {descripcion} y {fecha_Pedido}")

        else:
            QMessageBox.about(self, "Error al guardar", "Todos los campos deben ser rellenados")

    def editarPedido(self, index):

        if (
                self.line_Id.text() != "" and self.line_Descripcion.toPlainText() != "" and self.cb_cliente.currentData() != None and  self.dt_pedido.text() != ""):

            try:
                Pedido.id_pedido = self.line_Id.text()
                Pedido.id_cliente = self.cb_cliente.currentData()
                Pedido.descripcion = self.line_Descripcion.toPlainText()
                Pedido.fecha_Pedido = self.dt_pedido.text()


                dt_Pedidos.Dt_Pedidos.editarPedido(Pedido)
                self.llenarTablaPedidos(dt_Pedidos.Dt_Pedidos.listarPedidos())
            except Exception as ex:
                print(f"Error al editar pedido: {ex}")
        else:
            QMessageBox.about(self, "Error al editar el registro", "Debe elegir un registro y todos los campos deben ser rellenados")

    def eliminarPedido(self):

        try:
            if not self.line_Id == "":
                Pedido.id_pedido = self.line_Id.text()

                dt_Pedidos.Dt_Pedidos.eliminarPedido(Pedido)

                QMessageBox.about(self, "Registro eliminado", "El pedido se ha eliminado con exito")
                self.limpiarCampos()
                self.llenarTablaPedidos(dt_Pedidos.Dt_Pedidos.eliminarPedido())
                self.llenarComboCliente()


            else:
                QMessageBox.about(self, "Error al eliminar" ,"Seleccione un registro de pedido para eliminar")
        except Exception as ex:
            print(f"Error al eliminar pedido: {ex}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = pedido_Window()
    mw.show()
    app.exec()
