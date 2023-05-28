import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QTableWidgetItem, QMessageBox

from Datos import dt_taller
from Datos.dt_taller import Dt_taller
from Entidades.taller import Taller
from Interfaces import vw_taller

class vw_taller_funciones(QtWidgets.QMainWindow, vw_taller.Ui_mw_taller):
    def __init__(self, parent=None):
        super(vw_taller_funciones, self).__init__(parent)
        self.setupUi(self)
        #Acciones de las tablas
        self.llenarTablaTaller(dt_taller.Dt_taller.listarTaller())
        self.tw_taller.itemSelectionChanged.connect(self.obtenerDatosTablaTaller)

        # Botones
        self.btnGuardar.clicked.connect(self.guardarTaller)

        self.btnEditar.clicked.connect(self.editarTaller)





    def limpiarCampos(self):

        if not self.txtNombre.text() == "" or not self.txtDireccion.text() == "" or not self.txtTelefono.text() == "" or not self.txtEmail.text() == "":
            self.txtNombre.clear()
            self.txtDireccion.clear()
            self.txtTelefono.clear()
            self.txtEmail.clear()

    def notMensaje(self, indicador, resultado):

        if indicador == True: #consulta
            QMessageBox.about(self, "Exito!", " los datos fueron " + resultado + " correctamente")
        else:
            QMessageBox.about(self, "Error", "Ha ocurrido un erro")

    def llenarTablaTaller(self, datos):

        vacio = ""
        print("\nDatos de la tabla Taller")

        i = len(datos)
        self.tw_taller.setRowCount(i)
        tableRow = 0

        for row in datos:
            self.tw_taller.setItem(tableRow, 0, QTableWidgetItem(row['nombre']))
            self.tw_taller.setItem(tableRow, 1, QTableWidgetItem(row['direccion']))
            self.tw_taller.setItem(tableRow, 2, QTableWidgetItem(row['telefono']))
            self.tw_taller.setItem(tableRow, 3, QTableWidgetItem(row['email']))
            tableRow += 1


    def guardarTaller(self):
       try:

           Taller.nombre = self.txtNombre.text()
           Taller.direccion = self.txtDireccion.text()
           Taller.telefono = self.txtTelefono.text()
           Taller.email = self.txtEmail.text()
           #Taller.id_tienda = 1

           if not self.txtNombre == "" and not self.txtDireccion.text() == "" and not self.txtTelefono.text() == "" and not self.txtEmail.text() == "":
               indicador = dt_taller.Dt_taller.guardarTaller(Taller)
               self.notMensaje(indicador, "Taller guardado")
               self.limpiarCampos()

               self.llenarTablaTaller(dt_taller.Dt_taller.listarTaller())

           else:
               self.notMensaje(False, "")

       except Exception as e:
           print(f"Error al guardar el usuario {e}")


    def editarTaller(self):
        try:
            Taller.id = self.lblID.text()
            Taller.nombre = self.txtNombre.text()
            Taller.direccion = self.txtDireccion.text()
            Taller.telefono = self.txtTelefono.text()
            Taller.email = self.txtEmail.text()

            if not self.txtNombre == "" and not self.txtDireccion.text() == "" and not self.txtTelefono.text() == "" and not self.txtEmail.text() == "" and not self.lblID.text() == 0:

                indicador = dt_taller.Dt_taller.editarTaller(Taller)
                self.notMensaje(indicador, "Taller editado")

                self.limpiarCampos()

                self.llenarTablaTaller(dt_taller.Dt_taller.listarTaller())

            else:

                self.notMensaje(False, "")
                self.limpiarCampos()


        except Exception as e:
            print(f"Ocurrio un error en {e}")

    def obtenerDatosTablaTaller(self):

        #se selecciona el dato de la tabla
        filaSeleccionada = self.tw_taller.currentRow()
        nombre = self.tw_taller.item(filaSeleccionada, 0).text()
        direccion = self.tw_taller.item(filaSeleccionada, 1).text()
        telefono = self.tw_taller.item(filaSeleccionada, 2).text()
        email = self.tw_taller.item(filaSeleccionada, 3).text()

        #se muestra el dato seleccionado
        self.txtNombre.setText(nombre)
        self.txtDireccion.setText(direccion)
        self.txtTelefono.setText(telefono)
        self.txtEmail.setText(email)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = vw_taller_funciones()
    mw.show()
    app.exec()