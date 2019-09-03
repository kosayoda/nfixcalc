import cmd
from typing import List

from nfixcalc import Mode
from nfixcalc.calculator import calc_infix, calc_postfix, calc_prefix


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
    intro = "Help: help | Current mode: Infix"
    prompt = ">>> "

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mode = Mode.INFIX

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

    def do_mode(self, mode) -> None:
        """
        Switch modes based on input.
        """
        modes = {
            "Infix": Mode.INFIX,
            "Postfix": Mode.POSTFIX,
            "Prefix": Mode.PREFIX,
        }
        try:
            self.mode = modes[mode.title()]
        except KeyError:
            print(f"Invalid mode! Modes: {', '.join(modes.keys())}")
        else:
            print(f"Help: help | Current mode: {self.mode}")

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


def main():
    """
    Function to run the REPL calculator.
    """
    Repl().cmdloop()
