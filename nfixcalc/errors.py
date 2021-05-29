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
