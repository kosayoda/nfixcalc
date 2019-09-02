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

OPERATORS = list(OP_FUNC) + ["(", ")"]
OP_PREC = {"^": 4, "%": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}


def is_number(string: str) -> bool:
    """
    Checks if a given string is a real number.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def infix_postfix(equation: List[str]) -> List[str]:
    """
    Converts an infix notation equation to postfix notation.
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
    Converts a postfix notation equation to infix notation.
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
    Converts a prefix notation equation to postfix notation.
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
    Converts a postfix notation equation to prefix notation.
    """
    stack = []
    for token in equation:
        if is_number(token):
            stack.append(token)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(f"{token} {operand_2} {operand_1}")
    return stack.pop().split()


def calc_postfix(equation: List[str]) -> float:
    """
    Evaluates a postfix equation and returns the result.
    """
    stack = []
    for token in equation:
        if is_number(token):
            stack.append(float(token))
        else:
            operand_2, operand_1 = stack.pop(), stack.pop()
            solution = OP_FUNC[token](operand_1, operand_2)
            stack.append(solution)
    return stack.pop()


def calc_infix(equation: List[str]) -> float:
    """
    Evaluates an infix equation and returns the result.
    """
    operator_stack = []
    operand_stack = []

    def process():
        nonlocal operator_stack, operand_stack
        operand_2, operand_1 = operand_stack.pop(), operand_stack.pop()
        operator = operator_stack.pop()
        result = OP_FUNC[operator](operand_1, operand_2)
        operand_stack.append(result)

    for token in equation:
        if is_number(token):
            operand_stack.append(float(token))
        elif token in OP_FUNC:
            if operator_stack and OP_PREC[token] >= OP_PREC[operator_stack[-1]]:
                operator_stack.append(token)
            elif not operator_stack:
                operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack[-1] != "(":
                process()
            operator_stack.pop()
        else:
            process()
    while operator_stack:
        process()
    return operand_stack.pop()


def calc_prefix(equation: List[str]) -> float:
    """
    Evaluates a prefix equation and returns the result.
    """
    stack = []
    for token in reversed(equation):
        if is_number(token):
            stack.append(float(token))
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            solution = OP_FUNC[token](operand_1, operand_2)
            stack.append(solution)
    return stack.pop()
