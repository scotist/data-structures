# _*_ encoding: utf-8 _*_
"""Function to check if sets of parentheses in string are well-formed."""
# from stack import Stack

# test_stack = Stack()

# from collections import deque
# test_stack = deque()


def evaluate_parens(sample):
    """Check whether sets of parentheses in string are well-formed."""
    parens = []
    open_check = 0
    closed_check = 0
    balanced = True

    for c in reversed(sample):
        if c is '(':
            parens.append(c)
        elif c is ')':
            parens.append(c)

    for item in parens:
        if item == '(':
            open_check += 1
        elif item == ')':
            closed_check += 1

    if open_check > closed_check:
        return 1
    elif closed_check > open_check:
        return -1
    elif closed_check == open_check:
        return 0

    # for p in parens:
    #     test_stack.push(p)

    # for p in parens:
    #     test_stack.append(p)

    # for item in test_stack:
    #     if test_stack.pop() == '(':
    #         counter += 1
    #     elif test_stack.pop() == ')':
    #         counter -= 1
    #     elif IndexError:
    #         break

  # while True:
  #     try:
      #     if test_stack.pop() == '(':
      #         counter += 1
      #     elif test_stack.pop() == ')':
      #         counter -= 1
      # except IndexError:
      #     break

    return counter


    # split string
    # filter out everything but parens
    # make counter
    # push parens into stack
