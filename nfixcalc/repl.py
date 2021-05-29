import cmd
import re
import sys
from typing import List

from nfixcalc import Mode
from nfixcalc.calculator import OPERATORS, calc_infix, calc_postfix, calc_prefix


class InvalidEquationError(Exception):
    """Exception class for an error when solving an equation."""
    def __init__(self, mode, message) -> None:
        self.mode = mode
        self.message = message

    def __str__(self) -> str:
        return f"Invalid Equation for mode {self.mode}: {self.message}"


class InvalidVariableError(Exception):
    """Exception class for an invalid variable."""
    def __init__(self, variable) -> None:
        self.variable = variable

    def __str__(self) -> str:
        return f"Invalid Variable: {self.variable}"


class Repl(cmd.Cmd):
    """A class for Read-Evaluate-Print-Loop equation solving functionality."""
    intro = "Welcome to nfixcalc, eternally version 0.1.0\n"
    prompt = "[ Infix ] "
    ruler = ""
    doc_header = (
        "== Help ==\n"
        "Usage:\n"
        "    1. Make sure the correct mode is selected, see: help mode\n"
        "    2. Enter an equation to be evaluated.\n"
        "    3. Optional: Assign result of an equation to a single letter variable.\n"
        "                 Variables can be used in expressions but are not saved upon exit.\n"
        "                 Allowed variables: a-z, A-Z\n"
        "Available Operators:\n"
        f"    {' '.join(OPERATORS)}\n"
        "Example:\n"
        "    [ Infix ] a = ( 5 + 6 ) * 4\n"
        "    44.0\n"
        "    [ Infix ] b = 5 / 2\n"
        "    2.5\n"
        "    [ Infix ] a = a + b\n"
        "    46.5\n\n"
        "== Available Commands =="
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mode = Mode.INFIX
        Repl.echo_info(self.mode)

        self.variables = {}
        self.EQUATION_RE = re.compile(
            # TODO: Dynamic equation regex depending on available operators
            r"\d+(?:\.\d+)?|[+\-*^()]|[\/]{1,2}|[A-z]+"
        )

    def default(self, line) -> None:
        """
        The default action when no command is given.

        Solves the input line as if a regular equation.
        Exits if the `cmdloop` passes "EOF".
        """
        if line == "EOF":
            self.do_exit()

        try:
            result = self.calculate(line.strip())
        except (InvalidEquationError, InvalidVariableError) as error:
            self.display(error)
        else:
            self.display(result)

    def do_mode(self, mode: str) -> None:
        """Switch modes based on input."""
        if not mode:
            self.display(f"-- Current mode: {self.mode} --")
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
            self.display("Invalid mode! Modes: Infix, Postfix, Prefix")
        else:
            self.display(f"-- Current mode: {self.mode} --")

    def help_mode(self) -> None:
        """Help command for the `mode` command."""
        help_string = (
            "\n-- Help: mode --\n"
            "Switches the mode of the calculator.\n"
            "Available modes: Infix, Postfix, Prefix\n"
        )
        self.display(help_string)

    def calculate(self, tokens: str) -> float:
        """
        Solves an equation based on the current mode.

        If the equation contains an assignment to a valid variable,
        saves the result of the equation to that variable.

        Raises InvalidEquationError if there was an error parsing the equation.
        """
        modes = {
            Mode.INFIX: calc_infix,
            Mode.POSTFIX: calc_postfix,
            Mode.PREFIX: calc_prefix,
        }
        try:
            variable, eq, tokens = tokens.rpartition("=")
            variable = variable.strip()
            token_list = self.filter_variables(tokens)

            result = modes[self.mode](token_list)

            # `=` present but no variable is given on the left
            if eq and not variable:
                raise InvalidVariableError(variable)
            # Valid variables: a-z, A-Z
            elif variable.isalpha():
                # Only single-letter variables
                if len(variable) != 1:
                    raise InvalidVariableError(variable)
                self.variables[variable] = str(result)
            return result
        except InvalidVariableError:
            raise
        except Exception:
            raise InvalidEquationError(self.mode, " ".join(tokens))

    # The catch-all args is because I have no idea what keeps passing a positional argument
    def do_clear(self, *_) -> None:
        """Clears any variables present in the session."""
        self.variables = {}
        self.display("-- Variables cleared --")

    def help_clear(self) -> None:
        """Help command for the `clear` command."""
        help_string = (
            "\n-- Help: clear --\n"
            "Clears any variables in the session. Note: There is no confirmation\n"
        )
        self.display(help_string)

    # The catch-all args is because I have no idea what keeps passing a positional argument
    def do_exit(self, *_) -> None:
        """Exits the application cleanly."""
        self.display("\nThanks for using nfixcalc!")
        sys.exit(0)

    def help_exit(self) -> None:
        """Help command for the `exit` command."""
        help_string = (
            "\n-- Help: exit --\n"
            "Exits the calculator.\n"
        )
        self.display(help_string)

    @staticmethod
    def echo_info(mode: Mode) -> None:
        """"Echoes the current mode and available operators to the screen"""
        Repl.display(f"Help: help | Current mode: {mode} | Available operators: {' '.join(OPERATORS)}")

    @staticmethod
    def display(*args, **kwargs) -> None:
        """Display the given text on the screen."""
        print(*args, **kwargs)

    def filter_variables(self, tokens: str) -> List[str]:
        """
        Replaces any variables a-Z in the string with the stored value.

        Returns the token itself otherwise.
        """
        return [
            self.variables.get(token, token)
            if token.isalpha() else token
            for token in self.EQUATION_RE.findall(tokens)
        ]


def main() -> None:
    """Function to run the REPL calculator."""
    try:
        repl = Repl()
        repl.cmdloop()
    except KeyboardInterrupt:
        repl.do_exit()
