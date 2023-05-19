import sys

from Datos import Conexion
from Entidades.materiales_por_proveedor import MaterialesPorProveedor


class DtMaterialesPorProveedor:
    #Carlos Eduardo Chavarria Centneo
    _SELECT = "SELECT * FROM materiales_por_proveedor"  #Para mi yo del futuro: recuerda agregar el estado
    _INSERT = "INSERT INTO materailes_por_proveedor(id_proveedor, id_material) VALUES (%s, %s)"
    _UPDATE = "UPDATE materiales_por_proveedor set id_proveedor= %s, id_material= %s, estado = 2 WHERE id= %s" #Tambien hay que cambiar el estado a 2
    _DELETE = "UPDATE materiales_por_proveedor set estado = 3 WHERE id = %s"
    _cursor = None
    @classmethod
    def listar_materiales_por_proveedor(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        materiales_por_proveedores = []
        for x in resultado:
            m = MaterialesPorProveedor(x['id_materiales_por_proveedor'], x['id_proveedor'], x['id_material'])
            materiales_por_proveedores.append(m)
            print('si', materiales_por_proveedores)
        return materiales_por_proveedores

if __name__ == '__main__':
    materiales_por_proveedores =DtMaterialesPorProveedor.listar_materiales_por_proveedor()
    for u in materiales_por_proveedores:
        print(u)

    # def listarUsuario(cls):
    #     cursor = Conexion.getConnection().cursor()
    #     cursor.execute(cls._SELECT)
    #     resultado = cursor.fetchall()
    #     usuarios = []
    #     for x in resultado:
    #         u = Usuario(x['idusuario'], x['nombre'], x['apellido'], x['nombreusuario'],
    #                     x['clave'], x['fecha_creacion'], x['estado'])
    #         usuarios.append(u)
    #         print('usuarios', usuarios)
    #     return usuarios