import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from Proyecto.Interfaces import  vw_vista_previa_pedido

class VwVistaPreviaPedidosFunciones(QtWidgets.QMainWindow, vw_vista_previa_pedido.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VwVistaPreviaPedidosFunciones, self).__init__(parent)
        self.setupUi(self)