# _*_ encoding: utf-8 _*_
"""Make a python graph."""


class Graph(object):
    """Implement a directed graph."""

    def __init__(self):
        """Initiate the graph as an empty dictionary."""
        self.graph = {}

    def nodes(self):
        """Return list of nodes in graph."""
        nodes = []
        for key in self.graph:
            nodes.append(key)
        return nodes

    def edges(self):
        """Return list of edges in graph."""
        return [(), ()]

    def add_node(self, val):
        """Add node to graph."""
        if val in self.graph:
            pass
        else:
            self.graph[val] = []

    def add_edge(self, val, val2):
        """Add edge to graph."""
        if val not in self.graph:
            self.add_node(val)
        if val2 not in self.graph:
            self.add_node(val2)

        if val2 in self.graph[val]:
            pass
        else:
            self.graph[val].append(val2)

    # def delete_node(val):
    #     pass

    # def delete_edge(val, val2):
    #     pass

    # def has_node(val):
    #     if node in graph:
    #         return True
    #     else:
    #         return False

    # def neighbors(val):
    #     for item in edge that is not val:
    #         return item

    # def adjacent(val, val2):
    #     if edge for val and val2:
    #         return True
    #     elif no edge for val and val2:
    #         return False
    #     elif val or val2 not in graph:
    #         raise error
