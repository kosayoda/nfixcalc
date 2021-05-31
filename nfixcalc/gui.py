import sys
from functools import partial
from itertools import cycle

import qdarkstyle
from PySide2.QtWidgets import QApplication, QDesktopWidget, QMainWindow
from PySide2.QtCore import QCoreApplication
from nfixcalc import Mode, calculator, ui
from nfixcalc.buffer import Buffer


class MainApplication(QMainWindow):
    """Main GUI class."""
    def __init__(self) -> None:
        super().__init__()

        self.ui = ui.MainWindow()
        self.ui.setupUi(self)
        self.center()

        self.buffer = Buffer()
        self.result = 0

        self.modes = cycle(Mode)
        self.cycle_mode()

        self.bind_buttons()
        self.update_shortcuts()

    def center(self) -> None:
        """Centers application to screen."""
        frame = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screen_center)
        self.move(frame.topLeft())

    def bind_buttons(self) -> None:
        """Binds buttons to their respective functions."""
        # Numbers, period and operator keys
        for key in self.ui.tokens.buttons():
            key_name = key.text()
            key.clicked.connect(partial(self.buffer.add, key_name))

        # Special function keys
        self.ui.key_sign.clicked.connect(self.buffer.invert_sign)
        self.ui.key_ac.clicked.connect(self.clear)
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

    def update_shortcuts(self) -> None:
        """
        Setup keyboard shortcuts for UI buttons.

        Most regular keybindings are set in QT Designer, however the Extra1 and Extra2
        keys differ based on the current mode, so it is determined here.
        """
        mode_shortcuts = {
            Mode.INFIX: ("(", ")"),
            Mode.POSTFIX: ("End", ""),
            Mode.PREFIX: ("End", ""),
        }
        shortcut_1, shortcut_2 = mode_shortcuts[self.mode]
        self.ui.key_extra1.setShortcut(QCoreApplication.translate("MainWindow", shortcut_1))
        self.ui.key_extra2.setShortcut(QCoreApplication.translate("MainWindow", shortcut_2))

    def update(self) -> None:
        """Updates label and screen."""
        self.ui.info_label.setText(self.buffer.equation_label)

        self.result_len = len(str(self.result))
        self.ui.screen.setDigitCount(max(self.result_len, 5))
        self.ui.screen.display(self.result)

    def cycle_mode(self) -> None:
        """Cycles between the modes Infix, Postfix and Prefix."""
        self.mode = next(self.modes)

        # Update key text
        text_1, text_2 = self.mode.key_text
        self.ui.key_extra1.setText(text_1)
        self.ui.key_extra2.setText(text_2)

        # Update key shortcuts
        self.update_shortcuts()

        self.ui.statusbar.showMessage(f"Mode: {self.mode}")

    def ex_clicked(self, key: int) -> None:
        """Handler for extra buttons."""
        if self.mode is Mode.INFIX:
            self.buffer.add(self.mode.key_text[key])
        else:
            func = {
                0: self.buffer.flush,
                1: lambda: None,
            }
            func[key]()

    def calculate(self, mode: Mode, equation: list[str]) -> float:
        """Solves the current equation."""
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
            self.ui.statusbar.showMessage("Error: Division by zero")
        return self.result

    def clear(self) -> None:
        """Clears the buffer and the screen."""
        self.buffer.clear()
        self.result = 0


def main() -> None:
    """Function to run the GUI calculator."""
    app = QApplication(sys.argv)
    app.setApplicationName("nfixcalculator")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    window = MainApplication()
    window.show()

    sys.exit(app.exec_())
