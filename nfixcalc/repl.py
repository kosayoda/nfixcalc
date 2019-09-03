import cmd
import sys
from typing import List

from nfixcalc import Mode
from nfixcalc.calculator import OPERATORS, calc_infix, calc_postfix, calc_prefix


class InvalidEquationError(Exception):
    """
    Exception class for an error when solving an equation.
    """
    def __init__(self, mode, message) -> None:
        self.mode = mode
        self.message = message

    def __str__(self) -> str:
        return f"Invalid Equation for mode {self.mode}: {self.message}"


class Repl(cmd.Cmd):
    """
    A class for Read-Evaluate-Print-Loop equation solving functionality.
    """
    intro = "Welcome to nfixcalc, eternally version 0.1.0\n"
    prompt = "[ Infix ] "
    ruler = ""
    doc_header = (
        "== Help ==\n"
        "Usage:\n"
        "    1. Make sure the correct mode is centered, see: help mode\n"
        "    2. Enter an equation to be evaluated. All tokens **must** be space delimited.\n"
        "Available Operators:\n"
        f"    {' '.join(OPERATORS)}\n"
        "Example:\n"
        "    [ Infix ] ( 5 + 6 ) * 4\n\n"
        "== Available Commands =="
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mode = Mode.INFIX
        Repl.echo_info(self.mode)

    def default(self, line) -> None:
        """
        The default action when no command is given.

        Solves the input line as if a regular equation.
        """
        tokens = line.split()
        try:
            result = self.calculate(tokens)
        except InvalidEquationError as error:
            print(error)
        else:
            print(result)

    def do_mode(self, mode: str) -> None:
        """
        Switch modes based on input.
        """
        if not mode:
            print(f"-- Current mode: {self.mode} --")
            return
        modes = {
            "Infix": Mode.INFIX,
            "Postfix": Mode.POSTFIX,
            "Prefix": Mode.PREFIX,
        }
        try:
            self.mode = modes[mode.title()]
            Repl.prompt = f"[{self.mode:^7}] "
        except KeyError:
            print("Invalid mode! Modes: Infix, Postfix, Prefix")
        else:
            print(f"-- Current mode: {self.mode} --")

    def help_mode(self) -> None:
        """
        Help command for the `mode` command.
        """
        help_string = (
            "\n-- Help: mode --\n"
            "Switches the mode of the calculator.\n"
            "Available modes: Infix, Postfix, Prefix\n"
        )
        print(help_string)

    def calculate(self, tokens: List[str]) -> float:
        """
        Solves an equation based on the current mode.

        Raises InvalidEquationError if there was an error parsing the equation.
        """
        modes = {
            Mode.INFIX: calc_infix,
            Mode.POSTFIX: calc_postfix,
            Mode.PREFIX: calc_prefix,
        }
        try:
            return modes[self.mode](tokens)

        except Exception:
            raise InvalidEquationError(self.mode, " ".join(tokens))

    def do_exit(self) -> None:
        """
        Exits the application cleanly.
        """
        print("\nThanks for using nfixcalc!")
        sys.exit(0)

    def help_exit(self) -> None:
        """
        Help command for the `exit` command.
        """
        help_string = (
            "\n-- Help: exit --\n"
            "Exits the calculator.\n"
        )
        print(help_string)

    @staticmethod
    def echo_info(mode: Mode) -> None:
        """
        Echoes the current mode and available operators to the screen.
        """
        print(f"Help: help | Current mode: {mode} | Available operators: {' '.join(OPERATORS)}")


def main() -> None:
    """
    Function to run the REPL calculator.
    """
    try:
        repl = Repl()
        repl.cmdloop()
    except KeyboardInterrupt:
        repl.do_exit()
