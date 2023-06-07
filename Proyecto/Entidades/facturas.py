import copy


class Facturas:
    def __init__(self, id_factura=None, id_pedido=None, fecha=None, precio_materiales=None, mano_de_obra=None, precio_total=None, estado=None):
        self._id_factura = id_factura
        self._id_pedido = id_pedido
        self._fecha = fecha
        self._precio_materiales = precio_materiales
        self._mano_de_obra = mano_de_obra
        self._precio_total = precio_total
        self._estado = estado


    def __str__(self):
        return f'''
        id_factura: {self._id_factura}
        id_pedido: {self._id_pedido},
        fecha: {self._fecha},
        precio_materiales: {self._precio_materiales},  
        mano_de_obra: {self._mano_de_obra},
        precio_total: {self._precio_total},
        estado: {self._estado}

        '''

    def __getitem__(self, item):
        u = copy.copy(self) #realiza una copia exacta del objeto
        u.id_factura = u._id_factura
        u.id_pedido = u._id_pedido
        u.fecha = u._fecha
        u.precio_materiales = u._precio_materiales
        u.mano_de_obra = u._mano_de_obra
        u.precio_total = u._precio_total
        u.estado = u._estado
        return u

    #GET
    @property
    def id_factura(self):
        return self._id_factura

    #SET
    @id_factura.setter
    def id_factura(self, id_factura):
        self._id_factura = id_factura

    @property
    def id_pedido(self):
        return self._id_pedido

    @id_pedido.setter
    def id_pedido(self, id_pedido):
        self._id_pedido = id_pedido


    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def precio_materiales(self):
        return self._precio_materiales
    @precio_materiales.setter
    def precio_materiales(self, precio_materiales):
        self._precio_materiales = precio_materiales

    @property
    def mano_de_obra(self):
        return self._mano_de_obra

    @mano_de_obra.setter
    def mano_de_obra(self, mano_de_obra):
        self._mano_de_obra = mano_de_obra

    @property
    def precio_total(self):
        return self._precio_total
    @precio_total.setter
    def precio_total(self, precio_total):
        self._precio_total = precio_total

