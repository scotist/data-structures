# _*_ encoding: utf-8 _*_
"""Test parenthetics.py."""
import pytest

TEST_CASES = [(['a'], 0),
              (['()'], 0),
              (['(Hello))'], -1)]


# @pytest.mark.parametrize('li, result', TEST_CASES)
# def test_evaluate_parens(li, result):
#     """Test the eval function."""
#     from parenthetics import evaluate_parens
#     assert evaluate_parens(li) == result

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

def test_evaluate_parens():
    from parenthetics import evaluate_parens
    assert evaluate_parens(')))(((') == -1
