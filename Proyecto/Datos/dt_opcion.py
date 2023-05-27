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
    def guardarOpcion(cls, Opcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO opcion (descripcion ,estado) VALUES ('{Opcion.opcion}', '{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarOpcion: {e}")

        return indicador



    @classmethod
    def editarOpcion(cls, Opcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE opcion SET descripcion = "{Opcion.opcion}", estado = '{2}' WHERE idopcion = {Opcion.idOpcion}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarOpcion: {e}")

        return indicador



    @classmethod
    def eliminarOpcion(cls, Opcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM opcion WHERE idopcion = {Opcion.idOpcion}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarOpcion: {ex}")

        return indicador

    @classmethod
    def tablaAsignarOpcion(cls):
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f'''Select descripcion FROM opcion''')
            querys = cursor.fetchall()
            cursor.close()
            return querys

        except Exception as ex:
            print(f"Error en llenarComboxOpcion: {ex}")

    @classmethod
    def ExisteRol(cls,Opcion):
        try:

            existe = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f"Select * FROM opcion WHERE descripcion = '{Opcion.opcion}' ")
            consulta = cursor.fetchall()

            if consulta:
                existe = True

            return existe

        except Exception as ex:
            print(f"Error en Opcion Existente:{ex}")


    @classmethod
    def buscarIndexOpcion(cls, id):

        try:

            listaOpcion = Dt_Opcion.listarOpcion()
            indice = 0

            for row in listaOpcion:
                indice += 1
                if row["idopcion"] == id:
                    break

            return indice

        except Exception as e:
            print(f"Error en buscarUsuario_Rol: {e}")



if __name__ == '__main__':
    print(Dt_Opcion.buscarIndexOpcion(3))
