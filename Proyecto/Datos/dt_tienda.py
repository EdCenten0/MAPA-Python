# Francisco de Jesús Melendez Simplina

from Datos import Conexion
from Entidades import tienda


class Dt_tienda:

    @classmethod
    def listarRol(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM tienda")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def editarRol(cls, Tienda):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE tienda SET nombre = "{Tienda.nombre}", direccion = "{Tienda.direccion}", telefono = "{Tienda.telefono}", email = "{Tienda.email}", estado = '{2}' WHERE id_tienda = "{Tienda.id_tienda}"''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarTienda: {e}")

        return indicador


if __name__ == '__main__':
    print(Dt_tienda.listarRol())