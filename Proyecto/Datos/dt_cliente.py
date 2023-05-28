# Francisco de Jesús Melendez Simplina

from Datos import Conexion

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
            sql = f'''INSERT INTO clientes (nombre, apellido, email, telefono, cedula, id_tienda, estado) 
                      VALUES ('{cliente.nombre}', '{cliente.apellido}', '{cliente.email}', '{cliente.telefono}', '{cliente.cedula}', 1 , 1)'''
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario: {e}")

        return indicador



    @classmethod
    def editarClientes(cls, cliente):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE usuario SET nombre = "{cliente.nombre}" , apellido = "{cliente.apellido}", emauk = "{cliente.email}", telefono = "{cliente.telefono}", cedula = "{cliente.cedula}"''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarUsuario: {e}")

        return indicador



    @classmethod
    def eliminarClientes(cls, cliente):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM usuario WHERE id_usuario = {cliente.id_usuario}''')
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
