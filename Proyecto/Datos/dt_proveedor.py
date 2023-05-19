#Francisco de Jesús Meléndez Simplina

from Datos import Conexion

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


        except Exception as e:
            print(f"Error en dt_Proveedor Guardar: {e}")


if __name__ == '__main__':
    print(Dt_Proveedor.listarProveedor())