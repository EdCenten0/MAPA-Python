# Francisco de Jesús Melendez Simplina
#Entidad Rol

class Rol:
    def __init__(self, idRol, rol, estado):
        self.idRol = idRol
        self.rol = rol
        self.estado = estado

    def __str__(self):
        return f'''
        idRol: {self.idRol}
        rol: {self.rol}
        estado: {self.estado}
        '''

    @property
    def idRol(self):
        return self.idRol

    @idRol.setter
    def idRol(self, idRol):
        self.idRol = idRol

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


