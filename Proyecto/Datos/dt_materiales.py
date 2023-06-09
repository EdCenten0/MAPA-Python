from Datos.Conexion import Conexion
from Entidades import pedidos, materiales


class Dt_materiales:

    @classmethod
    def listarMateriales(cls):
        cursor = Conexion.obtenerConexion().cursor()
        sentencia = "SELECT * FROM materiales"
        cursor.execute(sentencia)
        res = cursor.fetchall()
        cursor.close()
        return res

    @classmethod
    def listarSoloUnUsuario(cls, id):
        cursor = Conexion.obtenerConexion().cursor()
        query = f"SELECT * FROM materiales WHERE id_material = {id}"
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res

    @classmethod
    def buscarMaterial(cls, nombre_material):

        cursor = Conexion.obtenerConexion().cursor()
        sentencia = (f"SELECT * FROM MAPA.materiales WHERE nombre_material like '%' '{nombre_material}' '%'")
        cursor.execute(sentencia)
        resultado_materiales = cursor.fetchall()
        cursor.connection.commit()
        cursor.close()
        return resultado_materiales

    @classmethod
    def guardarMaterial(cls, Materiales):

        indicador = False
        try:

            cursor = Conexion.obtenerConexion().cursor()
            sentencia = (
                f'''INSERT INTO materiales(nombre_material, descripcion, cantidad, unidad_de_medida, precio_por_unidad, precio_total, id_pedido) VALUES('{Materiales.nombre_material}', '{Materiales.descripcion}', '{Materiales.cantidad}', '{Materiales.unidad_de_medida}', '{Materiales.precio_por_unidad}', '{Materiales.precio_total}', '{Materiales.id_pedido}')''')
            cursor.execute(sentencia)
            cursor.connection.commit()
            cursor.close()
            print("Material Guardado")
            indicador = True

        except Exception as e:
            print(f"Error al guardar el material: {e}")

        return indicador

    @classmethod
    def editarMaterial(cls, Materiales):

        indicador = True

        try:

            cursor = Conexion.obtenerConexion().cursor()
            sentecia = (
                f'''UPDATE materiales SET nombre_material = '{Materiales.nombre_material}', descripcion = '{Materiales.descripcion}', cantidad = '{Materiales.cantidad}', unidad_de_medida = '{Materiales.unidad_de_medida}', precio_por_unidad = '{Materiales.precio_por_unidad}', precio_total = {Materiales.precio_total}, id_pedido = "{Materiales.id_pedido}" WHERE id_material = {Materiales.id_material} ''')
            cursor.execute(sentecia)
            cursor.connection.commit()
            cursor.close()
            print("Material Guardado")
            indicador = True

        except Exception as e:
            print(f"Occurio un error al editar el taller {e}")
        return indicador

    @classmethod
    def eliminarMaterial(cls, Materiales):

        indicador = True

        try:

            cursor = Conexion.obtenerConexion().cursor()
            sentencia = (f"DELETE FROM materiales WHERE id_material = {Materiales.id_material}")
            cursor.execute(sentencia)
            cursor.connection.commit()
            cursor.close()
            print("Material eliminado")
            indicador = True

        except Exception as e:
            print(f"Error al elimianr el material {e}")
        return indicador

    @classmethod
    def buscarIndexMateriall(cls, id):

        try:

            listarMateriales = cls.listarMateriales()
            indice = 0

            for row in listarMateriales:
                indice += 1
                if row["id_material"] == id:
                    break

            return indice

        except Exception as e:
            print(f"Error en buscar_index_material: {e}")

    @classmethod
    def contarMaterialesPorPedido(cls, id_pedido):
        cursor = Conexion.obtenerConexion().cursor()
        cursor.execute(f"SELECT COUNT(id_material) AS 'cuenta' FROM materiales WHERE id_pedido = {id_pedido}")
        nRegistros = cursor.fetchall()
        cuenta = []
        for n in nRegistros:
            cuenta = n["cuenta"]
        cursor.close()

        return cuenta

    @classmethod
    def sumarPrecioMateriales(cls, id_pedido : int):
        cursor = Conexion.obtenerConexion().cursor()
        cursor.execute(f"SELECT SUM(precio_total) AS suma FROM materiales WHERE id_pedido = {id_pedido}")
        registro = cursor.fetchall()
        cantidad : int
        for n in registro:
            cantidad = n["suma"]
        cursor.close()
        return cantidad

    #MATERIALES POR PEDIDO

    @classmethod
    def listarMaterialesPorPedido(cls, id_pedido):
        cursor = Conexion.obtenerConexion().cursor()
        id_pedido = id_pedido
        print(id_pedido)
        sentencia = f"SELECT * FROM materiales WHERE id_pedido = {id_pedido}"
        cursor.execute(sentencia)
        res = cursor.fetchall()
        cursor.close()
        return res

    @classmethod
    def buscarMateriaPorPedido(cls, nombre_material, id_pedido):

        cursor = Conexion.obtenerConexion().cursor()
        sentencia = (f"SELECT * FROM MAPA.materiales WHERE nombre_material like '%' '{nombre_material}' '%' AND id_pedido = {id_pedido}")
        cursor.execute(sentencia)
        resultado_materiales = cursor.fetchall()
        cursor.connection.commit()
        cursor.close()
        return resultado_materiales

    # def guardarMaterialPorPedido(self, Materiales : materiales.Materiales):
    #     try:
    #         cursor = Conexion.obtenerConexion().cursor()
    #         sentencia = (
    #             f'''INSERT INTO materiales(nombre_material, descripcion, cantidad, unidad_de_medida, precio_por_unidad, precio_total, id_pedido) VALUES('{Materiales.nombre_material}', '{Materiales.descripcion}', '{Materiales.cantidad}', '{Materiales.unidad_de_medida}', '{Materiales.precio_por_unidad}', '{Materiales.precio_total}', '{Materiales.id_pedido}')''')
    #         cursor.execute(sentencia)
    #         cursor.connection.commit()
    #         cursor.close()
    #         print("Material Guardado")
    #         indicador = True
    #
    #     except Exception as e:
    #         print(f"Error al guardar el material: {e}")

if __name__ == '__main__':
    materiales1 = Dt_materiales.listarMateriales()
    for m in materiales1:
        print(m)
    Dt_materiales.contarMaterialesPorPedido(2)
    print(Dt_materiales.listarMaterialesPorPedido(pedidos.Pedido(2, None, None, None, None)))