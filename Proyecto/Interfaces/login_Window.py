

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from Interfaces import vw_Login


class login_Window(QMainWindow, vw_Login.Ui_Login):

    def __init__(self, parent=None):
        super(login_Window, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = login_Window()
    mw.show()
    app.exec()
