import Conexion

class Dt_Ventas:
    @classmethod
    def listarVentas(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM ventas")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarVenta(cls, Venta):
        indicador = False
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f"INSERT INTO ventas (id_tienda, id_factura, cantidad, descripcion) VALUES ({Venta.id_tienda}, {Venta.id_factura}, {Venta.cantidad}, {Venta.descripcion})")
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            indicador = True

        except Exception as ex:
            print(ex)
        return indicador

    @classmethod
    def editarVenta(cls, Venta):
        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE ventas SET id_tienda = {Venta.id_tienda},  id_factura = {Venta.id_factura}, cantidad = {Venta.cantidad}, descripcion = "{Venta.descripcion}"''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Venta editada")
            indicador = True

        except Exception as ex:
            print(f"Error al editar venta: {ex}")
        return indicador

    @classmethod
    def eliminarVenta(cls, Venta):
        indicador = False
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM ventas WHERE id_venta = {Venta.id_Venta}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Registro de ventas eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error al eliminar Venta: {ex}")

        return indicador



if __name__ == '__main__':
    print(Dt_Ventas.listarVentas())
