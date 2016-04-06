# _*_ encoding: utf-8 _*_
"""Binary Search Tree Implementation."""


class Node(object):
    """Make node for binary search tree."""

    def __init__(self, value, parent=None, left_child=None, right_child=None):
        """Init function."""
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    @property
    def left_child(self):
        """Left child."""
        return self._left_child

    @left_child.setter
    def left_child(self, other_node):
        self._left_child = other_node
        other_node.parent = self

    @property
    def right_child(self):
        """Right child."""
        return self._right_child

    @right_child.setter
    def right_child(self, other_node):
        self._right_child = other_node
        other_node.parent = self
