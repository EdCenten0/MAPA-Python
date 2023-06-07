import copy

class ventas:
    def __init__(self, id_venta=None, id_tienda=None,  id_factura=None, cantidad=None, descripcion=None):
        self._id_venta = id_venta
        self._id_tienda = id_tienda
        self._id_factura = id_factura
        self._cantidad = cantidad
        self._descripcion = descripcion


    def __str__(self):
        return f'''
        ID venta = {self._id_venta}
        ID tienda = {self._id_tienda}
        ID factura = {self._id_factura}
        Cantidad = {self._cantidad}
        Descripcion = {self._descripcion}
        '''

    def __getitem__(self, item):
        v = copy.copy(self)
        v.id_venta = v._id_venta
        v.id_tienda = v._id_tienda
        v.id_factura = v._id_factura
        v.cantidad = v._cantidad
        v.descripcion = v._descripcion


    @property
    def id_venta(self):
        return self._id_tienda

    @id_venta.setter
    def id_venta(self, id_venta):
        self._id_venta = id_venta

    @property
    def id_tienda(self):
        return self._id_tienda

    @id_tienda.setter
    def if_tienda(self, id_tienda):
        self._id_tienda = id_tienda

    @property
    def id_factura(self):
        return self._id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self._id_factura = id_factura

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

