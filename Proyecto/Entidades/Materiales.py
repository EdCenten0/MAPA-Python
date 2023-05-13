import copy


class Materiales:
    def __init__(self, id=None, material=None, descripcion=None, cantidad=None, precio_unidad=None, precio_total=None):
        self._id = id
        self._material = material
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._precio_unidad = precio_unidad
        self._precio_total = precio_total

    def __str__(self):
        return f'''
        id: {self._id},
        material: {self._material},
        descripcion: {self._descripcion},
        cantidad: {self._cantidad},
        precio_unidad: {self._precio_unidad},
        precio_total: {self._precio_total}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.id = u._id
        u.material = u._material
        u.descripcion = u._descripcion
        u.cantidad = u._cantidad
        u.precio_unidad = u._precio_unidad
        u.precio_total  = u._precio_total

    @property
    def id(self):
        return self._id

    @id.setter
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

if __name__ == '__main__':
    m1 = Materiales(2, 'Tornillo', 'Para paredes', 30, 10, (30*10))
    print(m1)