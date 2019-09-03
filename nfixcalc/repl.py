import cmd

from nfixcalc import Mode
from nfixcalc.calculator import calc_infix, calc_postfix, calc_prefix


class InvalidEquationError(Exception):
    def __init__(self, mode, message):
        self.mode = mode
        self.message = message

    def __str__(self):
        return f"Invalid Equation for mode {self.mode}: {self.message}"


class Repl(cmd.Cmd):
    intro = "Help: help | Current mode: Infix"
    prompt = ">>> "

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = Mode.INFIX

    def default(self, line):
        tokens = line.split()
        try:
            result = self.calculate(tokens)
        except InvalidEquationError as error:
            print(error)
        else:
            print(result)

    def do_mode(self, mode):
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

    def calculate(self, tokens):
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
    Repl().cmdloop()


if __name__ == "__main__":
    main()
