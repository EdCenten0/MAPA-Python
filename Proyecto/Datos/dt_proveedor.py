#Francisco de Jesús Meléndez Simplina

from Proyecto.Datos import Conexion

class Dt_Proveedor:

    @classmethod
    def listarProveedor(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM proveedores")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarProveedor(cls, Proveedor):

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f"INSERT INTO proveedores ( id_tienda, nombre, email, telefono, catalogo, ruc, direccion, estado) VALUES ( '{1}', '{Proveedor.nombre}', '{Proveedor.correo}', '{Proveedor.telefono}', '{Proveedor.catalogo}', '{Proveedor.ruc}', '{Proveedor.direccion}'  , '{1}')")
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            return True


        except Exception as e:
            print(f"Error en dt_Proveedor Guardar: {e}")


    @classmethod
    def editarProveedor(cls, Proveedor):

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE proveedores SET id_tienda = '{1}', nombre = '{Proveedor.nombre}', email = '{Proveedor.correo}', telefono = '{Proveedor.telefono}', catalogo = '{Proveedor.catalogo}', ruc = '{Proveedor.ruc}', direccion = '{Proveedor.direccion}', estado = '{2}' WHERE id_proveedor = {Proveedor.id_proveedor}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            return True

        except Exception as e:
            print(f"Error en dt_Proveedor Editar: {e}")


    @classmethod
    def eliminarProveedor(cls, Proveedor):

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f''' DELETE FROM proveedores WHERE id_proveedor = {Proveedor.id_proveedor}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            return True


        except Exception as e:
            print(f"Error en dt_Proveedor Eliminar: {e}")



if __name__ == '__main__':
    print(Dt_Proveedor.listarProveedor())