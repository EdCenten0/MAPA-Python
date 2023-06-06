#Francisco De Jesus Melendez Simplina

class Tienda:

    def __init__(self, id_tienda, nombre, direccion, telefono, email, estado):
        self.id_tienda = id_tienda
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.estado = estado

    def __str__(self):
        return f'''
        id_tienda = {self.id_tienda},
        nombre = {self.nombre},
        direccion = {self.direccion},
        telefono = {self.telefono},
        email = {self.email},
        estado = {self.estado}
        '''

    @property
    def id_tienda(self):
        return self.id_tienda

    # SET
    @id_tienda.setter
    def id_tienda(self, id_tienda):
        self.id_tienda = id_tienda



    @property
    def nombre(self):
        return self.nombre

    # SET
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre


    @property
    def direccion(self):
        return self.direccion

    # SET
    @direccion.setter
    def direccion(self, direccion):
        self.direccion = direccion


    @property
    def email(self):
        return self.email

    # SET
    @email.setter
    def email(self, email):
        self.email = email


    @property
    def telefono(self):
        return self.telefono

    # SET
    @telefono.setter
    def telefono(self, telefono):
        self.telefono = telefono


    @property
    def estado(self):
        return self.estado

    # SET
    @estado.setter
    def estado(self, estado):
        self.estado = estado

