import sys
#from encodings.punycode import selective_find

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QTableWidget, QMessageBox, QTableWidgetItem

from Datos import dt_materiales
from Datos.dt_Pedidos import Dt_Pedidos
from Entidades.materiales import Materiales
from Interfaces import vw_materiales_por_pedido
from Interfaces import vw_materiales_por_pedido

class vw_materiales_por_pedido_funciones(QtWidgets.QMainWindow, vw_materiales_por_pedido.Ui_mw_materiales):
    id = None

    def __init__(self, parent = None):
        super(vw_materiales_por_pedido_funciones, self).__init__(parent)
        self.setupUi(self)
        #Acciones de la tabla
        self.llenarTablaMateriales(dt_materiales.Dt_materiales.listarMaterialesPorPedido(vw_materiales_por_pedido_funciones.id))
        self.tw_materiales.itemSelectionChanged.connect(self.obtenerDatosTablaMateriales)

        #cb
        self.llenarComboBoxPedidos()
        # self.cbPedidos.activated.connect()

        # Botones
        self.btnGuardar.clicked.connect(self.guardarMateriales)
        self.btnEditar.clicked.connect(self.editarMaterial)
        self.btnEliminar.clicked.connect(self.eliminarMaterial)
        self.btnVaciarCampos.clicked.connect(self.limpiarCampos)
        self.btnBuscar.clicked.connect(self.buscarMaterial)
        self.btnRefrescar.clicked.connect(self.refrescarTabla)

    def llenarComboBoxPedidos(self):
        pedidos = Dt_Pedidos.listarPedidos()
        try:
            for p in pedidos:
                self.cbPedidos.addItem(p['descripcion'], p['id_pedido'])
                #self.cbPedidos.addItem()
                #self.cbPedidos.addItem()
        except Exception as e:
            print(f"Ocurrio una excepcion al recuperar los pedidos {e}")


    def limpiarCampos(self):

        if not self.txtNombreMaterial.text() == "" or not self.txtDescripcion.text() == "" or not self.txtPrecioUnidadMedida.text() == "" or not self.txtCantidad.text() == "" or not self.txtPrecioTotal.text() == "":

            self.lblId.clear()
            self.txtNombreMaterial.clear()
            self.txtDescripcion.clear()
            self.txtPrecioUnidadMedida.clear()
            self.txtCantidad.clear()
            self.txtPrecioTotal.clear()
            #self.cbPedidos.clearEditText("A")
            #self.cbUnidadesMedida.setItemText(self, 3, "pulg")
            #self.cbUnidadesMedida.setCurrentText(self, 0, "")

    def notMensaje(self, indicador, resultado):

        if indicador == True:
            QMessageBox.about(self, "Exito!", "existosamente " + resultado)
        else:
            QMessageBox.about(self, "Error", "Ha ocurrido un error")

    def buscarMaterial(self):
        try:
            #self.tw_materiales.setCurrentItem(None)

            nombre_material = str(self.txtBuscar.text())
            materiales = dt_materiales.Dt_materiales.buscarMaterial(nombre_material)
            indexes = len(materiales)
            self.tw_materiales.setRowCount(indexes)
            tableRow = 0

            for m in materiales:
                self.tw_materiales.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(m['id_material'])))
                self.tw_materiales.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(m['nombre_material']))
                self.tw_materiales.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(m['descripcion']))
                self.tw_materiales.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(m['precio_por_unidad'])))
                self.tw_materiales.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(m['cantidad'])))
                self.tw_materiales.setItem(tableRow, 5, QtWidgets.QTableWidgetItem(str(m['unidad_de_medida'])))
                self.tw_materiales.setItem(tableRow, 6, QtWidgets.QTableWidgetItem(str(m['precio_total'])))
                self.tw_materiales.setItem(tableRow, 7, QtWidgets.QTableWidgetItem(str(m['id_pedido'])))
                tableRow += 1

        except Exception as e:
            print(f"Excepcion en {e}")


    def llenarTablaMateriales(self, datos):
        vacio = ""
        print("Datos de la tabla Materiales")

        i = len(datos)
        self.tw_materiales.setRowCount(i)
        tableRow = 0

        for row in datos:
            self.tw_materiales.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(row['id_material'])))
            self.tw_materiales.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row['nombre_material']))
            self.tw_materiales.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row['descripcion']))
            self.tw_materiales.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(row['precio_por_unidad'])))
            self.tw_materiales.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row['cantidad'])))
            self.tw_materiales.setItem(tableRow, 5, QtWidgets.QTableWidgetItem(str(row['unidad_de_medida'])))
            self.tw_materiales.setItem(tableRow, 6, QtWidgets.QTableWidgetItem(str(row['precio_total'])))
            self.tw_materiales.setItem(tableRow, 7, QtWidgets.QTableWidgetItem(str(row['id_pedido'])))
            tableRow += 1


    def refrescarTabla(self):

        datos = dt_materiales.Dt_materiales.listarMateriales()
        i = len(datos)

        self.tw_materiales.setRowCount(i)
        tableRow = 0

        for row in datos:
            self.tw_materiales.setItem(tableRow, 0, QTableWidgetItem(str(row['id_material'])))
            self.tw_materiales.setItem(tableRow, 1, QTableWidgetItem(row['nombre_material']))
            self.tw_materiales.setItem(tableRow, 2, QTableWidgetItem(row['descripcion']))
            self.tw_materiales.setItem(tableRow, 3, QTableWidgetItem(str(row['precio_por_unidad'])))
            self.tw_materiales.setItem(tableRow, 4, QTableWidgetItem(str(row['cantidad'])))
            self.tw_materiales.setItem(tableRow, 5, QTableWidgetItem(str(row['unidad_de_medida'])))
            self.tw_materiales.setItem(tableRow, 6, QTableWidgetItem(str(row['precio_total'])))
            self.tw_materiales.setItem(tableRow, 7, QTableWidgetItem(str(row['id_pedido'])))
            tableRow += 1



    def obtenerDatosTablaMateriales(self):

        filaSeleccionada = self.tw_materiales.currentRow()
        id_material = self.tw_materiales.item(filaSeleccionada, 0).text()
        material = self.tw_materiales.item(filaSeleccionada, 1).text()
        descripcion = self.tw_materiales.item(filaSeleccionada, 2).text()
        precio_por_unidad = self.tw_materiales.item(filaSeleccionada, 3).text()
        cantidad = self.tw_materiales.item(filaSeleccionada, 4).text()
        unidad_de_medida = self.tw_materiales.item(filaSeleccionada, 5).text()
        precio_total = self.tw_materiales.item(filaSeleccionada, 6).text()
        id_pedido = self.tw_materiales.item(filaSeleccionada, 7).text()

        self.lblId.setText(id_material)
        self.txtNombreMaterial.setText(material)
        self.txtDescripcion.setText(descripcion)
        self.txtPrecioUnidadMedida.setText(precio_por_unidad)
        self.txtCantidad.setText(cantidad)
        self.cbUnidadesMedida.setCurrentText(unidad_de_medida)
        self.txtPrecioTotal.setText(precio_total)
        self.cbPedidos.setCurrentIndex(int(id_pedido)-1)


    def guardarMateriales(self):
        try:

            #self.cbPedidos.addItem("Prueba")
            Materiales.nombre_material = self.txtNombreMaterial.text()
            Materiales.descripcion = self.txtDescripcion.text()
            Materiales.precio_por_unidad = self.txtPrecioUnidadMedida.text()
            Materiales.cantidad = self.txtCantidad.text()
            Materiales.unidad_de_medida = self.cbUnidadesMedida.currentText()
            #print(self.cbUnidadesMedida.currentText())
            mult = str(float(self.txtPrecioUnidadMedida.text()) * float(self.txtCantidad.text()))
            Materiales.precio_total = mult
            self.txtPrecioTotal.setText(mult)

            Materiales.id_pedido = self.cbPedidos.currentData()

            if self.lblId.text() == "" and not self.txtNombreMaterial.text() == "" and not self.txtDescripcion.text() == "" and not self.txtPrecioUnidadMedida.text() == "" and not self.txtCantidad.text() == "" and not self.txtPrecioTotal == "":

                if float(self.txtPrecioUnidadMedida.text()) > 0 and float(self.txtCantidad.text()) > 0 and float(self.txtPrecioTotal.text()) > 0:
                    indicador = dt_materiales.Dt_materiales.guardarMaterial(Materiales)
                    self.notMensaje(indicador, "material guardado")
                    self.limpiarCampos()

                    self.llenarTablaMateriales(dt_materiales.Dt_materiales.listarMateriales())
                else:
                    QMessageBox.about(self, "Error", "No se puede introducir numeros negativos")

            else:
                self.notMensaje(False, "")


        except Exception as e:
            print(f"Ha ocurrido una excepcion en {e}")

    def editarMaterial(self):

        try:

            Materiales.id_material = self.lblId.text()
            Materiales.nombre_material = self.txtNombreMaterial.text()
            Materiales.descripcion = self.txtDescripcion.text()
            Materiales.precio_por_unidad = self.txtPrecioUnidadMedida.text()
            Materiales.cantidad = self.txtCantidad.text()
            Materiales.unidad_de_medida = self.cbUnidadesMedida.currentText()
            mult = str(float(self.txtPrecioUnidadMedida.text()) * float(self.txtCantidad.text()))
            Materiales.precio_total = mult
            self.txtPrecioTotal.setText(mult)
            Materiales.id_pedido = self.cbPedidos.currentData()

            if not self.lblId.text() == "" and not self.txtNombreMaterial.text() == "" and not self.txtDescripcion.text() == "" and not self.txtPrecioUnidadMedida.text() == "" and not self.txtCantidad.text() == "" and not self.txtPrecioTotal == "":
                if float(self.txtPrecioUnidadMedida.text()) > 0 and float(self.txtCantidad.text()) > 0 and float(self.txtPrecioTotal.text()) > 0:
                    indicador = dt_materiales.Dt_materiales.editarMaterial(Materiales)
                    self.notMensaje(indicador, "material editado")

                    self.limpiarCampos()

                    self.llenarTablaMateriales(dt_materiales.Dt_materiales.listarMateriales())
                else:
                    QMessageBox.about(self, "Error", "No se puede introducir numeros negativos")
            else:

                self.notMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Ha ocurrido un error al editar el taller {e}")

    def eliminarMaterial(self):
        try:

            Materiales.id_material = self.lblId.text()

            if not self.lblId.text() == "" and not self.txtNombreMaterial.text() == "" and not self.txtDescripcion.text() == "" and not self.txtPrecioUnidadMedida.text() == "" and not self.txtCantidad.text() == "" and not self.txtPrecioTotal == "":

                indicador = dt_materiales.Dt_materiales.eliminarMaterial(Materiales)
                self.notMensaje(indicador, "material eliminado")
                self.limpiarCampos()
                self.llenarTablaMateriales(dt_materiales.Dt_materiales.listarMateriales())

            else:
                self.notMensaje(False, "")

        except Exception as e:
            print(f"Ocurrio un error al eliminar el material {e}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = vw_materiales_por_pedido_funciones()
    mw.show()
    app.exec()





