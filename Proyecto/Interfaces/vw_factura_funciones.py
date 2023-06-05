import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from Proyecto.Datos import dt_facturas
from Proyecto.Entidades import facturas
from Proyecto.Interfaces import vw_Factura


class Ui_MainWindow(QMainWindow, vw_Factura.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

        #Tabla
        self.llenarTablaFactura(dt_facturas.Dt_facturas.listarFacturas())
        self.tableWidget.itemSelectionChanged.connect(self.obtenerDatosTablaFactura)

        #Botones
        self.pushButton.clicked.connect(self.guardarFactura)
        self.pushButton_3.clicked.connect(self.limpiarCampos)
        self.pushButton_2.clicked.connect(self.eliminarFactura)

    def limpiarCampos(self):
        self.lineEdit.setText("")
        self.textEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")


    def obtenerDatosTablaFactura(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tableWidget.currentRow()

        id_factura = self.tableWidget.item(filaSeleccionada, 0).text()
        precio_materiales = self.tableWidget.item(filaSeleccionada, 1).text()
        mano_de_obra = self.tableWidget.item(filaSeleccionada, 2).text()
        precio_total = self.tableWidget.item(filaSeleccionada, 3).text()
        fecha = self.tableWidget.item(filaSeleccionada, 4).text()
        id_pedido = self.tableWidget.item(filaSeleccionada, 5).text()

        # Tramsformar la fecha en formato "yyyy-MM-dd"
        fechaTransformada = QDate.fromString(fecha, "yyyy-MM-dd")

        self.lineEdit.setText(id_factura)
        self.textEdit.setText(id_pedido)
        self.dateEdit.setDate(fechaTransformada)
        self.lineEdit_3.setText(precio_materiales)
        self.lineEdit_2.setText(mano_de_obra)
        self.lineEdit_4.setText(precio_total)


    def notifMensaje(self, indicador, resultado):

        if indicador == True:  # Se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Exito!", "Los Datos Fueron " + resultado + " Correctamente")

        else:  # No se hizo correctamente la consulta a la base de datos
            QMessageBox.about(self, "Error", "Ha Ocurrido un Error")



    def llenarTablaFactura(self, datos):
        print("\nDatos de la Tabla Cliente")
        i = len(datos)
        self.tableWidget.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row["id_factura"])))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row["id_pedido"])))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(str(row["fecha"])))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(str(row["precio_materiales"])))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(str(row["mano_de_obra"])))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(str(row["precio_total"])))

            tablerow = tablerow + 1

    def guardarFactura(self):
        try:
            facturas.id_factura = self.lineEdit.toPlainText()
            facturas.id_pedido = self.textEdit.toPlainText()
            facturas.fecha = self.dateEdit.toPlainText()
            facturas.precio_materiales = self.lineEdit_3.toPlainText()
            facturas.mano_de_obra = self.lineEdit_2.toPlainText()
            facturas.precio_total = self.lineEdit_4.toPlainText()

            if self.lineEdit.toPlainText() == "" and not self.textEdit.toPlainText() == "" and not self.dateEdit.toPlainText() == "" and not self.lineEdit_3.toPlainText() == "" and not self.lineEdit_2.toPlainText() == "" and not self.lineEdit_4.toPlainText() == "":

                indicador = dt_facturas.Dt_facturas.guardarFactura(facturas)
                self.notifMensaje(indicador, "Guardados")
                self.limpiarCampos()
                self.llenarTablaFactura(dt_facturas.Dt_facturas.listarFacturas())


        except Exception as e:
            print(f"Error en guardarFactura: {e}")


    def eliminarFactura(self):

        try:
            facturas.id_factura = self.lineEdit.text()

            if not self.lineEdit.text() == "" :
                indicador = dt_facturas.Dt_facturas.eliminarFactura(facturas)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(indicador, "Eliminados")

                self.limpiarCampos()

                self.llenarTablaFactura(dt_facturas.Dt_facturas.listarFacturas())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(False, "")
                self.limpiarCampos()

        except Exception as e:
            print(f"Error en eliminarFactura: {e}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Ui_MainWindow()
    mw.show()
    app.exec()