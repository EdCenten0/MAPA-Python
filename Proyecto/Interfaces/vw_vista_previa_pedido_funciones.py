import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from Datos import dt_Pedidos
from Datos.dt_Pedidos import Dt_Pedidos
from Datos.dt_cliente import Dt_Clientes
from Interfaces import vw_vista_previa_pedido

# Carlos Eduardo Chavarria Centeno (EdCenten0)
# Universidad Centroamericana
class VwVistaPreviaPedidosFunciones(QtWidgets.QMainWindow, vw_vista_previa_pedido.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VwVistaPreviaPedidosFunciones, self).__init__(parent)
        self.setupUi(self)


        # Llenado de combobox
        self.llenarComboSeleccion(Dt_Pedidos.listarPedidos())
        self.comboBox_2.currentIndexChanged.connect(lambda : self.obtenerRegistroSeleccionadoComboBox())

    def llenarComboSeleccion(self, datos):
        self.comboBox_2.clear()
        for registro in datos:
            self.comboBox_2.addItem(registro["descripcion"], registro["id_pedido"])

        #Hice uso de esta funcion aqui para que cuando se cargue la ventana se muestre la info seleccionada por defecto
        self.obtenerRegistroSeleccionadoComboBox()

    def obtenerRegistroSeleccionadoComboBox(cls):

        #Selecciono el valor que tiene el combobox, en este caso es el id_pedido
        index = cls.comboBox_2.currentData()

        #Teniendo el id_pedido lo uso para traer especificamente el registro que necesito
        datos_lista_pedido = Dt_Pedidos.listarSoloUnPedido(index)

        #Debido a que la funcion me devuelve una lista en lugar de un objeto, lo que hago
        #es seleccionar una fila de la lista (Tambien se podria construir el objeto desde la funcion de listarSoloUnPedido, es totalmente valido)
        datos_pedido = datos_lista_pedido[0]

        #Guardo los datos correspondientes a la lista del pedido en variables para usarlas despues
        descripcion = datos_pedido['descripcion']
        fecha_pedido = datos_pedido['fecha_pedido']
        id_cliente = datos_pedido['id_cliente']

        #Uso el id_cliente para usarlo como argumento para la funcion que trae un solo cliente, aplicando lo mismo antes dicho con pedido
        datos_lista_cliente = Dt_Clientes.listarSoloUnCliente(id_cliente)

        #Selecciono la fila de la lista (Como es solo una fila pues solo tiene el indice 0)
        datos_cliente = datos_lista_cliente[0]

        #Teniendo el cliente en cuestion obtengo su nombre y apellido para guardarlo en una variable
        nombre_apellido_cliente = datos_cliente['nombre'] + " " +datos_cliente['apellido']

        #Obtengo la fecha
        date = fecha_pedido

        #Finalmente ocupo las variables almacenadas para poner la informacion en su lugar del formulario
        cls.lineEdit.setText(nombre_apellido_cliente)
        cls.textEdit.setText(descripcion)
        cls.calendarWidget.setSelectedDate(date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = VwVistaPreviaPedidosFunciones()
    mw.show()
    app.exec()


