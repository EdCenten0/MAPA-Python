# Francisco de Jesús Melendez Simplina
#Entidad de Usuario

class Usuarios:
    def __init__(self,id_usuario, nombre, apellido, user, password, fechaCreacion, estado):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.user = user
        self.password = password
        self.fechaCreacion = fechaCreacion
        self.estado = estado

    def __str__(self):
        return f'''
        id_usuario: {self.id_usuario}
        nombre: {self.nombre}
        apellido: {self.apellido}
        user: {self.user}
        password: {self.password}
        fechaCreacion: {self.fechaCreacion}
        estado: {self.estado}
        '''

    @property
    def id_usuario(self):
        return self.id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def apellido(self):
        return self.apellido

    @apellido.setter
    def apellido(self, apellido):
        self.apellido = apellido

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, user):
        self.user = user

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password = password

    @property
    def fechaCreacion(self):
        return self.fechaCreacion

    @fechaCreacion.setter
    def fechaCreacion(self, fechaCreacion):
        self.fechaCreacion = fechaCreacion

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado
