import pytest

cases = [('(', 1),
         ('(())', 0),
         ('b(r)o(k)e)n(', -1),
         ('()()((()()()()))', 0),
         ('(()', 1),
         ('))(()))', -1),
         ('Test()', 0),
         ('30()())', -1),
         ('( a, 3j2 ()', 1),
         ('No Parens Here!', 0),
         ('', 0)]


@pytest.mark.parametrize('st, result', cases)
def test_proper_paren(st, result):
    from paren_aj import proper_paren
    assert proper_paren(st) == result
