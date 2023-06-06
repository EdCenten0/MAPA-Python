from Datos import Conexion

class Dt_facturas:

    @classmethod
    def listarFacturas(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM facturas")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarFacturas(cls, factura):

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = f'''INSERT INTO facturas (id_factura, id_pedido, fecha, precio_materiales, mano_de_obra, precio_total, estado) 
                      VALUES ('{factura.id_factura}', '{factura.id_pedido}', '{factura.fecha}', '{factura.precio_materiales}', '{factura.mano_de_obra}', '{factura.precio_total}' , 1)'''
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarFacturas: {e}")

        return indicador
    @classmethod
    def eliminarFactura(cls, factura):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM facturas WHERE id_factura = {factura.id_factura}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarFactura: {ex}")

        return indicador

    @classmethod
    def ExisteFactura(cls, factura):
        try:

            existe = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f"Select * FROM facturas WHERE id_factura = '{factura.id_factura}' ")
            consulta = cursor.fetchall()

            if consulta:
                existe = True

            return existe

        except Exception as ex:
            print(f"Error en factura Existente:{ex}")

if __name__ == '__main__':
    print(Dt_facturas.listarFacturas())

