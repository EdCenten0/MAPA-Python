# Francisco de Jesús Meléndez Simplina
# Entidad del Proveedor

class Proveedor:

    def __init__(self, id_proveedor, id_tienda, nombre, ruc, correo, catalogo, telefono, direccion,estado):
        self.id_proveedor = id_proveedor
        self.id_tienda = id_tienda
        self.nombre = nombre
        self.ruc = ruc
        self.correo = correo
        self.catalogo = catalogo
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado

    def __str__(self):
        return f'''
        id_proveedor = {self.id_proveedor}
        id_tienda = {self.id_tienda}
        nombre = {self.nombre}
        ruc = {self.ruc}
        correo = {self.correo}
        catalogo = {self.catalogo}
        direccion = {self.direccion}
        estado = {self.estado}
        '''

    @property
    def id_proveedor(self):
        return self.id_proveedor

    @id_proveedor.setter
    def id_proveedor(self, id_proveedor):
        self.id_proveedor = id_proveedor

    @property
    def id_tienda(self):
        return self.id_tienda

    @id_tienda.setter
    def id_tienda(self, id_tienda):
        self.id_tienda = id_tienda

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
    def catalogo(self):
        return self.catalogo

    @catalogo.setter
    def catalogo(self, catalogo):
        self.catalogo = catalogo

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado