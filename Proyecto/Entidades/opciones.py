# Francisco de Jesús Melendez Simplina
#Entidad Opcion


class Opcion:
    def __init__(self,idOpcion, opcion, estado):
        self.idOpcion = idOpcion
        self.opcion = opcion
        self.estado = estado

    def __str__(self):
        return f'''
        idOpcion: {self.idOpcion}
        opcion: {self.opcion}
        estado: {self.estado}
        '''

    @property
    def idOpcion(self):
        return self.idOpcion

    @idOpcion.setter
    def idOpcion(self, idOpcion):
        self.idOpcion = idOpcion

    @property
    def opcion(self):
        return self.opcion

    @opcion.setter
    def opcion(self, opcion):
        self.rol = opcion

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado


