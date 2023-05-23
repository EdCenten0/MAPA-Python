import copy


class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, cedula=None, correo=None, telefono=None, id_tienda=None, estado=None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono
        self._cedula = cedula
        self._id_tienda = id_tienda
        self._estado = estado


    def __str__(self):
        return f'''
        id: {self._id}
        nombre: {self._nombre},
        apellido: {self._apellido},
        cedula: {self._cedula},  
        correo: {self._correo},
        telefono: {self._telefono},
        id_tienda: {self._id_tienda}
        estado: {self._estado}

        '''

    def __getitem__(self, item):
        u = copy.copy(self) #realiza una copia exacta del objeto
        u.id = u._id
        u.nombre = u._nombre
        u.cedula = u._cedula
        u.apellido = u._apellido
        u.correo = u._correo
        u.telefono = u._telefono
        u.id_tienda = u._id_tienda
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
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono


    @property
    def id_tienda(self):
        return self._id_tienda

    @id_tienda.setter
    def id_tienda(self, id_tienda):
        self._id_tienda = id_tienda

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado

