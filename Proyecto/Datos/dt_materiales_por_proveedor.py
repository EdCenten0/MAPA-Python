import sys

import pymysql

from Proyecto.Datos import Conexion
from Proyecto.Entidades.materiales_por_proveedor import MaterialesPorProveedor


class DtMaterialesPorProveedor:
    # Carlos Eduardo Chavarria Centneo
    _SELECT = "SELECT mpp.id_materiales_por_proveedor, mpp.id_proveedor, mpp.id_material, m.nombre_material, m.descripcion, m.cantidad, m.unidad_de_medida, p.nombre, p.catalogo FROM MAPA.materiales_por_proveedor AS mpp INNER JOIN MAPA.materiales AS m ON mpp.id_material = m.id_material INNER JOIN MAPA.proveedores AS p ON mpp.id_proveedor = p.id_proveedor ORDER BY mpp.id_materiales_por_proveedor;"  # Para mi yo del futuro: recuerda agregar el estado
    _INSERT = "INSERT INTO materiales_por_proveedor(id_proveedor, id_material) VALUES (%s, %s)"
    _UPDATE = "UPDATE materiales_por_proveedor set id_proveedor= %s, id_material= %s, estado = 2 WHERE id_materiales_por_proveedor= %s"  # Tambien hay que cambiar el estado a 2
    _DELETE = "DELETE FROM materiales_por_proveedor WHERE id_materiales_por_proveedor = %s"
    _SELECT_VISTA = f"SELECT mpp.id_materiales_por_proveedor, mpp.id_proveedor, mpp.id_material, m.nombre_material, m.descripcion, m.cantidad, m.unidad_de_medida, p.nombre, p.catalogo FROM MAPA.materiales_por_proveedor AS mpp INNER JOIN MAPA.materiales AS m ON mpp.id_material = m.id_material INNER JOIN MAPA.proveedores AS p ON mpp.id_proveedor = p.id_proveedor"
    _cursor = None

    @classmethod
    def listar_materiales_por_proveedor(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        mpp_vistas = []
        for m in resultado:
            mpp_vista = MaterialesPorProveedor(m["id_materiales_por_proveedor"], m["id_proveedor"], m["id_material"],
                                               m["nombre_material"], m["descripcion"], m["cantidad"],
                                               m["unidad_de_medida"], m["nombre"], m["catalogo"])
            mpp_vistas.append(mpp_vista)
        return mpp_vistas


    @classmethod
    def guardar_materiales_por_proveedor(cls, id_proveedor, id_material):
        flag = False
        try:
            mppSetQuery = f"INSERT INTO materiales_por_proveedor(id_proveedor, id_material) VALUES ({id_proveedor}, {id_material})"
            print(mppSetQuery)
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(mppSetQuery)
            cursor.connection.commit()
            cursor.close()

            flag = True
        except pymysql.Error as e:
            print(f"Error al guardar materiales_por_proveedor: {e}")

        return flag

    @classmethod
    def editar_materiales_por_proveedor(cls, mpp: MaterialesPorProveedor):
        flag = False
        try:
            mppSetQuery = (mpp.id_proveedor, mpp.id_material, mpp.id_materiales_por_proveedor)
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(cls._UPDATE, mppSetQuery)
            cursor.connection.commit()
            cursor.close()

            flag = True
        except pymysql.Error as e:
            print(f"Error al editar materiales_por_provedor: {e}")

        return flag


    @classmethod
    def eliminar_materiales_por_proveedor(cls, mpp: MaterialesPorProveedor):
        try:
            mppSetQuery = mpp.id_materiales_por_proveedor
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(cls._DELETE, mppSetQuery)
            cursor.connection.commit()
            cursor.close()

        except pymysql.Error as e:
            print(f"Error al eliminar materiales_por_proveedor: {e}")




if __name__ == '__main__':
    materiales_por_proveedores = DtMaterialesPorProveedor.listar_materiales_por_proveedor()
    for u in materiales_por_proveedores:
        print(u)

# hola = MaterialesPorProveedor(None, 2, 1)
# DtMaterialesPorProveedor.guardar_materiales_por_proveedor(hola)
