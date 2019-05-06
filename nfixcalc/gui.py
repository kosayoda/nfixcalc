import sys

import qdarkstyle
from PySide2.QtWidgets import QApplication, QMainWindow

from nfixcalc import ui


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.MainWindow()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("nfixcalculator")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    window = MainApplication()
    window.show()

    sys.exit(app.exec_())
