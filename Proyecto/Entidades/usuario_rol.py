
# Francisco de Jesús Melendez Simplina
# Entidad de usuario_rol


class Usuario_rol:
    def __init__(self,usuario_rol_id, id_usuario, id_rol):
        self.usuario_rol_id = usuario_rol_id
        self.id_usuario = id_usuario
        self.id_rol = id_rol

    def __str__(self):
        return f'''
        usuario_rol_id: {self.usuario_rol_id}
        id_usuario: {self.id_usuario}
        id_rol: {self.id_rol}
        '''

    @property
    def usuario_rol_id(self):
        return self.usuario_rol_id

    @usuario_rol_id.setter
    def usuario_rol_id(self, usuario_rol_id):
        self.usuario_rol_id = usuario_rol_id

    @property
    def id_usuario(self):
        return self.id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    @property
    def id_rol(self):
        return self.id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self.id_rol = id_rol


