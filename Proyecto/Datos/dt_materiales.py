from Datos.Conexion import Conexion
from Entidades.materiales import Materiales

class Dt_materiales:

    _SELECT = "SELECT * FROM materiales"

    @classmethod
    def listarMateriales(cls):
        cursor = Conexion.obtenerConexion().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        materiales = []
        for ma in resultado:
            m = Materiales(ma['id_material'], ma['nombre_material'], ma['descripcion'], ma['cantidad'], ma['unidad_de_medida'], ma['precio_por_unidad'], ma['precio_total'], ma['id_pedido'])
            materiales.append(m)
            print("materiales: ", materiales)
        return materiales



if __name__ == '__main__':
    materiales1 = Dt_materiales.listarMateriales()
    for m in materiales1:
        print(m)