# Francisco de Jesús Melendez Simplina

from Datos import Conexion


class Dt_Rol:

    @classmethod
    def listarRol(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM rol")
        querys = cursor.fetchall()
        cursor.close()
        return querys



    @classmethod
    def guardarRol(cls, descripcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO rol (descripcion) VALUES ('{descripcion}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarRol: {e}")

        return indicador



    @classmethod
    def editarRol(cls, id, descripcion):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE rol SET descripcion = "{descripcion}" WHERE idrol = {id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarRol: {e}")

        return indicador



    @classmethod
    def eliminarRol(cls, id):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM rol WHERE idrol = {id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarRol: {ex}")

        return indicador



if __name__ == '__main__':
    print(Dt_Rol.listarRol())
