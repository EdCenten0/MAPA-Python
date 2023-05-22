# Francisco de Jesús Melendez Simplina

from Datos import Conexion
from Entidades import roles


class Dt_Rol:

    @classmethod
    def listarRol(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM rol")
        querys = cursor.fetchall()
        cursor.close()
        return querys



    @classmethod
    def guardarRol(cls, Rol):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO rol (descripcion) VALUES ('{Rol.rol}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarRol: {e}")

        return indicador



    @classmethod
    def editarRol(cls, Rol):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE rol SET descripcion = "{Rol.rol}" WHERE id_rol = {Rol.id_rol}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarRol: {e}")

        return indicador



    @classmethod
    def eliminarRol(cls, Rol):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM rol WHERE id_rol = {Rol.id_rol}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarRol: {ex}")

        return indicador



    @classmethod
    def ExisteRol(cls,Rol):
        try:

            existe = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f"Select * FROM rol WHERE descripcion = '{Rol.rol}' ")
            consulta = cursor.fetchall()

            if consulta:
                existe = True

            return existe

        except Exception as ex:
            print(f"Error en Rol Existente:{ex}")



if __name__ == '__main__':
    print(Dt_Rol.ExisteRol())

