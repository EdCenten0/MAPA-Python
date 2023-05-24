import copy


class Taller:
    def __init__(self, id=None, nombre=None, direccion=None, telefono=None, email=None, id_tienda = None):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
        self._id_tienda = id_tienda

    def __str__(self):
        return f'''
        id: {self._id}
        nombre: {self._nombre},
        direccion: {self._direccion},
        telefono: {self._telefono},
        email: {self._email}
        id_tienda: {self._id_tienda}
        '''

    def __getitem__(self, item):
        u = copy.copy(self) #realiza una copia exacta del objeto
        u.id = u._id
        u.nombre = u._nombre
        u.direccion = u._direccion
        u.telefono = u._telefono
        u.email = u._email

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
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def id_tienda(self):
        return self._id_tienda

    @id_tienda.setter
    def id_tienda(self, id_tienda):
        self._id_tienda = id_tienda

if __name__ == '__main__':
    t = Taller(2, 'MAPA', 'managua', 45786532, 'hpalacios@gmail.com', 1)
    print(t)
