from Datos import Conexion
from Datos.dt_usuario import Dt_Usuarios
from Entidades.usuario_rol import Usuario_rol


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
            sql = (f'''INSERT INTO usuario_rol (id_usuario, id_rol, estado) VALUES ('{Usuario_rol.id_usuario}','{Usuario_rol.id_rol}', '{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario_Rol: {e}")

        return indicador

    @classmethod
    def editarUsuarioRol(cls, Usuario_rol):

        try:
            indicador = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE usuario_rol SET id_usuario = {Usuario_rol.id_usuario}, id_rol = {Usuario_rol.id_rol}, estado = {2} WHERE usuario_rol_id = {Usuario_rol.usuario_rol_id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario_Rol: {e}")

        return indicador


    @classmethod
    def eliminarUsuarioRol(cls, Usuario_rol):

        try:
            indicador = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM usuario_rol WHERE usuario_rol_id = {Usuario_rol.usuario_rol_id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario_Rol: {e}")

        return indicador




if __name__ == '__main__':
    print(Dt_Usuario_rol.eliminarUsuarioRol())