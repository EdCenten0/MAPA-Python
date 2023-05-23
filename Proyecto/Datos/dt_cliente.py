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
    def guardarClientes(cls, Clientes):


        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO usuario ( nombre, apellido, direccion, correo, telefono, cedula) VALUES ('{Clientes.nombre}','{Clientes.apellido}','{Clientes.direccion}','{Clientes.correo}','{Clientes.telefono}','{Clientes.cedula}','{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")
            indicador = True

        except Exception as e:
            print(f"Error en guardarUsuario: {e}")

        return indicador



    @classmethod
    def editarClientes(cls, Clientes):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE usuario SET nombre = "{Clientes.nombre}" , apellido = "{Clientes.apellido}" , direccion = "{Clientes.direccion}", correo = "{Clientes.correo}", telefono = "{Clientes.telefono}", cedula = "{Clientes.cedula}", estado = "{2}" WHERE id_cliente = {Clientes.id_cliente}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")
            indicador = True

        except Exception as e:
            print(f"Error en editarUsuario: {e}")

        return indicador



    @classmethod
    def eliminarClientes(cls, Clientes):

        indicador = False

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM usuario WHERE id_usuario = {Clientes.id_usuario}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")
            indicador = True

        except Exception as ex:
            print(f"Error en eliminarClientes: {ex}")

        return indicador

    @classmethod
    def ExisteClientes(cls,Clientes):
        try:

            existe = False
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute(f"Select * FROM clientes WHERE id_cliente = '{Clientes.id_cliente}' ")
            consulta = cursor.fetchall()

            if consulta:
                existe = True

            return existe

        except Exception as ex:
            print(f"Error en Cliente Existente:{ex}")

if __name__ == '__main__':
    print(Dt_Clientes.llenarComboxCliente())

