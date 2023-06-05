import sys

import pymysql
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Datos.dt_materiales import Dt_materiales
from Entidades.materiales_por_proveedor import MaterialesPorProveedor
from Interfaces import vw_materiales_por_proveedor
from Entidades import materiales_por_proveedor
from Datos import dt_materiales_por_proveedor, dt_proveedor, dt_materiales
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView

from Interfaces.vw_materiales_por_proveedor import Ui_background


# Carlos Eduardo Chavarria Centeno (EdCenten0)
# Universidad Centroamericana

class VwMaterialesPorProveedorFunciones(QtWidgets.QMainWindow, vw_materiales_por_proveedor.Ui_background):
    def __init__(self, parent=None):
        super(VwMaterialesPorProveedorFunciones, self).__init__(parent)
        self.setupUi(self)
        self.listarMaterialesPorProveedor()
        self.llenarComboProveedor()
        self.llenarComboMaterial()
        self.table_materiales_por_proveedor.itemSelectionChanged.connect(self.obtenerDatosTablas)

        # Botones

        self.bt_guardar.clicked.connect(self.guardarMaterialesPorProveedor)

    def llenarComboMaterial(self):
        self.cb_material.clear()

        materiales = dt_materiales.Dt_materiales.listarMateriales()

        try:
            for m in materiales:
                self.cb_material.addItem(m['nombre_material'], m['id_material'])
        except Exception as e:
            print(e)

        n = self.cb_proveedor.currentData()
        print(n)

    def llenarComboProveedor(self):
        self.cb_proveedor.clear()

        proveedores = dt_proveedor.Dt_Proveedor.listarProveedor()
        print(proveedores)

        try:
            for p in proveedores:
                self.cb_proveedor.addItem(p["nombre"], p["id_proveedor"])
        except Exception as e:
            print(f"Ha ocurrido un error al rellenar el combobox de proveedores en "
                  f"el archivo de funciones de materiales_por_proveedor : {e}")

    def listarMaterialesPorProveedor(self):
        datos = dt_materiales_por_proveedor.DtMaterialesPorProveedor.listar_vista()
        i = len(datos)
        print(f"Tamano de los datos de la tabla: {i}")
        self.table_materiales_por_proveedor.setRowCount(i)
        tablerow = 0

        for row in datos:
            self.table_materiales_por_proveedor.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(
                str(row.id_materiales_por_proveedor)))
            self.table_materiales_por_proveedor.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.id_proveedor)))
            self.table_materiales_por_proveedor.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.id_material)))
            self.table_materiales_por_proveedor.setItem(tablerow, 3,
                                                        QtWidgets.QTableWidgetItem(str(row.nombre_material)))
            self.table_materiales_por_proveedor.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.descripcion)))
            self.table_materiales_por_proveedor.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.cantidad)))
            self.table_materiales_por_proveedor.setItem(tablerow, 6,
                                                        QtWidgets.QTableWidgetItem(str(row.unidad_de_medida)))
            self.table_materiales_por_proveedor.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row.nombre)))
            self.table_materiales_por_proveedor.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row.catalogo)))
            tablerow += 1

    def obtenerDatosTablas(self):
        filaSelecccionada = self.table_materiales_por_proveedor.currentRow()

        id_proveedor = self.table_materiales_por_proveedor.item(filaSelecccionada, 1).text()
        id_material = self.table_materiales_por_proveedor.item(filaSelecccionada, 2).text()
        print(f"El valor de id_proveedor es: {id_proveedor}"
              f" Y el de id_material es: {id_material}")

        proveedor = dt_proveedor.Dt_Proveedor.buscarIndexProveedor(int(id_proveedor))
        material = dt_materiales.Dt_materiales.buscarIndexMateriall(int(id_material))

        if proveedor is None:
            print(proveedor)
            print(f"Efectivamente, es None")
            self.listarMaterialesPorProveedor()
        else:
            self.cb_proveedor.setCurrentIndex(proveedor - 1)
            self.cb_material.setCurrentIndex(material - 1)

    def guardarMaterialesPorProveedor(self):
        try:
            id_material = self.cb_material.currentData()
            id_proveedor = self.cb_proveedor.currentData()
            mpp = MaterialesPorProveedor(None, id_proveedor, id_material)
            dt_materiales_por_proveedor.DtMaterialesPorProveedor.guardar_materiales_por_proveedor(id_proveedor, id_material)
            self.listarMaterialesPorProveedor()


        except pymysql.Error as e:
            print(f"ERROR EN BOTON DE GUARDAR MATERIALES POR PROVEEDOR: {e}")


    def vaciarCombo(self):
        self.cb_proveedor.setCurrentIndex(0)
        self.cb_material.setCurrentIndex(0)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = vw_materiales_por_proveedor.Ui_background()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
