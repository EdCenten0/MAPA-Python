import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Datos import dt_Pedidos, dt_materiales, dt_facturas
from Entidades.facturas import Facturas
from vw_vista_previa_factura import Ui_MainWindow

class VistaPreviaFacturaFunciones(QtWidgets.QMainWindow, Ui_MainWindow):

    id_pedido = None
    descripcion_pedido = None
    precio_de_materiales = None
    precio_total = None
    fecha = None

    def __init__(self, parent=None):
        super(VistaPreviaFacturaFunciones, self).__init__(parent)
        self.setupUi(self)
        self.obtenerDatosDelPedido()
        self.lineEdit_3.textEdited.connect(lambda: self.setPrecioTotal())
        self.pushButton.clicked.connect(lambda: self.guardarFactura())

    def obtenerDatosDelPedido(self):
        pedido = dt_Pedidos.Dt_Pedidos.listarSoloUnPedido(VistaPreviaFacturaFunciones.id_pedido)
        precio_total = dt_materiales.Dt_materiales.sumarPrecioMateriales(pedido.id_pedido)
        self.label_4.setText(pedido.descripcion)
        self.label_5.setText(str(round(precio_total)))
        now = datetime.now()
        self.label_9.setText(str(f"{now.year}-{now.month}-{now.day}"))
        print(pedido)

    def setPrecioTotal(self):
        if self.label_5.text() != "" and self.lineEdit_3.text() != "":
            try:
                precio_total = float(self.label_5.text()) + float(self.lineEdit_3.text())
                self.label_7.setText(str(precio_total))
                print(precio_total)
            except Exception as e:
                QMessageBox.about(self, f"Digítos inválidos",
                                  f"No puede ingresar letras a la mano de obra: {e}")

    def guardarFactura(self):
        factura = Facturas()
        factura.id_pedido = VistaPreviaFacturaFunciones.id_pedido
        factura.fecha = self.label_9.text()
        factura.precio_materiales = self.label_5.text()
        factura.mano_de_obra = self.lineEdit_3.text()
        factura.precio_total = self.label_7.text()
        dt_facturas.Dt_facturas.guardarFacturas(factura)
        QMessageBox.about(self, "Factura", f"La Factura ha sido guardada correctamente")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal_obj = VistaPreviaFacturaFunciones()
    ventana_principal_obj.show()
    app.exec_()
