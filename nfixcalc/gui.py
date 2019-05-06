import functools
import sys

import qdarkstyle
from PySide2.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from nfixcalc import ui
from nfixcalc.buffer import Buffer


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.MainWindow()
        self.ui.setupUi(self)
        self.center()

        self.buffer = Buffer()

        self.bind_buttons()

    def center(self):
        """
        Centers application to screen.
        """
        frame = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screen_center)
        self.move(frame.topLeft())

    def bind_buttons(self):
        for key in self.ui.tokens.buttons():
            key_name = key.text()
            key.clicked.connect(
                functools.partial(self.buffer.add, key_name)
            )


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("nfixcalculator")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    window = MainApplication()
    window.show()

    sys.exit(app.exec_())
