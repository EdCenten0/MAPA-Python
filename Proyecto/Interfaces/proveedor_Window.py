#Francisco de Jesús Meléndez Simplina


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from Datos import dt_Proveedor
from Interfaces import vw_Proveedores


class proveedor_Window(QMainWindow, vw_Proveedores.Ui_Proveedores):

    def __init__(self, parent=None):
        super(proveedor_Window, self).__init__(parent)
        self.setupUi(self)
        self.llenarTablaProveedor(dt_Proveedor.Dt_Proveedor.listarProveedor())
        self.tb_Proveedor.itemSelectionChanged.connect(self.obtenerDatosTablaProveedor)


    def obtenerDatosTablaProveedor(self):
        # Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Proveedor.currentRow()

        id = self.tb_Proveedor.item(filaSeleccionada, 0).text()
        nombre = self.tb_Proveedor.item(filaSeleccionada, 1).text()
        email = self.tb_Proveedor.item(filaSeleccionada, 2).text()
        telefono = self.tb_Proveedor.item(filaSeleccionada, 3).text()
        catalogo = self.tb_Proveedor.item(filaSeleccionada, 4).text()
        ruc = self.tb_Proveedor.item(filaSeleccionada, 5).text()
        direccion = self.tb_Proveedor.item(filaSeleccionada, 6).text()

        self.line_Id.setText(id)
        self.line_Nombre.setText(nombre)
        self.line_Correo.setText(email)
        self.line_Telefono.setText(telefono)
        self.line_Catalogo.setText(catalogo)
        self.line_Ruc.setText(ruc)
        self.line_Direccion.setText(direccion)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = proveedor_Window()
    mw.show()
    app.exec()