import sys
from enum import Enum
from functools import partial
from itertools import cycle

import qdarkstyle
from PySide2.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from nfixcalc import calculator
from nfixcalc import ui
from nfixcalc.buffer import Buffer


class Mode(Enum):
    INFIX = 0
    PREFIX = 1
    POSTFIX = 2

    def __str__(self):
        return self.name.title()

    @property
    def key_text(self):
        if self is Mode.INFIX:
            return "(", ")"
        else:
            return "Enter ↑", ""


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ui.MainWindow()
        self.ui.setupUi(self)
        self.center()

        self.buffer = Buffer()
        self.result = 0

        self.modes = cycle(Mode)
        self.cycle_mode()

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
        """
        Binds buttons to their respective functions
        """
        # Numbers, period and operator keys
        for key in self.ui.tokens.buttons():
            key_name = key.text()
            key.clicked.connect(partial(self.buffer.add, key_name))

        # Special function keys
        self.ui.key_sign.clicked.connect(self.buffer.invert_sign)
        self.ui.key_ac.clicked.connect(self.buffer.clear)
        self.ui.key_del.clicked.connect(self.buffer.delete)
        self.ui.key_mode.clicked.connect(self.cycle_mode)
        self.ui.key_solve.clicked.connect(
            lambda: self.calculate(self.mode, self.buffer.equation)
        )
        self.ui.key_extra1.clicked.connect(lambda: self.ex_clicked(0))
        self.ui.key_extra2.clicked.connect(lambda: self.ex_clicked(1))

        # Map each key to the label update function
        layout = self.ui.gridlayout
        for key in (layout.itemAt(i).widget() for i in range(layout.count())):
            key.clicked.connect(self.update)

    def update(self):
        self.ui.info_label.setText(self.buffer.equation_label)
        self.ui.screen.display(self.result)

    def cycle_mode(self):
        self.mode = next(self.modes)

        text_1, text_2 = self.mode.key_text
        self.ui.key_extra1.setText(text_1)
        self.ui.key_extra2.setText(text_2)

        self.ui.statusbar.showMessage(f"Mode: {self.mode}")

    def ex_clicked(self, key):
        if self.mode is Mode.INFIX:
            self.buffer.add(self.mode.key_text[key])
        else:
            func = {
                0: self.buffer.flush,
                1: lambda: None,
            }
            func[key]()

    def calculate(self, mode, equation):
        mode_function = {
            Mode.PREFIX: calculator.calc_prefix,
            Mode.INFIX: calculator.calc_infix,
            Mode.POSTFIX: calculator.calc_postfix,
        }
        try:
            self.result = mode_function[mode](equation)
        except IndexError:
            self.ui.statusbar.showMessage(
                f"Error: Invalid equation for mode {self.mode}"
            )
        except ZeroDivisionError:
            self.ui.statusbar.showMessage(
                f"Error: Division by zero"
            )
        return self.result


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("nfixcalculator")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    window = MainApplication()
    window.show()

    sys.exit(app.exec_())
