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
        return [(key, item) for key in self.graph for item in self.graph[key]]

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

    def has_node(self, val):
        if val in self.nodes():
            return True
        return False

    def delete_node(self, val):
        present = False
        for key in self.graph:
            if key is val:
                del self.graph[key]
                present = True
                break
        if not present:
            raise IndexError("Already not in graph")
        for key in self.graph:
            if val in self.graph[key]:
                self.graph[key].remove(val)

    def delete_edge(self, val, val2):
        if self.has_node(val):
            if val2 in self.graph[val]:
                self.graph[val].remove(val2)
                return
            raise IndexError("No such edge")
        raise IndexError("Your first value is not present in the graph.")

    def neighbors(self, val):
        neighbors = []
        if val not in self.graph:
            raise IndexError("not in graph")
        for key in self.graph:
            if val in self.graph[key]:
                neighbors.append(key)
        for item in self.graph[val]:
            if item not in neighbors:
                neighbors.append(item)
        return neighbors


    def adjacent(self, val, val2):
        if val not in self.graph or val2 not in self.graph:
            raise IndexError("Value not in graph.")
        edges_list = self.edges()
        if (val, val2) in edges_list or (val2, val) in edges_list:
            return True
        return False
