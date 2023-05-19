import copy


#Entidad de los materiales requeridos por pedido
class MaterialesPorProveedor:

    #Metodo constructor
    def __init__(self, id_materiales_por_proveedor = None, id_material = None, id_proveedor = None, estado = None):
        self._id_materiales_por_proveedor = id_materiales_por_proveedor
        self._id_material = id_material
        self._id_proveedor = id_proveedor
        self._estado = estado

    #Metodo toString
    def __str__(self):
        return f'''
        id_materiales_por_proveedor: {self.id_materiales_por_proveedor},
        id_material: {self._id_material},
        id_proveedor: {self._id_proveedor},
        estado: {self._estado}   
        '''

    #Metodo para delvolver el objeto
    def __getitem__(self, item):
        mrp = copy.copy(self)
        mrp.id_por_proveedor = mrp._id_materiales_por_proveedor
        mrp.id_material = mrp._id_material
        mrp.id_proveedor = mrp._id_proveedor
        mrp.estado = mrp._estado
        return mrp


#id_materiales_por_proveedor

    #GETTER
    @property
    def id_materiales_por_proveedor(self):
        return self._id_materiales_por_proveedor

    #SETTER
    @id_materiales_por_proveedor.setter
    def  id_materiales_por_proveedor(self, id_materiales_por_proveedor):
        self._id_materiales_por_proveedor = id_materiales_por_proveedor

#id_material

   #GETTER
    @property
    def id_material(self):
        return self._id_material

    #SETTER
    @id_material.setter
    def  id_material(self, id_material):
        self._id_material = id_material

#id_proveedor
    #GETTER
    @property
    def id_proveedor(self):
        return self._id_proveedor

    #SETTER
    @id_proveedor.setter
    def  id_proveedor(self, id_proveedor):
        self._id_proveedor = id_proveedor



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
    hola = MaterialesPorProveedor(1, 2, 1, 3)
    print(hola)



