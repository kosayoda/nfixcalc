import pytest
from nfixcalc.calculator import (
    infix_postfix, postfix_infix,
    prefix_postfix, postfix_prefix,
    calc_postfix, calc_infix
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

results = [
    6.3333333333,
    78.0879120879,
    3,
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


def test_calc_postfix():
    for postfix, result in zip(postfixes, results):
        assert calc_postfix(postfix.split()) == pytest.approx(result)


def test_calc_infix():
    for infix, result in zip(infixes, results):
        assert calc_infix(infix.split()) == pytest.approx(result)
