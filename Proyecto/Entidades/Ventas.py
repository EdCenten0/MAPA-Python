import copy

class ventas:
    def __init__(self, id_venta=None, id_tienda=None,  id_factura=None, cantidad=None, descripcion=None, estado=None):
        self.id_venta = id_venta
        self.id_tienda = id_tienda
        self.id_factura = id_factura
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f'''
ID venta = {self.id_venta}
ID tienda = {self.id_tienda}
ID factura = {self.id_factura}
Cantidad = {self.cantidad}
Descripcion = {self.descripcion}
Estado = {self.estado}'''

    @property
    def id_venta(self):
        return self.id_tienda

    @id_venta.setter
    def id_venta(self, id_venta):
        self.id_venta = id_venta

    @property
    def id_tienda(self):
        return self.id_tienda

    @id_tienda.setter
    def if_tienda(self, id_tienda):
        self.id_tienda = id_tienda

    @property
    def id_factura(self):
        return self.id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self.id_factura = id_factura

    @property
    def cantidad(self):
        return self.cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.cantidad = cantidad

    @property
    def descripcion(self):
        return self.descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.descripcion = descripcion

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado
