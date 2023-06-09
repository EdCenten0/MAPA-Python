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




        # Botones
        self.btnGuardar.clicked.connect(self.guardarMateriales)
        self.btnEditar.clicked.connect(self.editarMaterial)
        self.btnEliminar.clicked.connect(self.eliminarMaterial)
        self.btnVaciarCampos.clicked.connect(self.limpiarCampos)
        self.btnBuscar.clicked.connect(self.buscarMaterial)
        self.btnRefrescar.clicked.connect(self.refrescarTabla)

        # TextBox
        self.txtPrecioUnidadMedida.textEdited.connect(lambda: self.setPrecioTotal())
        self.txtCantidad.textEdited.connect(lambda: self.setPrecioTotal())

    def limpiarCampos(self):

        if not self.txtNombreMaterial.text() == "" or not self.txtDescripcion.text() == "" or not self.txtPrecioUnidadMedida.text() == "" or not self.txtCantidad.text() == "" or not self.txtPrecioTotal.text() == "":

            self.lblId.clear()
            self.txtNombreMaterial.clear()
            self.txtDescripcion.clear()
            self.txtPrecioUnidadMedida.clear()
            self.txtCantidad.clear()
            self.txtPrecioTotal.clear()


    def setPrecioTotal(self):
        if self.txtPrecioUnidadMedida.text() != "" and self.txtCantidad.text() != "":
            if  '-' not in self.txtPrecioUnidadMedida.text() and  '-' not in self.txtCantidad.text() :
                try:
                    precio_total = float(self.txtCantidad.text()) * float(self.txtPrecioUnidadMedida.text())
                    self.txtPrecioTotal.setText(str(precio_total))
                    print(precio_total)
                except Exception as e:
                    QMessageBox.about(self, f"Digítos inválidos", f"No puede ingresar letras a la cantidad ni al precio: {e}")
            else:
                QMessageBox.about(self, f"Digítos inválidos", f"No puede ingresar numeros menores a 0")
                self.txtPrecioTotal.setText("")




    def notMensaje(self, indicador, resultado):

        if indicador == True:
            QMessageBox.about(self, "Exito!", "existosamente " + resultado)
        else:
            QMessageBox.about(self, "Error", "Ha ocurrido un error")

    def buscarMaterial(self):
        try:
            #self.tw_materiales.setCurrentItem(None)

            nombre_material = str(self.txtBuscar.text())
            materiales = dt_materiales.Dt_materiales.buscarMateriaPorPedido(nombre_material, vw_materiales_por_pedido_funciones.id)
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



    def guardarMateriales(self):
        try:

            Materiales.nombre_material = self.txtNombreMaterial.text()
            Materiales.descripcion = self.txtDescripcion.text()
            Materiales.precio_por_unidad = self.txtPrecioUnidadMedida.text()
            Materiales.cantidad = self.txtCantidad.text()
            Materiales.unidad_de_medida = self.cbUnidadesMedida.currentText()
            mult = str(float(self.txtPrecioUnidadMedida.text()) * float(self.txtCantidad.text()))
            Materiales.precio_total = mult
            self.txtPrecioTotal.setText(mult)
            Materiales.id_pedido = vw_materiales_por_pedido_funciones.id

            if self.lblId.text() == "" and not self.txtNombreMaterial.text() == "" and not self.txtDescripcion.text() == "" and not self.txtPrecioUnidadMedida.text() == "" and not self.txtCantidad.text() == "" and not self.txtPrecioTotal == "":

                if float(self.txtPrecioUnidadMedida.text()) > 0 and float(self.txtCantidad.text()) > 0 and float(self.txtPrecioTotal.text()) > 0:
                    indicador = dt_materiales.Dt_materiales.guardarMaterial(Materiales)
                    self.notMensaje(indicador, "material guardado")
                    self.limpiarCampos()

                    self.llenarTablaMateriales(dt_materiales.Dt_materiales.listarMaterialesPorPedido(vw_materiales_por_pedido_funciones.id))
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
            print(f"Editar Materiales: {vw_materiales_por_pedido_funciones.id}")
            Materiales.id_pedido = vw_materiales_por_pedido_funciones.id

            if not self.lblId.text() == "" and not self.txtNombreMaterial.text() == "" and not self.txtDescripcion.text() == "" and not self.txtPrecioUnidadMedida.text() == "" and not self.txtCantidad.text() == "" and not self.txtPrecioTotal == "":
                if float(self.txtPrecioUnidadMedida.text()) > 0 and float(self.txtCantidad.text()) > 0 and float(self.txtPrecioTotal.text()) > 0:
                    indicador = dt_materiales.Dt_materiales.editarMaterial(Materiales)
                    self.notMensaje(indicador, "material editado")

                    self.limpiarCampos()

                    self.llenarTablaMateriales(dt_materiales.Dt_materiales.listarMaterialesPorPedido(vw_materiales_por_pedido_funciones.id))
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





