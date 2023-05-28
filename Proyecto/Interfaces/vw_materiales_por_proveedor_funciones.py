import sys

import pymysql
from PyQt5.QtWidgets import QMainWindow
from Interfaces import vw_materiales_por_proveedor
from Entidades import materiales_por_proveedor
from Datos import dt_materiales_por_proveedor, dt_proveedor
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
        self.llenarComboProveedor()
        self.cb_proveedor.activated.connect(self.handleActivated)   


    # def llenarComboMaterial(self):
    #     self.cb_material.clear()
    #     try:
    #
    #     except pymysql.Error as e:
    #         print(f"No se puedieron recuperar los datos para el combobox de materiales en el archivo"
    #               f"de funciones de materiales_por_proveedor")
    #
    #     try:
    #         for m in materiales_por_proveedor:
    #             self.cb_material.addItem()
    #     except Exception as e:
    #         print(f"Ha ocurrido un error al rellenar el combobox de materiales en "
    #               f"el archivo de funciones de materiales_por_proveedor : {e}")


    def llenarComboProveedor(self):
        self.cb_proveedor.clear()

        proveedores = dt_proveedor.Dt_Proveedor.listarProveedor()
        print(f"No se puedieron recuperar los datos para el combobox de materiales en el archivo"
            f"de funciones de materiales_por_proveedor")

        try:
            for p in proveedores:
                self.cb_proveedor.addItem(p.index(), p.id_proveedor)
        except Exception as e:
            print(f"Ha ocurrido un error al rellenar el combobox de materiales en "
            f"el archivo de funciones de materiales_por_proveedor : {e}")

    def handleActivated(self, index):
        print(self.cb_proveedor.itemText(index))
        print(self.cb_proveedor.itemData(index))
    def listarMaterialesPorProveedor(self):
        print()
        # materiales_por_proveedor = dt_materiales_por_proveedor.DtMaterialesPorProveedor.listar_materiales_por_proveedor()
        # indexes = len(materiales_por_proveedor)
        # self.table_materiales_requeridos_por_pedido.setRowCount(indexes)
        # tablerow = 0
        # for row in materiales_por_proveedor:
        #     self.table_materiales_requeridos_por_pedido.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.id_materiales_por_proveedor)))
        #     self.table_materiales_requeridos_por_pedido.setItem((tablerow, 1, QtWidgets.QTableWidgetItem(str(row))))

    # def listarUsuarios(self):
    #     usuarios = DT_Usuario.listarUsuario()
    #     indexes = len(usuarios)
    #     self.tw_usuarios.setRowCount(indexes)
    #     tablerow = 0
    #     for row in usuarios:
    #         self.tw_usuarios.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.idusuario)))
    #         self.tw_usuarios.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row.nombre))
    #         self.tw_usuarios.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row.apellido))
    #         self.tw_usuarios.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row.nombreusuario))
    #         self.tw_usuarios.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.fecha_creacion)))
    #         tablerow += 1

    def guardarMaterialesPorProveedorDesdeTf(self, index):
        mpp = materiales_por_proveedor.MaterialesPorProveedor()
        mpp.id_material = self.cb_material.itemData(index)
        mpp.id_proveedor = self.cb_proveedor.itemData(index)

        if(mpp.id_material != None and mpp.id_proveedor != None):
            try:
                dt_materiales_por_proveedor.DtMaterialesPorProveedor.guardar_materiales_por_proveedor(mpp)
                print("Guardado con exito")

            except pymysql.Error as e:
                print(f"Error al llamar el metodo guardatMaterialesPorProveedorDesdeTf en el archivo de funciones,"
                f"Error: {e}")
        else:
            print("Puede que no se hayan guardado los datos")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = vw_materiales_por_proveedor.Ui_background()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())