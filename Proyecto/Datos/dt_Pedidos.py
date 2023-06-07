from PyQt5.QtWidgets import QMessageBox

from Datos import Conexion
from Entidades.pedidos import Pedido


class Dt_Pedidos:
    @classmethod
    def listarPedidos(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        sql = ("SELECT * FROM pedidos")
        cursor.execute(sql)
        querys = cursor.fetchall()
        cursor.close()
        return querys

    def listarSoloUnPedido(id_pedido):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        sql_query = (f"SELECT * FROM pedidos WHERE id_pedido = {id_pedido}")

        cursor.execute(sql_query)
        registro = cursor.fetchall()
        pedido : Pedido
        for n in registro:
            id_pedido = n["id_pedido"]
            id_cliente = n["id_cliente"]
            descripcion = n["descripcion"]
            fecha = n["fecha_pedido"]
            pedido = Pedido(id_pedido, id_cliente, descripcion, fecha)
        cursor.close()
        return pedido

    @classmethod
    def guardarPedido(cls, pedido: Pedido):
        indicador = False
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = "INSERT INTO pedidos (id_cliente, descripcion, fecha_pedido) VALUES (%s, %s, %s)"
            values = (pedido.id_cliente, pedido.descripcion, pedido.fecha_Pedido)
            cursor.execute(sql, values)
            cursor.connection.commit()
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
            sql = "UPDATE pedidos SET descripcion = %s, fecha_pedido = %s, id_cliente = %s WHERE id_pedido = %s"
            values = (Pedido.descripcion, Pedido.fecha_Pedido, Pedido.id_cliente, Pedido.id_pedido)
            cursor.execute(sql, values)
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
            sql = (f'''DELETE FROM pedidos WHERE id_pedido = {Pedido.id_pedido}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Registro de pedido eliminado")

        except Exception as ex:
            print(f"Error al eliminar pedido: {ex}")
        return indicador


if __name__ == '__main__':
    print(Dt_Pedidos.listarPedidos())
