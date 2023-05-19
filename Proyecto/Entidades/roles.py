# Francisco de Jesús Melendez Simplina
#Entidad de Rol

class Rol:
    def __init__(self, id_rol, rol, estado):
        self.id_rol = id_rol
        self.rol = rol
        self.estado = estado

    def __str__(self):
        return f'''
        id_rol: {self.id_rol}
        rol: {self.rol}
        estado: {self.estado}
        '''

    @property
    def id_rol(self):
        return self.id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self.id_rol = id_rol

    @property
    def rol(self):
        return self.rol

    @rol.setter
    def rol(self, rol):
        self.rol = rol

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado


