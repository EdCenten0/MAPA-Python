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
            sql = (f"INSERT INTO pedidos (descripcion, fecha_pedido, id_cliente) VALUES ({Pedido.descripcion}, {Pedido.idPedido}, {Pedido.fecha_Pedido}, {Pedido.idCliente})")
