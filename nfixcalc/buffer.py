from typing import List

from nfixcalc.calculator import OPERATORS


class Buffer:
    def __init__(self):
        self.equation: List[str] = []
        self.temp_val: List[str] = []

    def add(self, token: str):
        print(f"{token} pressed!")
        if token in OPERATORS:
            self.flush()
            self.equation.append(token)
        else:
            self.temp_val.append(token)

    def delete(self):
        if self.temp_val:
            self.temp_val.pop()
        elif self.equation:
            val = self.equation.pop()
            if len(val) > 1:
                self.temp_val.append(val[:-1])

    def flush(self):
        if self.temp_val:
            self.equation.append("".join(self.temp_val))
            self.temp_val.clear()

    def clear(self):
        self.equation.clear()
        self.temp_val.clear()

    def invert_digit(self):
        if self.temp_val:
            if self.temp_val[0] == "-":
                self.temp_val.pop()
            else:
                self.temp_val.insert(0, "-")
        elif self.equation:
            val = self.equation.pop()
            if val not in OPERATORS:
                if val.startswith("-"):
                    val = val[1:]
                else:
                    val = f"-{val}"
            self.equation.append(val)
