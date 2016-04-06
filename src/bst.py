# _*_ encoding: utf-8 _*_
"""Binary Search Tree Implementation."""

# class Node(object):
#     """Make node for binary search tree."""

#     def __init__(self, value, parent=None, left_child=None, right_child=None):
#         """Init function."""
#         self.value = value
#         self.parent = parent
#         self.left_child = left_child
#         self.right_child = right_child

#     @property
#     def left_child(self):
#         """Left child."""
#         return self._left_child

#     @left_child.setter
#     def left_child(self, other_node):
#         self._left_child = other_node
#         other_node.parent = self

#     @property
#     def right_child(self):
#         """Right child."""
#         return self._right_child

#     @right_child.setter
#     def right_child(self, other_node):
#         self._right_child = other_node
#         other_node.parent = self


class Bst(object):
    """Implement Binary Search Tree."""

    def __init__(self, value=None, parent=None, left_child=None, right_child=None):
        """Init Tree."""
        self.value = value
        self._list = set()
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
        if other_node is not None:
            other_node.parent = self

    @property
    def right_child(self):
        """Right child."""
        return self._right_child

    @right_child.setter
    def right_child(self, other_node):
        self._right_child = other_node
        if other_node is not None:
            other_node.parent = self

    def insert(self, value):
        """Insert value into tree if not present."""
        if value in self._list:
            return value
        self._list.append(value)
        if self.value is None:
            self.value = value
        if value > self.value:
            if not self.right_child:
                self.right_child = Bst(parent=self, value=value)
            else:
                self.right_child.insert(value)
        elif value < self.value:
            if not self.left_child:
                self.left_child = Bst(parent=self, value=value)
            else:
                self.left_child.insert(value)

    def contains(self, value):
        """Return True if value in tree."""
        return value in self._list

    def size(self):
        """Return size of tree."""
        return len(self._list)

    def depth(self):
        """Return number of levels in the tree."""
        if not self.left_child and not self.right_child:
            return 1
        depths = [child.depth()
                  for child in (self.left_child, self.right_child)
                  if child is not None]
        return max(depths) + 1

    def balance(self):
        """Return number expressing balance or lack thereof of tree."""
        return self.left_child.depth() - self.right_child.depth()
