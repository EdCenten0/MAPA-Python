import pymysql.cursors
import sys
from Datos.Conexion import Conexion
from Entidades.taller import Taller

class Dt_taller:

    @classmethod
    def listarTaller(cls):
        cursor = Conexion.obtenerConexion().cursor()
        sentencia = "SELECT * FROM taller"
        cursor.execute(sentencia)
        res = cursor.fetchall()
        cursor.close()
        return res

    @classmethod
    def guardarTaller(cls, Taller):

        indicador = False

        try:
            cursor = Conexion.obtenerConexion().cursor()
            sentencia = (f'''INSERT INTO taller (nombre, direccion, telefono, email, id_tienda) VALUES ('Taller D','Managua','76817986','denisse@mail.com','{1}')''')
            cursor.execute(sentencia)
            cursor.connection.commit()
            cursor.close()
            print("Taller Guardado")
            indicador = True

        except Exception as e:
            print(f"Error al guardar el taller:{e}")

        return indicador


    @classmethod
    def editarTaller(cls):
        indicador = False

        try:
            cursor = Conexion.obtenerConexion().cursor()
            sentencia = (f'''UPDATE taller set nombre = 'Denisse T', direccion = 'Masaya', telefono = '85555646', email = 'isabel@gmail.com', id_tienda = '{1}' WHERE id_taller = 2''')
            cursor.execute(sentencia)
            cursor.connection.commit()
            cursor.close()
            print("Taller editado")
            indicador = True

        except Exception as e:
            print("Ocurrio un error en {}".format(e))
        return indicador


    @classmethod
    def eliminarTaller(cls):
        indicador = False

        try:
            cursor = Conexion.obtenerConexion().cursor()
            sentecia = f'''DELETE FROM taller WHERE id_taller = 3'''
            cursor.execute(sentecia)
            cursor.connection.commit()
            cursor.close()
            print("Taller eliminado")
            indicador = True

        except Exception as e:
            print(f"Ha ocurrido un error {e}")
        return  indicador

if __name__ == '__main__':
    taller1 = Dt_taller.listarTaller()
    for t in taller1:
        print(t)
    #taller2 = Dt_taller.guardarTaller()
    #taller3 = Dt_taller.editarTaller()
    #taller4 = Dt_taller.eliminarTaller()


