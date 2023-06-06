from Proyecto.Datos import Conexion

class Dt_Clientes:

    @classmethod
    def listarClientes(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM clientes")
        querys = cursor.fetchall()
        cursor.close()
        return querys

    def listarSoloUnCliente(id_cliente):
        from Datos import Conexion
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        sql_query = (f"SELECT * FROM clientes WHERE id_cliente = {id_cliente}")
        cursor.execute(sql_query)
        registro = cursor.fetchall()
        cursor.close()
        return registro


    @classmethod
    def guardarClientes(cls, cliente):


        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = f'''INSERT INTO clientes (nombre, apellido, email, telefono, cedula, id_tienda, estado) 
                      VALUES ('{cliente.nombre}', '{cliente.apellido}', '{cliente.email}', '{cliente.telefono}', '{cliente.cedula}', 1 , 1)'''
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
            sql = (f'''UPDATE clientes SET nombre = "{cliente.nombre}" , apellido = "{cliente.apellido}", emauk = "{cliente.email}", telefono = "{cliente.telefono}", cedula = "{cliente.cedula}"''')
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
    def ExisteClientes(cls, cliente):
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

    @classmethod
    def buscarIndexCliente(cls, id):
        try:
            listarVenta = cls.listarVentas()
            indice = 0

            for row in listarVenta:
                indice += 1
                if row["id_venta"] == id:
                    break

            return indice

        except Exception as ex:
            print(f"Error al buscar indice cliente: {ex}")

if __name__ == '__main__':
    print(Dt_Clientes.listarClientes())

