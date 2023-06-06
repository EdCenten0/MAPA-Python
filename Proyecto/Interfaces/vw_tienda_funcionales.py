import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from Proyecto.Interfaces import vw_tienda
from Proyecto.Datos.dt_tienda import Dt_tienda
from Proyecto.Entidades.tienda import Tienda


class VentanaTienda(QMainWindow, vw_tienda.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaTienda, self).__init__(parent)
        self.setupUi(self)

        #Botones
        self.bt_editar.clicked.connect(self.mostrarFrame)
        self.bt_guardar.clicked.connect(self.editarTienda)
        self.bt_vaciar.clicked.connect(self.vaciarCampos)

        #Funciones
        self.ocultarFrame()
        self.llenarDatos()

    def vaciarCampos(self):
        self.line_nombre.clear()
        self.line_telefono.clear()
        self.line_direccion.clear()
        self.line_email.clear()

    def ocultarFrame(self):
        self.fr_datos_1.setVisible(False)
        self.fr_datos_2.setVisible(False)
        self.bt_editar.setVisible(True)


    def mostrarFrame(self):
        self.fr_datos_1.setVisible(True)
        self.fr_datos_2.setVisible(True)
        self.bt_editar.setVisible(False)

    def llenarDatos(self):

        listaTienda = Dt_tienda.listarRol()
        self.lb_id.setText("1")
        for t in listaTienda:
            #Labels
            self.lb_nombre.setText(t["nombre"])
            self.lb_email.setText(t["email"])
            self.lb_direccion.setText(t["direccion"])
            self.lb_telefono.setText(t["telefono"])

            #Edits Lines
            self.line_nombre.setText(t["nombre"])
            self.line_email.setText(t["email"])
            self.line_direccion.setText(t["direccion"])
            self.line_telefono.setText(t["telefono"])

    def editarTienda(self):
        Tienda.id_tienda = 1
        Tienda.nombre = self.line_nombre.text()
        Tienda.direccion = self.line_direccion.toPlainText()
        Tienda.email = self.line_email.text()
        Tienda.telefono = self.line_telefono.text()

        if not self.line_nombre.text() == "" and not self.line_telefono.text() == "" and not self.line_direccion.toPlainText() == "" and not self.line_email == "":
            if len(self.line_nombre.text()) <= 50:

                if len(self.line_telefono.text()) <= 12:

                    if len(self.line_direccion.toPlainText()) <= 200:

                        if len(self.line_email.text()) <= 50:

                            Dt_tienda.editarRol(Tienda)
                            QMessageBox.about(self, "Exito!", "Los Datos de la tienda fueron modificados")
                            self.ocultarFrame()
                            self.llenarDatos()

                        else:
                            QMessageBox.about(self, "Error!", "El nombre de la tienda debe tener menos de 50 caracteres")

                    else:
                        QMessageBox.about(self, "Error!", "La direccion de la tienda debe tener menos de 200 caracteres")

                else:
                    QMessageBox.about(self, "Error!", "El telefono de tienda debe tener menos de 12 caracteres")

            else:
                QMessageBox.about(self, "Error!", "El email de la tienda debe tener menos de 50 caracteres")

        else:
            QMessageBox.about(self, "Error!", "Llene todos los campos vacios")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = VentanaTienda()
    mw.show()
    sys.exit(app.exec_())