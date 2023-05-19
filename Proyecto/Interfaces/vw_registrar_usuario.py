import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Interfaces import vw_registrar_usuario_login
from Interfaces.vw_login import Ui_Login


class registrar_Window(QMainWindow, vw_registrar_usuario_login.Ui_Registrar):
    def __init__(self):
        super(registrar_Window, self).__init__()
        self.setupUi(self)

        self.bt_registrar.clicked.connect(self.abrirLogin)

    def abrirLogin(self):
        try:
            self.close()
            self.ventana = QMainWindow()
            self.ventana_login = Ui_Login()
            self.ventana_login.setupUi(self.ventana)
            self.ventana.show()

        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = registrar_Window()
    mw.show()
    sys.exit(app.exec_())

