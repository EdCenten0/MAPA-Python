import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from Interfaces.vw_materiales_funciones import vw_materiales_funciones
from vw_ventana_principal import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Interfaces import vw_ventana_principal, vw_cliente_funciones, vw_proveedor_funciones, \
    vw_materiales_por_proveedor_funciones, vw_taller_funciones, vw_factura_funciones, vw_materiales, \
    vw_seguridad_funciones, vw_ventas_funciones, vw_tienda_funcionales
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
        self.bt_materiales.clicked.connect(lambda: self.mostrar_formularios(vw_materiales_funciones()))
        self.bt_proveedores.clicked.connect(lambda: self.mostrar_formularios(vw_proveedor_funciones.proveedor_Window()))
        self.bt_facturas.clicked.connect(lambda: self.mostrar_formularios(vw_factura_funciones.Ui_MainWindow()))
        self.bt_materiales_por_proveedor.clicked.connect(lambda: self.mostrar_formularios(vw_materiales_por_proveedor_funciones.VwMaterialesPorProveedorFunciones()))
        self.bt_taller.clicked.connect(lambda: self.mostrar_formularios((vw_taller_funciones.vw_taller_funciones())))
        self.bt_ventas.clicked.connect(lambda: self.mostrar_formularios(vw_ventas_funciones.Vw_ventas_funciones()))
        self.bt_tienda.clicked.connect(lambda: self.mostrar_formularios(vw_tienda_funcionales.VentanaTienda()))
        self.bt_seguridad.clicked.connect(lambda: self.mostrar_formularios(vw_seguridad_funciones.seguridad_Window()))
    # Para este metodo es obliga    torio pasar la clase del formulario, por
    # lo que se tiene que hacer referencia hasta llegar a la clase
    # por ejemplo archivo.clase o import la clase desde antes
    def mostrar_formularios(self, form):
        # Cierra todas las ventanas abiertas
        for openedForm in self.openedForms:
            openedForm.close()
            self.ly_contenedor.removeWidget(openedForm)

        # Limpia la lista de ventanas abiertas
        self.openedForms = []

        # Agrega la nueva ventana al ly_contenedor
        self.ly_contenedor.addWidget(form)
        self.openedForms.append(form)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal_obj = VentanaPrincipal()
    ventana_principal_obj.show()
    app.exec_()
