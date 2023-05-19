
# Francisco de Jesús Melendez Simplina
# Entidad de Rol_opcion


class Rol_opcion:
    def __init__(self,rol_opcion_id, id_opcion, id_rol):
        self.rol_opcion_id = rol_opcion_id
        self.id_opcion = id_opcion
        self.id_rol = id_rol

    def __str__(self):
        return f'''
        rol_opcion_id: {self.rol_opcion_id}
        id_opcion: {self.id_opcion}
        id_rol: {self.id_rol}
        '''

    @property
    def rol_opcion_id(self):
        return self.rol_opcion_id

    @rol_opcion_id.setter
    def rol_opcion_id(self, rol_opcion_id):
        self.rol_opcion_id = rol_opcion_id

    @property
    def id_opcion(self):
        return self.id_opcion

    @id_opcion.setter
    def id_opcion(self, id_opcion):
        self.id_opcion = id_opcion

    @property
    def id_rol(self):
        return self.id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self.id_rol = id_rol


