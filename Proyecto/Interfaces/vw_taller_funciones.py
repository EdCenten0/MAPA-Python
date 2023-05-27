import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QTableWidgetItem

from Datos import dt_taller
from Datos.dt_taller import Dt_taller
from Entidades.taller import Taller
from Interfaces import vw_taller

class vw_taller_funciones(QtWidgets.QMainWindow, vw_taller.Ui_mw_taller):
    def __init__(self, parent=None):
        super(vw_taller_funciones, self).__init__(parent)
        self.setupUi(self)
        self.llenarTablaTaller(dt_taller.Dt_taller.listarTaller())


    def llenarTablaTaller(self, datos):

        vacio = ""
        print("\nDatos de la tabla Taller")

        i = len(datos)
        self.tw_taller.setRowCount(i)
        tableRow = 0

        for row in datos:
            self.tw_taller.setItem(tableRow, 0, QTableWidgetItem(row['nombre']))
            self.tw_taller.setItem(tableRow, 1, QTableWidgetItem(row['direccion']))
            self.tw_taller.setItem(tableRow, 2, QTableWidgetItem(row['telefono']))
            self.tw_taller.setItem(tableRow, 3, QTableWidgetItem(row['email']))
            tableRow += 1








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmTaller_funciones = QtWidgets.QMainWindow()
    ui = vw_taller_funciones()
    ui.setupUi(frmTaller_funciones)
    frmTaller_funciones.show()
    sys.exit(app.exec())