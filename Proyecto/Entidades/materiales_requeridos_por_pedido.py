import copy


#Entidad de los materiales requeridos por pedido
class materiales_requerido_por_pedido:

    #Metodo constructor
    def __init__(self, id_materiales_por_pedido=None, material=None, cantidad=None, unidad_de_medida=None,
                 precio_por_unidad_de_medida=None, precio_total=None, estado=None):
        self._id_materiales_por_pedido = id_materiales_por_pedido
        self._material = material
        self._cantidad = cantidad
        self._unidad_de_medida = unidad_de_medida
        self._precio_por_unidad_de_medida = precio_por_unidad_de_medida
        self._precio_total = precio_total
        self._estado = estado


    #Metodo toString
    def __str__(self):
        return f'''
        id_materiales_por_pedido: {self.id_materiales_por_pedido},
        material: {self.material},
        cantidad: {self._cantidad},
        unidad_de_medida: {self.unidad_de_medida},
        precio_por_unidad_de_medida: {self.precio_por_unidad_de_medida},
        precio_total: {self.precio_total},
        estado: {self.estado}        
        '''

    #Metodo para delvolver el objeto
    def __getitem__(self, item):
        mrp = copy.copy(self)
        mrp.id_materiales_por_pedido = mrp._id_materiales_por_pedido
        mrp.material = mrp._material
        mrp.cantidad = mrp._cantidad
        mrp.unidad_de_medida = mrp._unidad_de_medida
        mrp.precio_por_unidad_de_medida = mrp._precio_por_unidad_de_medida
        mrp.precio_total = mrp._precio_total
        mrp.estado = mrp._estado
        return mrp


#id_materiales_por_pedido

    #GETTER
    @property
    def id_materiales_por_pedido(self):
        return self._id_materiales_por_pedido

    #SETTER
    @id_materiales_por_pedido.setter
    def  id_materiales_por_pedido(self, id_materiales_por_pedido):
        self._id_materiales_por_pedido = id_materiales_por_pedido

#material

   #GETTER
    @property
    def material(self):
        return self._material

    #SETTER
    @material.setter
    def  material(self, material):
        self._material = material

#cantidad
    #GETTER
    @property
    def cantidad(self):
        return self._cantidad

    #SETTER
    @cantidad.setter
    def  cantidad(self, cantidad):
        self._cantidad = cantidad


#unidad de medida
    #GETTER
    @property
    def unidad_de_medida(self):
        return self._unidad_de_medida

    #SETTER
    @unidad_de_medida.setter
    def  unidad_de_medida(self, unidad_de_medida):
        self._unidad_de_medida = unidad_de_medida


#precio_por_unidad_de_medida
    #GETTER
    @property
    def precio_por_unidad_de_medida(self):
        return self._precio_por_unidad_de_medida

    #SETTER
    @precio_por_unidad_de_medida.setter
    def  precio_por_unidad_de_medida(self, precio_por_unidad_de_medida):
        self._precio_por_unidad_de_medida = precio_por_unidad_de_medida


#precio_total
    #GETTER
    @property
    def precio_total(self):
        return self._precio_total

    #SETTER
    @precio_total.setter
    def  precio_total(self, precio_total):
        self._precio_total = precio_total


#estado
    #GETTER
    @property
    def estado(self):
        return self._estado

    #SETTER
    @estado.setter
    def  estado(self, estado):
        self._estado = estado


if __name__ == '__main__':
    hola = materiales_requerido_por_pedido(1,"Hola", 2, "lb", 10.0, 100, 1)
    print(hola)



