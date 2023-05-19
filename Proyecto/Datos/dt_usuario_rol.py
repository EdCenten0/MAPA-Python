from Datos import Conexion


class Dt_Usuario_rol:

    @classmethod
    def listarUsuario_rol(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM usuario_rol")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarUsuarioRol(cls, Usuario_rol):

        indicador = False



        try:

            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO usuario_rol (id_usuario, id_rol) VALUES ('{Usuario_rol.id_usuario}','{Usuario_rol.id_rol}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario_Rol: {e}")

        return indicador