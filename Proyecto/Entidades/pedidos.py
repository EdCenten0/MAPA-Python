# Francisco de Jesús Meléndez Simplina
# Entidades del Pedido
import copy


class Pedido:
    def __init__(self, id_pedido=None, id_cliente=None, descripcion=None
                 , fecha_Pedido=None, estado=None):
        self._id_pedido = id_pedido
        self._id_cliente = id_cliente
        self._descripcion = descripcion
        self._fecha_Pedido = fecha_Pedido
        self._estado = estado

    def __str__(self):
        return f'''
        id_pedido = {self._id_pedido}
        id_cliente = {self._id_cliente}
        descripcion = {self._descripcion}
        fecha_Pedido = {self._fecha_Pedido}
        estado = {self._estado}
        '''
    def __getitem__(self, item):
        p = copy.copy(self)
        p.id_pedido = p._id_pedido
        p.id_cliente = p._id_cliente
        p.descripcion = p._descripcion
        p.fecha_Pedido = p._fecha_Pedido
        p.estado = p._estado

    @property
    def id_pedido(self):
        return self._id_pedido

    @id_pedido.setter
    def id_pedido(self, id_pedido):
        self._id_pedido = id_pedido

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def fecha_Pedido(self):
        return self._fecha_Pedido

    @fecha_Pedido.setter
    def fecha_Pedido(self, fecha_Pedido):
        self._fecha_Pedido = fecha_Pedido

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado
