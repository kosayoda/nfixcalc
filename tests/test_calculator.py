from nfixcalc.calculator import (
    infix_postfix, postfix_infix,
    prefix_postfix, postfix_prefix,
)

prefixes = [
    "+ 3 / * 4 5 6",
    "/ * + 300 23 - 43 21 + 84 7",
    "/ * + 4 8 - 6 5 * - 3 2 + 2 2"
]
infixes = [
    "3 + ( ( 4 * 5 ) / 6 )",
    "( ( 300 + 23 ) * ( 43 - 21 ) ) / ( 84 + 7 )",
    "( ( 4 + 8 ) * ( 6 - 5 ) ) / ( ( 3 - 2 ) * ( 2 + 2 ) )",
]
postfixes = [
    "3 4 5 * 6 / +",
    "300 23 + 43 21 - * 84 7 + /",
    "4 8 + 6 5 - * 3 2 - 2 2 + * /",
]


def test_infix_postfix():
    for infix, postfix in zip(infixes, postfixes):
        assert infix_postfix(infix.split()) == postfix.split()


def test_postfix_infix():
    for postfix, infix in zip(postfixes, infixes):
        assert postfix_infix(postfix.split()) == infix.split()


def test_prefix_postfix():
    for prefix, postfix in zip(prefixes, postfixes):
        assert prefix_postfix(prefix.split()) == postfix.split()


def test_postfix_prefix():
    for postfix, prefix in zip(postfixes, prefixes):
        assert postfix_prefix(postfix.split()) == prefix.split()
