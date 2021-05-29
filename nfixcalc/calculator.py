import operator
from typing import List, Union

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
            # One number after another is invalid infix
            if is_number(last_token):
                raise ValueError

            postfix.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            top_token = stack.pop()
            while top_token != "(":
                postfix.append(top_token)
                top_token = stack.pop()

        elif token in OP_FUNC:
            # One operator after another is invalid infix
            if last_token in OP_FUNC:
                raise ValueError

            while stack and OP_PREC[stack[-1]] >= OP_PREC[token]:
                postfix.append(stack.pop())

            stack.append(token)
        else:
            raise ValueError

        last_token = token

    while stack:
        token = stack.pop()
        if token == "(" or token == ")":
            raise ValueError
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
        raise ValueError
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
        raise ValueError
    else:
        result = stack.pop()

    if result.is_integer():
        return int(result)

    return result
