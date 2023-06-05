from Proyecto.Datos.Conexion import Conexion

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
            sentencia = (f'''INSERT INTO materiales(nombre_material, descripcion, cantidad, unidad_de_medida, precio_por_unidad, precio_total, id_pedido) VALUES('{Materiales.nombre_material}', '{Materiales.descripcion}', '{Materiales.cantidad}', '{Materiales.unidad_de_medida}', '{Materiales.precio_por_unidad}', '{Materiales.precio_total}', '{Materiales.id_pedido}')''')
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
            sentecia = (f'''UPDATE materiales SET nombre_material = '{Materiales.nombre_material}', descripcion = '{Materiales.descripcion}', cantidad = '{Materiales.cantidad}', unidad_de_medida = '{Materiales.unidad_de_medida}', precio_por_unidad = '{Materiales.precio_por_unidad}', precio_total = {Materiales.precio_total}, id_pedido = "{Materiales.id_pedido}" WHERE id_material = {Materiales.id_material} ''')
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


if __name__ == '__main__':
    materiales1 = Dt_materiales.listarMateriales()
    for m in materiales1:
        print(m)