# Francisco de Jesús Melendez Simplina

from Datos import Conexion


class Dt_Usuarios:

    @classmethod
    def listarUsuarios(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM usuario")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarUsuario(cls, Usuarios):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO usuario ( nombre, apellido, user, clave, fecha_creacion, estado ) VALUES ('{Usuarios.nombre}','{Usuarios.apellido}','{Usuarios.user}','{Usuarios.apellido}', now(),'{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario: {e}")

        return indicador



    @classmethod
    def editarUsuario(cls, Usuarios):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE usuario SET nombre = "{Usuarios.nombre}" , apellido = "{Usuarios.apellido}" , user = "{Usuarios.user}", clave = "{Usuarios.password}", fecha_creacion = "{Usuarios.fechaCreacion}", estado = "{2}" WHERE id_usuario = {Usuarios.id_usuario}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarUsuario: {e}")

        return indicador



    @classmethod
    def eliminarUsuario(cls, Usuarios):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM usuario WHERE id_usuario = {Usuarios.id_usuario}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarUsuario: {ex}")

        return indicador

    @classmethod
    def ExisteUsuario(cls,Usuarios):
        try:

            existe = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f"Select * FROM usuario WHERE user = '{Usuarios.user}' ")
            consulta = cursor.fetchall()

            if consulta:
                existe = True

            return existe

        except Exception as ex:
            print(f"Error en Usuario Existente:{ex}")

    @classmethod
    def buscarIndexUsuario(cls, id):

        try:

            listaUsuario = Dt_Usuarios.listarUsuarios()
            indice = 0

            for row in listaUsuario:
                indice += 1
                if row["id_usuario"] == id:
                    break

            return indice

        except Exception as e:
            print(f"Error en buscarUsuario_Rol: {e}")



if __name__ == '__main__':
    print(Dt_Usuarios.buscarIndexUsuario(3))

