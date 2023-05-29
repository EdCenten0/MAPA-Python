import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from Datos import dt_Pedidos
from Datos.dt_Pedidos import Dt_Pedidos
from Interfaces import vw_vista_previa_pedido

# Carlos Eduardo Chavarria Centeno (EdCenten0)
# Universidad Centroamericana
class VwVistaPreviaPedidosFunciones(QtWidgets.QMainWindow, vw_vista_previa_pedido.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VwVistaPreviaPedidosFunciones, self).__init__(parent)
        self.setupUi(self)


        # Llenado de combobox
        self.llenarComboSeleccion(Dt_Pedidos.listarPedidos())

    def llenarComboSeleccion(self, datos):
        self.comboBox_2.clear()
        for registro in datos:
            self.comboBox_2.addItem(registro["descripcion"], registro["id_pedido"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = VwVistaPreviaPedidosFunciones()
    mw.show()
    app.exec()

