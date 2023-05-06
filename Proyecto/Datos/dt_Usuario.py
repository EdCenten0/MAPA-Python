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
            sql = (f'''INSERT INTO usuario ( nombre, apellido, user, clave, fecha_creacion, estado) VALUES ('{Usuarios.nombre}','{Usuarios.apellido}','{Usuarios.user}','{Usuarios.apellido}','{Usuarios.fechaCreacion}','{1}')''')
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
            sql = (f'''UPDATE usuario SET nombre = "{Usuarios.nombre}" , apellido = "{Usuarios.apellido}" , user = "{Usuarios.user}", clave = "{Usuarios.password}", fecha_creacion = "{Usuarios.fechaCreacion}", estado = "{2}" WHERE idusuario = {Usuarios.idUsuario}''')
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
            sql = (f'''DELETE FROM usuario WHERE idusuario = {Usuarios.idUsuario}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarUsuario: {ex}")

        return indicador



if __name__ == '__main__':
    print(Dt_Usuarios.listarUsuarios)

