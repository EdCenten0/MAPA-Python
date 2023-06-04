import sys

import pymysql

from Datos import Conexion
from Entidades.materiales_por_proveedor import MaterialesPorProveedor


class DtMaterialesPorProveedor:
    #Carlos Eduardo Chavarria Centneo
    _SELECT = "SELECT * FROM materiales_por_proveedor"  #Para mi yo del futuro: recuerda agregar el estado
    _INSERT = "INSERT INTO materiales_por_proveedor(id_proveedor, id_material) VALUES (%s, %s)"
    _UPDATE = "UPDATE materiales_por_proveedor set id_proveedor= %s, id_material= %s, estado = 2 WHERE id= %s" #Tambien hay que cambiar el estado a 2
    _DELETE = "UPDATE materiales_por_proveedor set estado = 3 WHERE id = %s"
    _SELECT_VISTA = "SELECT * FROM MAPA.materiales_por_proveedor_vistas"
    _cursor = None

    @classmethod
    def listar_vista(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute(cls._SELECT_VISTA)
        resultado = cursor.fetchall()
        mpp_vistas = []
        for m in resultado:
            mpp_vista = MaterialesPorProveedor(m["id_materiales_por_proveedor"],m["id_proveedor"], m["id_material"], m["nombre_material"], m["descripcion"], m["cantidad"], m["unidad_de_medida"], m["nombre"], m["catalogo"])
            mpp_vistas.append(mpp_vista)
        return mpp_vistas


    @classmethod
    def listar_materiales_por_proveedor(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        materiales_por_proveedores = []
        for x in resultado:
            m = MaterialesPorProveedor(x['id_materiales_por_proveedor'], x['id_proveedor'], x['id_material'])
            materiales_por_proveedores.append(m)
        return materiales_por_proveedores

    @classmethod
    def guardar_materiales_por_proveedor(cls, mpp):
        flag = False
        try:
            mppSetQuery =(mpp.id_proveedor, mpp.id_material)
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(cls._INSERT, mppSetQuery)
            cursor.connection.commit()
            cursor.close()
            Conexion.Conexion.obtenerConexion().close()
            flag = True
        except pymysql.Error as e:
            print(f"Error al guardar materiales_por_proveedor: {e}")

        return flag

    def editar_materiales_por_proveedor(cls, mpp):
        flag = False
        try:
            mppSetQuery = (mpp.id_materiales_por_proveedor, mpp.id_proveedor, mpp.id_material)
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(cls._UPDATE, mppSetQuery)
            cursor.connection.commit()
            cursor.close()
            Conexion.Conexion.obtenerConexion().close()
            flag = True
        except pymysql.Error as e:
            print(f"Error al editar materiales_por_provedor: {e}")

        return flag


    def eliminar_materiales_por_proveedor(cls, mpp):
        flag = False
        try:
            mppSetQuery = (mpp.id_proveedor)
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(cls._DELETE, mppSetQuery)
            cursor.connection.commit()
            cursor.close()
            Conexion.Conexion.obtenerConexion().close()
            flag = True
        except pymysql.Error as e:
            print(f"Error al eliminar materiales_por_proveedor: {e}")

        return  flag

if __name__ == '__main__':
     materiales_por_proveedores =DtMaterialesPorProveedor.listar_materiales_por_proveedor()
     for u in materiales_por_proveedores:
        print(u)

    # hola = MaterialesPorProveedor(None, 2, 1)
    # DtMaterialesPorProveedor.guardar_materiales_por_proveedor(hola)

