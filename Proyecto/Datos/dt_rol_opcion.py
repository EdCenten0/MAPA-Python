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
            sql = (f'''INSERT INTO rol_opcion (id_rol, id_opcion, estado) VALUES ('{Rol_opcion.id_rol}','{Rol_opcion.id_opcion}', '{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarRol_Opcion: {e}")

        return indicador


    @classmethod
    def editarRolOpcion(cls, Rol_opcion):

        try:
            indicador = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE rol_opcion SET id_opcion = {Rol_opcion.id_opcion}, id_rol = {Rol_opcion.id_rol}, estado = {2} WHERE rol_opcion_id = {Rol_opcion.rol_opcion_id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarRolOpcion: {e}")

        return indicador


    @classmethod
    def eliminarRolOpcion(cls, Rol_opcion):

        try:
            indicador = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM rol_opcion WHERE rol_opcion_id = {Rol_opcion.rol_opcion_id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as e:
            print(f"Error en eliminarRolOpcion: {e}")

        return indicador