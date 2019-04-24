from nfixcalc.calculator import infix_postfix, postfix_infix

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
