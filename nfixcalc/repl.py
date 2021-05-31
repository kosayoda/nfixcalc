import inspect
import re
import sys

from prompt_toolkit import PromptSession
from prompt_toolkit import print_formatted_text

from nfixcalc import Mode
from nfixcalc.calculator import OPERATORS, calc_infix, calc_postfix, calc_prefix
from nfixcalc.errors import InvalidEquationError, InvalidVariableError


class Repl:
    """A class for Read-Evaluate-Print-Loop equation solving functionality."""

    INFO = "Help: help | Current mode: {mode} | Available operators: {operators}"
    INTRO = "Welcome to nfixcalc, eternally version 0.1.0\n"
    HELP_MESSAGE = (
        "== Help ==\n"
        "Usage:\n"
        "    1. Make sure the correct mode is selected, see: help mode\n"
        "    2. Enter an equation to be evaluated.\n"
        "    3. Optional: Assign result of an equation to a single letter variable.\n"
        "                 Variables can be used in expressions but are not saved upon exit.\n"
        "                 Allowed variables: a-z, A-Z\n"
        "Available Operators:\n"
        "    {operators}\n"
        "Example:\n"
        "    [ Infix ] a = ( 5 + 6 ) * 4\n"
        "    44.0\n"
        "    [ Infix ] b = 5 / 2\n"
        "    2.5\n"
        "    [ Infix ] a = a + b\n"
        "    46.5\n\n"
        "== Available Commands ==\n"
        "   {commands}"
    )

    def __init__(self, *args, **kwargs) -> None:
        self.mode = Mode.INFIX
        self.variables = {}
        self.EQUATION_RE = re.compile(
            # TODO: Dynamic equation regex depending on available operators
            r"\d+(?:\.\d+)?|[+\-*^()]|[\/]{1,2}|[A-z]+"
        )

        self.session = PromptSession()

        Repl.display(Repl.INFO.format(mode=self.mode, operators=' '.join(OPERATORS)))

    def cmdloop(self):
        """The actual REPL."""
        while True:
            try:
                line = self.session.prompt(message=self.mode_string)
            except EOFError:
                Repl.exit()
            else:
                result = self.parse_cmd(line)

                if result is not None:
                    Repl.display(result)

    def parse_cmd(self, line: str) -> str:
        """
        Parse a given line of input into a command.

        Uses the same getattr black magic as the python `cmd` library.
        """
        line = line.strip()
        if not line:
            return "\n"

        command, sep, argument = line.partition(" ")
        if command == line and sep == "" and argument == "":  # Separator not found
            self.calculate(line)

        try:
            command_func = getattr(self, f"do_{command}")
        except AttributeError:
            return self.calculate(line)
        else:
            return command_func(argument)

    def do_help(self, command: str) -> str:
        """Returns the help string for a given command, or for the program."""
        if not command:
            return self.help_string

        # Let's do more black magickery and get the help message for a command
        # from the command function's docstring.
        try:
            command_func = getattr(self, f"do_{command}")
        except AttributeError:
            return f"Unknown command: {command}"
        else:
            if (documentation := inspect.getdoc(command_func)) is None:
                return f"Sorry, no help found for command: {command}"
            else:
                return f"-- Help: {command} --\n{documentation}"

    def do_mode(self, mode: str) -> None:
        """
        Switches the mode of the calculator.
        Available modes: Infix, Postfix, Prefix
        """
        if not mode:
            Repl.display(f"-- Current mode: {self.mode} --")
            return

        modes = {
            "Infix": Mode.INFIX,
            "Postfix": Mode.POSTFIX,
            "Prefix": Mode.PREFIX,
        }
        try:
            self.mode = modes[mode.title()]
        except KeyError:
            self.display("Invalid mode! Modes: Infix, Postfix, Prefix")
        else:
            self.display(f"-- Current mode: {self.mode} --")

    def do_clear(self, *_) -> None:
        """Clears any variables present in the session."""
        self.variables = {}
        Repl.display("-- Variables cleared --")

    def do_exit(self, *_) -> None:
        """Exits the application cleanly."""
        Repl.display("\nThanks for using nfixcalc!")
        sys.exit(0)

    def calculate(self, line: str) -> str:
        try:
            result = self._calculate(line)
        except (InvalidEquationError, InvalidVariableError) as error:
            return str(error)
        else:
            return str(result)

    def _calculate(self, tokens: str) -> float:
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
        except (InvalidVariableError, InvalidEquationError) as e:
            raise e
        except Exception:
            raise InvalidEquationError(self.mode, tokens)

    def filter_variables(self, tokens: str) -> list[str]:
        """
        Replaces any variables a-Z in the string with the stored value.

        Returns the token itself otherwise.
        """
        return [
            self.variables.get(token, token)
            if token.isalpha() else token
            for token in self.EQUATION_RE.findall(tokens)
        ]

    @property
    def help_string(self) -> str:
        cmd_list = [
            func[3:] for func in dir(Repl) if func.startswith("do_")
        ]
        return Repl.HELP_MESSAGE.format(
            operators=" ".join(OPERATORS), commands="  ".join(cmd_list)
        )

    @property
    def mode_string(self) -> str:
        """Returns the current mode is a nice representation for the prompt."""
        return f"[{self.mode:^7}] "

    @staticmethod
    def exit() -> None:
        """Exits the REPL."""
        Repl.display("Thanks for using nfixcalc!")
        sys.exit(0)

    @staticmethod
    def display(text: str) -> None:
        """Displays the given text onto the screen."""
        print_formatted_text(text)


def main() -> None:
    """Function to run the REPL calculator."""
    repl = Repl()
    try:
        repl.cmdloop()
    except KeyboardInterrupt:
        repl.exit()
