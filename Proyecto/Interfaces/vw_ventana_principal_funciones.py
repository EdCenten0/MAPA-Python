import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from vw_ventana_principal import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces import vw_ventana_principal, vw_cliente_funciones
from Interfaces import vw_vista_previa_pedido_funciones

# Carlos Eduardo Chavarria Centeno (EdCenten0)
# Universidad Centroamericana

class VentanaPrincipal(QtWidgets.QMainWindow, vw_ventana_principal.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        self.setupUi(self)
        self.openedForms = []

        # EVENTOS EN BOTONES
        self.bt_vista_previa_pedidos.clicked.connect(lambda: self.mostrar_formularios(vw_vista_previa_pedido_funciones.VwVistaPreviaPedidosFunciones()))
        self.bt_clientes.clicked.connect(lambda: self.mostrar_formularios(vw_cliente_funciones.Cliente_Window()))

    # Para este metodo es obligatorio pasar la clase del formulario, por
    # lo que se tiene que hacer referencia hasta llegar a la clase
    # por ejemplo archivo.clase o import la clase desde antes
    def mostrar_formularios(self, form):
        # Cerrar todas las ventanas abiertas
        for openedForm in self.openedForms:
            openedForm.close()
            self.ly_contenedor.removeWidget(openedForm)

        # Limpiar la lista de ventanas abiertas
        self.openedForms = []

        # Agregar la nueva ventana al layout
        self.ly_contenedor.addWidget(form)
        self.openedForms.append(form)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal_obj = VentanaPrincipal()
    ventana_principal_obj.show()
    app.exec_()
