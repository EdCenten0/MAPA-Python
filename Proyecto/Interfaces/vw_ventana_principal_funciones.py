import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from vw_ventana_principal import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces import vw_ventana_principal
from Interfaces import vw_vista_previa_pedido_funciones


class VentanaPrincipal(QtWidgets.QMainWindow, vw_ventana_principal.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        self.setupUi(self)
        self.showWindows = None
        self.lista_usuarios = None

        # Eventos en Botones
        self.bt_vista_previa_pedidos.clicked.connect(self.mostrar_formulario)

    def mostrar_formulario(self):
        self.lista_usuarios = vw_vista_previa_pedido_funciones.VwVistaPreviaPedidosFunciones()
        self.ly_contenedor.addWidget(self.lista_usuarios)
        self.showWindows = self.lista_usuarios


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal_obj = VentanaPrincipal()
    ventana_principal_obj.show()
    app.exec_()
