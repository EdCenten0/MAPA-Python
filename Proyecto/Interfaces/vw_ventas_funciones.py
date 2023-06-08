import sys

import vw_ventas
import Datos.dt_Ventas

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QTableWidget, QMessageBox, QTableWidgetItem
from Entidades import Ventas
from Datos import dt_Ventas

class Vw_ventas_funciones(PyQt5.QtWidgets.QMainWindow, vw_ventas.Ui_Ventas):
    def __init__(self, parent=None):
        super(Vw_ventas_funciones, self).__init__(parent)
        self.setupUi(self)
        self.limpiarCampos()
        self.llenarTablaVentas(dt_Ventas.Dt_Ventas.listarVentas())
        self.tb_Ventas.itemSelectionChanged.connect(self.obtenerDatosTablaVentas)

        self.bt_Guardar_Ventas.clicked.connect(self.guardarVenta)
        self.bt_Editar_Ventas.clicked.connect(self.editarVenta)
        self.bt_Eliminar_Ventas.clicked.connect(self.eliminarVenta)
        self.bt_Vaciar_Ventas.clicked.connect(self.limpiarCampos)

    def limpiarCampos(self):
        self.line_Ventas_Cantidad.setText("")
        self.line_Ventas_Descripcion.setText("")
        self.line_Ventas_Id.setText("")
        self.line_Ventas_Nfactura.setText("")
        self.Ventas_idTienda_line.setText("")

    def obtenerDatosTablaVentas(self):
        filaActual =  self.tb_Ventas.currentRow()

        id = self.tb_Ventas.item(filaActual, 0).text()
        idTienda = self.tb_Ventas.item(filaActual, 1).text()
        noFactura = self.tb_Ventas.item(filaActual, 2).text()
        descripcion = self.tb_Ventas.item(filaActual, 3).text()
        cantidad = self.tb_Ventas.item(filaActual, 4).text()

        self.line_Ventas_Id.setText(id)
        self.Ventas_idTienda_line.setText(idTienda)
        self.line_Ventas_Nfactura.setText(noFactura)
        self.line_Ventas_Descripcion.setText(descripcion)
        self.line_Ventas_Cantidad.setText(cantidad)

    def notifMensaje(self, indicador, resultado):

        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            PyQt5.QtWidgets.QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            PyQt5.QtWidgets.QMessageBox.about(self, "Error", "Ha Ocurrido un Error")

    def llenarTablaVentas(self, datos):
        print("\nDatos de la tabla Ventas")
        i = len(datos)
        self.tb_Ventas.setRowCount(i)

        tbRow = 0
        for row in datos:
            print(row)

            self.tb_Ventas.setItem(tbRow, 0, PyQt5.QtWidgets.QTableWidgetItem(str(row["id_venta"])))
            self.tb_Ventas.setItem(tbRow, 1, PyQt5.QtWidgets.QTableWidgetItem(str(row["id_tienda"])))
            self.tb_Ventas.setItem(tbRow, 2, PyQt5.QtWidgets.QTableWidgetItem(str(row["id_factura"])))
            self.tb_Ventas.setItem(tbRow, 3, PyQt5.QtWidgets.QTableWidgetItem(row["descripcion"]))
            self.tb_Ventas.setItem(tbRow, 4, PyQt5.QtWidgets.QTableWidgetItem(str(row["cantidad"])))
            tbRow += 1

    def guardarVenta(self):
        if self.line_Ventas_Id.text() == "" and not self.Ventas_idTienda_line == "" and not self.line_Ventas_Cantidad == "" and not self.line_Ventas_Nfactura == "" and not self.line_Ventas_Descripcion == "":
            if self.line_Ventas_Id != "":
                try:
                    venta = None
                    id_venta = self.line_Ventas_Id.text()
                    id_tienda = self.Ventas_idTienda_line.text()
                    cantidad = self.line_Ventas_Cantidad.text()
                    descripcion = self.line_Ventas_Descripcion.text()
                    id_factura = self.line_Ventas_Nfactura.text()
                    venta = Ventas.ventas(None, id_tienda, id_factura, cantidad, descripcion)

                    Datos.dt_Ventas.Dt_Ventas.guardarVenta(venta)

                    PyQt5.QtWidgets.QMessageBox.about(self, "Se ha guardado la venta", "La venta ha sido guardada correctamente")

                    self.limpiarCampos()
                    self.llenarTablaVentas(Datos.dt_Ventas.Dt_Ventas.listarVentas())



                except Exception as ex:
                    print(f"Error al guardar venta: {ex}")

            else: PyQt5.QtWidgets.QMessageBox.about(self, "Error", "El id ya existe")

        else: PyQt5.QtWidgets.QMessageBox.about(self, "Error", "Todos los campos deben ser llenados")

    def editarVenta(self):
        if not self.line_Ventas_Id.text() == "" and not self.line_Ventas_Nfactura.text() == "" and not self.line_Ventas_Descripcion.text() == "" and not self.line_Ventas_Cantidad.text() == "" and not self.Ventas_idTienda_line.text() == "":
            if not self.line_Ventas_Id.text() == "":
                try:

                    id_venta = self.line_Ventas_Id.text()
                    id_tienda = self.Ventas_idTienda_line.text()
                    cantidad = self.line_Ventas_Cantidad.text()
                    descripcion = self.line_Ventas_Descripcion.text()
                    id_factura = self.line_Ventas_Nfactura.text()
                    venta = Ventas.ventas(id_venta, id_tienda, id_factura, cantidad, descripcion)

                    indicador = dt_Ventas.Dt_Ventas.editarVenta(venta)

                    if indicador:
                        QMessageBox.about(self, "El registro de venta ha sido modificado con exito",
                                          "El registro ha sido editado")
                    else:
                        QMessageBox.about(self, "Error", "No se pudo editar el registro de venta")

                    self.limpiarCampos()
                    self.llenarTablaVentas(Datos.dt_Ventas.Dt_Ventas.listarVentas())

                except Exception as ex:
                    print(f"Error al editar venta: {ex}")

            else:
                QMessageBox.about(self, "Error", "Selecciona la venta que desea editar")

        else:
            QMessageBox.about(self, "Error", "Todos los campos deben ser llenados")

    def eliminarVenta(self):
        try:
            if not self.line_Ventas_Id.text() == "":
                Ventas.id_venta = self.line_Ventas_Id.text()
                Datos.dt_Ventas.Dt_Ventas.eliminarVenta(Ventas)

                QMessageBox.about(self, "Mensaje", "Venta elimninada con exito")

                self.llenarTablaVentas(Datos.dt_Ventas.Dt_Ventas.listarVentas())

            else: PyQt5.QtWidgets.QMessageBox.about(self, "Seleccione un registro a eliminar")
        except Exception as ex:
            print(f"Error al eliminar venta: {ex}")

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    mw = Vw_ventas_funciones()
    mw.show()
    app.exec()