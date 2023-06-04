import copy




class Materiales:
    def _init_(self, id_material=None, nombre_material=None, descripcion=None, cantidad=None, unidad_de_medida=None,
        precio_unidad=None, precio_total=None, id_pedido=None):
        self._id_material = id_material
        self._nombre_material = nombre_material
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._unidad_de_medida = unidad_de_medida
        self._precio_unidad = precio_unidad
        self._precio_total = precio_total
        self._id_pedido = id_pedido

    def _str_(self):
        return f'''
         id_material: {self._id_material},
         material: {self._nombre_material},
         descripcion: {self._descripcion},
         cantidad: {self._cantidad},
         unidad_de_medida: {self._unidad_de_medida},
         precio_unidad: {self._precio_unidad},
         precio_total: {self._precio_total},
         id_pedido: {self._id_pedido}
         '''

    def _getitem_(self, item):
        u = copy.copy(self)
        u.id_material = u._id_material
        u.nombre_material = u._nombre_material
        u.descripcion = u._descripcion
        u.cantidad = u._cantidad
        u.unidad_de_medida = u._unidad_de_medida
        u.precio_unidad = u._precio_unidad
        u.precio_total  = u._precio_total

    @property
    def id_material(self):
        return self._id_material

    @id_material.setter
    def id_material(self, id_material):
        self._id_material = id_material

    @property
    def nombre_material(self):
        return self._nombre_material

    @nombre_material.setter
    def nombre_material(self, nombre_material):
        self._nombre_material = nombre_material

    @property
    def descripcion(self):
        return self._descripcion


    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def unidad_de_medida(self):
        return self._unidad_de_medida

    @unidad_de_medida.setter
    def unidad_de_medida(self, unidad_de_medida):
        self._unidad_de_medida = unidad_de_medida

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def precio_unidad(self):
        return self._precio_unidad

    @precio_unidad.setter
    def precio_unidad(self, precio_unidad):
        self._precio_unidad = precio_unidad

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

if __name__ == '_main_':
    m1 = Materiales(2, 'Tornillo', 'Para paredes', 30, 10, (30*10))
    print(m1)