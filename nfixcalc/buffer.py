from typing import List

from nfixcalc.calculator import OPERATORS


class Buffer:
    """
    Buffer class to store and handle tokens in the current equation.

    `equation` is the list of tokens to be evaluated.
    `temp` is a list of characters in an incomplete token.
    """
    def __init__(self) -> None:
        self._equation: List[str] = []
        self.temp: List[str] = []

    def add(self, token: str) -> None:
        """Adds a token to the current equation."""
        # Operators mean that the current number is finished, therefore we can
        # flush the buffer. If not, the next token may still be the subsequent
        # character in a number.
        if token in OPERATORS:
            self.flush()
            self._equation.append(token)
        else:
            self.temp.append(token)

    def delete(self) -> None:
        """Removes the last character in the current equation."""
        # Characters in `temp` can simply be removed.
        # Since `equation` is a list of tokens, we need to get the last entered
        # token to remove the last character.
        if self.temp:
            self.temp.pop()
        elif self._equation:
            val = self._equation.pop()
            if len(val) > 1:
                self.temp.append(val[:-1])

    def flush(self) -> None:
        """Joins the current token in `temp` and adds it to the equation."""
        if self.temp:
            self._equation.append("".join(self.temp))
            self.temp.clear()

    def clear(self) -> None:
        """Clears all buffers in the system."""
        self._equation.clear()
        self.temp.clear()

    def invert_sign(self) -> None:
        """Toggles the sign of the last entered number."""
        if self.temp:
            if self.temp[0] == "-":
                self.temp.pop(0)
            else:
                self.temp.insert(0, "-")
        elif self._equation:
            val = self._equation.pop()
            if val not in OPERATORS:
                if val.startswith("-"):
                    val = val[1:]
                else:
                    val = f"-{val}"
            self._equation.append(val)

    @property
    def equation(self) -> List[str]:
        """Flushes the temporary buffer and returns the final equation."""
        self.flush()
        return self._equation

    @property
    def equation_label(self) -> str:
        """Returns current equation and buffer equation in a readable form."""
        display = ""
        if self._equation:
            display += f"{' '.join(self._equation)} "
        if self.temp:
            display += f"{''.join(self.temp)}"
        return display
