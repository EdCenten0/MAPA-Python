# Francisco de Jesús Meléndez Simplina
# Entidad del Proveedor

class Proveedor:

    def __init__(self, idProveedor, nombre, ruc, correo, catalogo, telefono, direccion,estado):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.ruc = ruc
        self.correo = correo
        self.catalogo = catalogo
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado

    def __str__(self):
        return f'''
        idProveedor = {self.idProveedor}
        nombre = {self.nombre}
        ruc = {self.ruc}
        correo = {self.correo}
        catalogo = {self.telefono}
        direccion = {self.direccion}
        estado = {self.estado}
        '''

    @property
    def idProveedor(self):
        return self.idProveedor

    @idProveedor.setter
    def idProveedor(self, idProveedor):
        self.idProveedor = idProveedor

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def ruc(self):
        return self.ruc

    @ruc.setter
    def ruc(self, ruc):
        self.ruc = ruc

    @property
    def correo(self):
        return self.correo

    @correo.setter
    def correo(self, correo):
        self.correo = correo

    @property
    def telefono(self):
        return self.telefono

    @telefono.setter
    def telefono(self, telefono):
        self.telefono = telefono

    @property
    def direccion(self):
        return self.direccion

    @direccion.setter
    def direccion(self, direccion):
        self.direccion = direccion

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado