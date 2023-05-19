import copy


class bodega:
    def __init__(self, id=None, nombre=None, descripcion=None, tienda=None):
        self._id = id
        self._nombre = nombre
        self._tienda = tienda
        self._descripcion = descripcion


    def __str__(self):
        return f'''
        id: {self._id}
        nombre: {self._nombre},
        tienda: {self._tienda},
        descripcion: {self._descripcion}

        '''

    def __getitem__(self, item):
        u = copy.copy(self) #realiza una copia exacta del objeto
        u.id = u._id
        u.nombre = u._nombre
        u.tienda = u._tienda
        u.descripcion = u._descripcion
        return u

    #GET
    @property
    def id(self):
        return self._id

    #SET
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def tienda(self):
        return self._tienda

    @tienda.setter
    def tienda(self, tienda):
        self._tienda = tienda

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion


