from Datos import Conexion


class Dt_rol_opcion:

    @classmethod
    def listarRolOpcion(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM rol_opcion")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarRolOpcion(cls, Rol_opcion):

        try:

            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO rol_opcion (id_rol, id_opcion) VALUES ('{Rol_opcion.id_rol}','{Rol_opcion.id_opcion}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarRol_Opcion: {e}")

        return indicador