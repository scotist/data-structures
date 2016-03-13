# _*_ encoding: utf-8 _*_


def proper_paren(text):
    li = [x for x in text if x == '(' or x == ')']
    if li and li[0] == ')':
        return -1
    paren_count = 0
    while li:
        while li and li[0] == '(':
            paren_count += len(li.pop(0))
            while li and li[0] == ')':
                paren_count -= len(li.pop(0))
                if paren_count < 0:
                    return -1
    if paren_count > 0:
        return 1
    return 0
