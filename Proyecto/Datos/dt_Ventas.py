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

        except Exception as e:
            print(e)

        return indicador

        if __name__ == '__main__':
            print(Dt_Ventas.listarVentas())
