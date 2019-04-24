import operator
from typing import List

OP_FUNC = {
    "^": operator.pow,
    "%": operator.mod,
    "*": operator.mul,
    "/": operator.truediv,
    "+": operator.add,
    "-": operator.sub,
}

TOKENS = ["^", "%", "*", "/", "+", "-", "(", ")"]
OP_PREC = {"^": 4, "%": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}


def is_number(string: str) -> bool:
    """
    Checks if a given string is a real number

    Args:
        string: The string to be checked

    Returns:
        True if the string is a real number, False otherwise
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def infix_postfix(equation: List[str]) -> List[str]:
    """
    Converts an infix notation equation to postfix notation

    Args:
        equation: An infix notation equation

    Returns:
        A postfix notation equation
    """
    stack = []
    postfix = []

    for token in equation:
        if is_number(token):
            postfix.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            top_token = stack.pop()
            while top_token != "(":
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            while stack and OP_PREC[stack[-1]] >= OP_PREC[token]:
                postfix.append(stack.pop())
            stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix


def postfix_infix(equation: List[str]) -> List[str]:
    """
    Converts a postfix notation equation to infix notation

    Args:
        equation: A postfix notation equation

    Returns:
        A infix notation equation
    """
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
    """
    Converts a prefix notation equation to postfix notation

    Args:
        equation: A prefix notation equation

    Returns:
        A postfix notation equation
    """
    stack = []
    for token in reversed(equation):
        if is_number(token):
            stack.append(token)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(f"{operand_1} {operand_2} {token}")
    return stack.pop().split()


def postfix_prefix(equation: List[str]) -> List[str]:
    """
    Converts a postfix notation equation to prefix notation

    Args:
        equation: A postfix notation equation

    Returns:
        A prefix notation equation
    """
    stack = []
    for token in equation:
        if is_number(token):
            stack.append(token)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(f"{token} {operand_2} {operand_1}")
    return stack.pop().split()
