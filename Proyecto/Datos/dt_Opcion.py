# Francisco de Jesús Melendez Simplina

from Datos import Conexion


class Dt_Opcion:

    @classmethod
    def listarOpcion(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM opcion")
        querys = cursor.fetchall()
        cursor.close()
        return querys



    @classmethod
    def guardarOpcion(cls, descripcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO opcion (descripcion) VALUES ('{descripcion}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarOpcion: {e}")

        return indicador



    @classmethod
    def editarOpcion(cls, id, descripcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE opcion SET descripcion = "{descripcion}" WHERE idopcion = {id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarOpcion: {e}")

        return indicador



    @classmethod
    def eliminarOpcion(cls, id):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM opcion WHERE idopcion = {id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarOpcion: {ex}")

        return indicador



if __name__ == '__main__':
    print(Dt_Opcion.listarOpcion())
