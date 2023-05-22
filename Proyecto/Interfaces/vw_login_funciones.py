import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from Interfaces import vw_login, vw_registrar_funciones
from Interfaces.vw_registrar_funciones import Ui_Registrar
from vw_registrar_funciones import registrar_Window

class login_Window(QMainWindow, vw_login.Ui_Login):
    def __init__(self, parent=None):
        super(login_Window, self).__init__(parent)
        self.setupUi(self)
        self.lb_crear_Usuario.mouseDoubleClickEvent(self.abrirRegistrar)


    def abrirRegistrar(self):
        try:
            self.ventana2 = QMainWindow()
            self.ventana_registrar = Ui_Registrar()
            self.ventana_registrar.setupUi(self.ventana2)
            self.ventana2.show()

        except Exception as e:
            print(f"ERROR: {e}")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = login_Window()
    mw.show()
    sys.exit(app.exec_())
