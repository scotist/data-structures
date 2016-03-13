# _*_ encoding: utf-8 _*_
"""Test parenthetics.py."""


def test_evaluate_parens():
    """Test the eval function."""
    from parenthetics import evaluate_parens
    assert evaluate_parens('((()') == 2
