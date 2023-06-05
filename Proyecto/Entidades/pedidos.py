# Francisco de Jesús Meléndez Simplina
# Entidades del Pedido

class Pedido:

    def __init__(self, id_pedido, id_cliente ,descripcion ,fecha_Pedido ,estado):
        self.id_pedido = id_pedido
        self.id_cliente= id_cliente
        self.descripcion = descripcion
        self.fecha_Pedido = fecha_Pedido
        self.estado = estado

    def __str__(self):
        return f'''
        id_pedido = {self.id_pedido}
        id_cliente = {self.id_cliente}
        descripcion = {self.descripcion}
        fecha_Pedido = {self.fecha_Pedido}
        estado = {self.estado}
        '''

    @property
    def id_pedido(self):
        return self.id_pedido

    @id_pedido.setter
    def id_pedido(self, id_pedido):
        self.id_pedido = id_pedido

    @property
    def id_cliente(self):
        return self.id_cliente

    @id_cliente.setter
    def nombre(self, id_cliente):
        self.id_cliente = id_cliente

    @property
    def descripcion(self):
        return self.descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.descripcion = descripcion

    @property
    def fecha_Pedido(self):
        return self.fecha_Pedido

    @fecha_Pedido.setter
    def fecha_Pedido(self, fecha_Pedido):
        self.fecha_Pedido = fecha_Pedido

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado

