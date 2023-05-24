import pymysql.cursors
import sys
from Datos.Conexion import Conexion
from Entidades.taller import Taller

class Dt_taller:
    _SELECT = "SELECT * FROM taller"
    _INSERT = "INSERT INTO MAPA.taller(id_taller, nombre, direccion, telefono, email, id_tienda) VALUES(%s, %s, %s, %s, 1)"

    @classmethod
    def listarTaller(cls):
        cursor = Conexion.obtenerConexion().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        taller = []

        for x in resultado:
            t = Taller(x['id_taller'], x['nombre'], x['direccion'], x['telefono'], x['email'], x['id_tienda'])
            taller.append(t)
            print("Taller: ", taller)
        return taller

    @classmethod
    def guardarTaller(cls, taller):
        conn = Conexion.obtenerConexion()
        cursor = Conexion.getCursor()
        try:
             print(f"Taller a insertar insertar: {taller}")
             val = (taller.nombre, taller.direccion, taller.telefono, taller.email, taller.id_tienda)
             cursor.execute(cls._INSERT, val)
             print(f'Taller insertado: {taller}')
             Conexion.commit()
             return cursor
        except Exception as e:
            print(f"Error {e}")



if __name__ == '__main__':
    taller1 = Dt_taller.listarTaller()
    for t in taller1:
        print(t)

    taller2 = Dt_taller.guardarTaller()
    for t2 in taller2:
        print(f"Usuario a insertar: {t2}")
