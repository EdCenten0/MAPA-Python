import copy


#Entidad de los materiales requeridos por pedido
class MaterialesPorProveedor:

    #Metodo constructor
    def __init__(self, id_materiales_por_proveedor = None, id_proveedor = None, id_material = None, nombre_material = None, descripcion = None, cantidad = None, unidad_de_medida = None, nombre = None, catalogo = None,  estado = None):
        self._id_materiales_por_proveedor = id_materiales_por_proveedor
        self._id_proveedor = id_proveedor
        self._id_material = id_material
        self._nombre_material = nombre_material
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._unidad_de_medida = unidad_de_medida
        self._nombre = nombre
        self._catalogo =catalogo
        self._estado = estado

    #Metodo toString
    def __str__(self):
        return f'''
        id_materiales_por_proveedor: {self.id_materiales_por_proveedor},
        id_proveedor: {self._id_proveedor},
        id_material: {self._id_material},
        nombre_material: {self._nombre_material},
        descripcion: {self._descripcion},
        cantidad: {self._cantidad},
        unidad_de_medida: {self._unidad_de_medida},
        nombre: {self._nombre},
        catalogo: {self._catalogo},      
        estado: {self._estado}   
        '''

    #Metodo para delvolver el objeto
    def __getitem__(self, item):
        mrp = copy.copy(self)
        mrp.id_por_proveedor = mrp._id_materiales_por_proveedor
        mrp.id_proveedor = mrp._id_proveedor
        mrp.id_material = mrp._id_material
        mrp.descripcion = mrp._descripcion
        mrp.cantidad = mrp._cantidad
        mrp.unidad_de_medida = mrp._unidad_de_medida
        mrp.nombre = mrp._nombre
        mrp.catalogo = mrp._catalogo
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


#nombre_material
    #GETTER
    @property
    def nombre_material(self):
        return self._nombre_material

    #SETTER
    @nombre_material.setter
    def nombre_material(self, nombre_material):
        self._nombre_material = nombre_material


#descripcion
    #GETTER
    @property
    def descripcion(self):
        return self._descripcion

    #SETTER
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

#cantidad
    #GETTER
    @property
    def cantidad(self):
        return self._cantidad

    #SETTER
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

#unidad_de_medida
    #GETTER
    @property
    def unidad_de_medida(self):
        return self._unidad_de_medida

    #SETTER
    @unidad_de_medida.setter
    def unidad_de_medida(self, unidad_de_medida):
        self._unidad_de_medida = unidad_de_medida

#nombre
    #GETTER
    @property
    def nombre(self):
        return self._nombre

    #SETTER
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


#catalogo
    #GETTER
    @property
    def catalogo(self):
        return self._catalogo

    @catalogo.setter
    def catalogo(self, catalogo):
        self._catalogo = catalogo

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



