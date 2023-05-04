# Francisco de Jesús Meléndez Simplina
# Entidades del Pedido

class Pedido:

    def __init__(self, idPedido, nombre ,descripcion ,fecha_Pedido ,estado):
        self.idPedido = idPedido
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_Pedido = fecha_Pedido
        self.estado = estado

    def __str__(self):
        return f'''
        idPedido = {self.idPedido}
        nombre = {self.nombre}
        descripcion = {self.descripcion}
        fecha_Pedido = {self.fecha_Pedido}
        estado = {self.estado}
        '''

    @property
    def idPedido(self):
        return self.idPedido

    @idPedido.setter
    def idPedido(self, idPedido):
        self.idPedido = idPedido

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

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

