from Proyecto.Datos import Conexion

class Dt_Clientes:

    @classmethod
    def listarClientes(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM clientes")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    @classmethod
    def guardarClientes(cls, cliente):


        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f"INSERT INTO clientes ( id_tienda, nombre, apellido, cedula, email, telefono, estado) VALUES ( {1}, '{cliente.nombre}', '{cliente.apellido}', '{cliente.cedula}', '{cliente.email}', '{cliente.telefono}', '{1}')")

            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarCliente: {e}")

        return indicador



    @classmethod
    def editarClientes(cls, cliente):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE clientes SET id_tienda = '{1}', nombre = '{cliente.nombre}', apellido = '{cliente.apellido}', email = '{cliente.email}', telefono = '{cliente.telefono}', cedula = '{cliente.cedula}', estado = '{2}' WHERE id_cliente = {cliente.id_cliente}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarCliente: {e}")

        return indicador


    @classmethod
    def busqueda(cls, cliente):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute(f"SELECT * FROM clientes WHERE nombre like '%' '{cliente}' '%' ")
        querys = cursor.fetchall()
        cursor.close()
        return querys
    @classmethod
    def eliminarClientes(cls, cliente):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM clientes WHERE id_cliente = {cliente.id_cliente}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarClientes: {ex}")

        return indicador

    @classmethod
    def ExisteClientes(cls,cliente):
        try:

            existe = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f"Select * FROM clientes WHERE id_cliente = '{cliente.id_cliente}' ")
            consulta = cursor.fetchall()

            if consulta:
                existe = True

            return existe

        except Exception as ex:
            print(f"Error en Cliente Existente:{ex}")

if __name__ == '__main__':
    print(Dt_Clientes.listarClientes())

