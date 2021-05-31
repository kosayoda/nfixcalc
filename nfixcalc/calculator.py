import operator
from typing import List, Union

from nfixcalc.errors import InvalidEquationError
from nfixcalc import Mode

OP_FUNC = {
    "^": operator.pow,
    "%": operator.mod,
    "*": operator.mul,
    "//": operator.floordiv,
    "/": operator.truediv,
    "+": operator.add,
    "-": operator.sub,
}

OPERATORS = set(OP_FUNC) | {"(", ")"}
OP_PREC = {"^": 4, "%": 4, "*": 3, "/": 3, "//": 3, "+": 2, "-": 2, "(": 1}


def is_number(string: str) -> bool:
    """Checks if a given string is a real number."""
    try:
        float(string)
        return True
    except ValueError:
        return False


def infix_postfix(equation: List[str]) -> List[str]:
    """Converts an infix notation equation to postfix notation."""
    stack = []
    postfix = []

    last_token = ""

    for token in equation:
        if is_number(token):
            if is_number(last_token):
                raise InvalidEquationError(Mode.INFIX, "Found number followed by another number")

            postfix.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            try:
                top_token = stack.pop()
                while top_token != "(":
                    postfix.append(top_token)
                    top_token = stack.pop()
            except IndexError:
                raise InvalidEquationError(Mode.INFIX, f"Imbalanced number of parenthesis")

        elif token in OP_FUNC:
            if last_token in OP_FUNC:
                raise InvalidEquationError(
                    Mode.INFIX, "Found operator followed by another operator"
                )

            while stack and OP_PREC[stack[-1]] >= OP_PREC[token]:
                postfix.append(stack.pop())

            stack.append(token)
        else:
            raise InvalidEquationError(Mode.INFIX, f"Unknown token: {token}")

        last_token = token

    while stack:
        token = stack.pop()
        if token == "(" or token == ")":
            raise InvalidEquationError(Mode.INFIX, f"Imbalanced number of parenthesis")
        postfix.append(token)
    return postfix


def postfix_infix(equation: List[str]) -> List[str]:
    """Converts a postfix notation equation to infix notation."""
    stack = []
    for token in equation:
        if is_number(token):
            stack.append(token)
        else:
            operand_2, operand_1 = stack.pop(), stack.pop()
            stack.append(f"( {operand_1} {token} {operand_2} )")

    result = stack.pop().strip("()")  # Trim outer brackets
    return result.split()


def prefix_postfix(equation: List[str]) -> List[str]:
    """Converts a prefix notation equation to postfix notation."""
    stack = []
    for token in reversed(equation):
        if is_number(token):
            stack.append(token)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(f"{operand_1} {operand_2} {token}")
    return stack.pop().split()


def postfix_prefix(equation: List[str]) -> List[str]:
    """Converts a postfix notation equation to prefix notation."""
    stack = []
    for token in equation:
        if is_number(token):
            stack.append(token)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(f"{token} {operand_2} {operand_1}")
    return stack.pop().split()


def calc_postfix(equation: List[str]) -> Union[float, int]:
    """Evaluates a postfix equation and returns the result."""
    stack = []
    for token in equation:
        if is_number(token):
            stack.append(float(token))
        else:
            operand_2, operand_1 = stack.pop(), stack.pop()
            solution = OP_FUNC[token](operand_1, operand_2)
            stack.append(solution)

    # The equation is invalid if after the calculation, there is still more
    # than one token on the stack
    if len(stack) > 1:
        raise InvalidEquationError(Mode.POSTFIX, f"Found leftover token(s) after stack evaluation")
    else:
        result = stack.pop()

    if result.is_integer():
        return int(result)

    return result


def calc_infix(equation: List[str]) -> float:
    """Evaluates a infix equation and returns the result."""
    postfix = infix_postfix(equation)
    return calc_postfix(postfix)


def calc_prefix(equation: List[str]) -> float:
    """Evaluates a prefix equation and returns the result."""
    stack = []
    for token in reversed(equation):
        if is_number(token):
            stack.append(float(token))
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            solution = OP_FUNC[token](operand_1, operand_2)
            stack.append(solution)

    # The equation is invalid if after the calculation, there is still more
    # than one token on the stack
    if len(stack) > 1:
        raise InvalidEquationError(Mode.PREFIX, f"Found leftover token(s) after stack evaluation")
    else:
        result = stack.pop()

    if result.is_integer():
        return int(result)

    return result
