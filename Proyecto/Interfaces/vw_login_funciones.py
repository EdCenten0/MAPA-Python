# Francisco de Jesús Melendez Simplina

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from Interfaces import vw_login
from Interfaces.vw_registrar_funciones import registrar_Window


class login_Window(QMainWindow, vw_login.Ui_Login):
    def __init__(self):
        super(login_Window, self).__init__()
        self.setupUi(self)
        self.bt_ingresar.clicked.connect(self.abrirRegistrar)

    def abrirRegistrar(self):
        try:
            self.registrar_window = registrar_Window()
            self.registrar_window.show()

        except Exception as e:
            print(f"ERROR: {e}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = login_Window()
    mw.show()
    sys.exit(app.exec_())
