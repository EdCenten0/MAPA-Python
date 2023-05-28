import Conexion

class Dt_Pedidos:
    @classmethod
    def listarPedidos(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        sql = ("SELECT * FROM pedidos")
        cursor.execute(sql)
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarPedido(cls, Pedido):
        indicador = False
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f"INSERT INTO pedidos (descripcion, fecha_pedido, id_cliente) VALUES ({Pedido.descripcion}, {Pedido.idPedido}, {Pedido.fecha_Pedido}, {Pedido.id_cliente})")
            cursor.execute(sql)
            cursor.close()
            print("Pedido guardado")
            indicador = True

        except Exception as ex:
            print(f"Error al guardar pedido: {ex}")
        return indicador

    @classmethod
    def editarPedido(cls, Pedido):
        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE pedidos SET descripcion = {Pedido.descripcion}, fecha_pedido = {Pedido.fecha_Pedido}, id_cliente = {Pedido.id_cliente}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Pedido editado")

        except Exception as ex:
            print(f"Error al editar pedido: {ex}")

        return indicador

    @classmethod
    def eliminarPedido(cls, Pedido):
        indicador = False
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM pedidos WHERE id_pedidos = {Pedido.idPedido}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Registro de pedido eliminado")

        except Exception as ex:
            print(f"Error al eliminar pedido: {ex}")
        return indicador

