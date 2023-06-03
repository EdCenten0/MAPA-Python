import copy

from pyparsing import unicode_set


class Materiales:
    def __init__(self, id_material=None, nombre_material=None, descripcion=None, cantidad=None, unidad_de_medida = None, precio_por_unidad=None, precio_total=None, id_pedido = None):
        self._id_material = id_material
        self._nombre_material = nombre_material
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._unidad_de_medida = unidad_de_medida
        self._precio_por_unidad = precio_por_unidad
        self._precio_total = precio_total
        self._id_pedido = id_pedido

    def __str__(self):
        return f'''
        id_material: {self._id_material},
        material: {self._nombre_material},
        descripcion: {self._descripcion},
        cantidad: {self._cantidad},
        unidad_de_medida: {self._unidad_de_medida}
        precio_por_unidad: {self._precio_por_unidad},
        precio_total: {self._precio_total},
        id_pedido: {self._id_pedido}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.id_material = u._id_material
        u.material = u._material
        u.descripcion = u._descripcion
        u.cantidad = u._cantidad
        u.unidad_de_medida = u._unidad_de_medida
        u.precio_por_unidad = u._precio_por_unidad
        u.precio_total  = u._precio_total

    @property
    def id_material(self):
        return self._id

    @id_material.setter
    def id(self, id):
        self._id = id

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    @property
    def descripcion(self):
        return self._descripcion


    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def unidad_de_medida(self):
        return self._unidad_de_medida

    @unidad_de_medida.setter
    def unidad_de_medidad(self, unidad_de_medida):
        self._unidad_de_medida = unidad_de_medida


    @property
    def precio_por_unidad(self):
        return self._precio_por_unidad

    @precio_por_unidad.setter
    def precio_por_unidad(self, precio_por_unidad):
        self._precio_por_unidad = precio_por_unidad

    @property
    def precio_total(self):
        return self._precio_unidad

    @precio_total.setter
    def precio_total(self, precio_total):
        self._precio_total = precio_total

    @property
    def id_pedido(self):
        return self._id_pedido

    @id_pedido.setter
    def id_pedido(self, id_pedido):
        self._id_pedido = id_pedido

if __name__ == '__main__':
    m1 = Materiales(2, 'Tornillo', 'Para paredes', 30, 10, (30*10))
    print(m1)