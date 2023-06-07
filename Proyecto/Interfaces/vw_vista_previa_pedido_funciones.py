import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from Datos import dt_Pedidos, dt_materiales
from Datos.dt_Pedidos import Dt_Pedidos
from Datos.dt_cliente import Dt_Clientes
from Entidades import materiales
from Interfaces import vw_vista_previa_pedido, vw_materiales_funciones, vw_materiales_por_pedido_funciones


class VwVistaPreviaPedidosFunciones(QtWidgets.QMainWindow, vw_vista_previa_pedido.Ui_MainWindow):

    def __init__(self, parent=None):
        super(VwVistaPreviaPedidosFunciones, self).__init__(parent)
        self.setupUi(self)

        self.openedForms = []
        self.id_pedido = self.comboBox_2.currentData()
        self.comboBox_2.currentIndexChanged.connect(self.setPedidoSeleccionado)


        print(f"self.id_pedido: {self.id_pedido}")
        self.llenarComboSeleccion(Dt_Pedidos.listarPedidos())
        self.comboBox_2.currentIndexChanged.connect(lambda: self.obtenerRegistroSeleccionadoComboBox())
        self.comboBox_2.currentIndexChanged.connect(self.setMaterialesAgregados)
        print(f"self.id_pedido: {self.id_pedido}")
        self.pushButton_2.clicked.connect(lambda: self.setMaterialesPorPedido(vw_materiales_por_pedido_funciones.vw_materiales_por_pedido_funciones()))
        print(f"materialesPorPedidido: id_pedido: {vw_materiales_por_pedido_funciones.vw_materiales_por_pedido_funciones.id}")





    def setPedidoSeleccionado(self):
        self.id_pedido = self.comboBox_2.currentData()
        vw_materiales_por_pedido_funciones.vw_materiales_por_pedido_funciones.id = self.id_pedido

    def llenarComboSeleccion(self, datos):
        self.comboBox_2.clear()
        for registro in datos:
            self.comboBox_2.addItem(registro["descripcion"], registro["id_pedido"])

        self.obtenerRegistroSeleccionadoComboBox()
        self.setMaterialesAgregados()

    def obtenerRegistroSeleccionadoComboBox(cls):
        index = cls.comboBox_2.currentData()
        datos_lista_pedido = Dt_Pedidos.listarSoloUnPedido(index)
        datos_pedido = datos_lista_pedido[0]
        descripcion = datos_pedido['descripcion']
        fecha_pedido = datos_pedido['fecha_pedido']
        id_cliente = datos_pedido['id_cliente']
        datos_lista_cliente = Dt_Clientes.listarSoloUnCliente(id_cliente)
        datos_cliente = datos_lista_cliente[0]
        nombre_apellido_cliente = datos_cliente['nombre'] + " " + datos_cliente['apellido']
        date = fecha_pedido

        cls.lineEdit.setText(nombre_apellido_cliente)
        cls.textEdit.setText(descripcion)
        cls.calendarWidget.setSelectedDate(date)

    def setMaterialesAgregados(self):
        id_pedido = self.comboBox_2.currentData()
        nMateriales = dt_materiales.Dt_materiales.contarMaterialesPorPedido(id_pedido)
        self.label.setText(f"{str(nMateriales)} materiales agregados...")



    def setMaterialesPorPedido(self, form):
        while self.ly_contenedor.count() > 0:
            item = self.ly_contenedor.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for openedForm in self.openedForms:
            openedForm.close()

        self.openedForms = []
        self.ly_contenedor.addWidget(form)
        self.openedForms.append(form)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = VwVistaPreviaPedidosFunciones()
    mw.show()
    app.exec()
