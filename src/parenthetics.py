# _*_ encoding: utf-8 _*_
"""Function to check if sets of parentheses in string are well-formed."""


def evaluate_parens(sample):
    """Check whether sets of parentheses in string are well-formed."""
    open_check = 0
    closed_check = 0

    for item in sample:
        if item == '(':
            open_check += 1
        elif item == ')':
            closed_check += 1
        if closed_check > open_check:
            return -1

    if closed_check == open_check:
        return 0
    else:
        return 1
