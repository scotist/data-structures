# _*_ encoding: utf-8 _*_
"""Test parenthetics.py."""


def test_evaluate_parens_0():
    """Test first case."""
    from parenthetics import evaluate_parens
    assert evaluate_parens('') == 0


def test_evaluate_parens_01():
    """Test second case."""
    from parenthetics import evaluate_parens
    assert evaluate_parens('()') == 0


def test_evaluate_parens_02():
    """Test third case."""
    from parenthetics import evaluate_parens
    assert evaluate_parens('(Hello))') == -1


def test_evaluate_parens_03():
    """Test fourth case."""
    from parenthetics import evaluate_parens
    assert evaluate_parens('((Hello)') == 1


def test_evaluate_parens_04():
    """Final test case."""
    from parenthetics import evaluate_parens
    assert evaluate_parens(')))(((') == -1
