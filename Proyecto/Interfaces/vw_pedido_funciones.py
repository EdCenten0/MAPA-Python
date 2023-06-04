#Francisco de Jesus Melendez Simplina

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Interfaces import vw_pedido


class pedido_Window(QMainWindow, vw_pedido.Ui_Pedidos):

    def __init__(self, parent=None):
        super(pedido_Window, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = pedido_Window()
    mw.show()
    app.exec()