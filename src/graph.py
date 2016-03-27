# _*_ encoding: utf-8 _*_
"""Make a python graph."""
from stack import Stack
from queue import Queue
from itertools import count
import heapq

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
        return [{(key1, key2): self.graph[key1][key2]} for key1 in self.graph for key2 in self.graph[key1]]

    def add_node(self, val):
        """Add node to graph."""
        if val in self.graph:
            pass
        else:
            self.graph[val] = {}

    def add_edge(self, val, val2, weight=0):
        """Add edge to graph."""
        if val not in self.graph:
            self.add_node(val)
        if val2 not in self.graph:
            self.add_node(val2)

        if val2 in self.graph[val]:
            pass
        else:
            self.graph[val][val2] = weight

    def has_node(self, val):
        """Check to see a given value is a node in the graph."""
        if val in self.nodes():
            return True
        return False

    def delete_node(self, val):
        """Delete a node from the graph."""
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
                del self.graph[key][val]

    def delete_edge(self, val, val2):
        """Delete an edge from the graph."""
        if self.has_node(val):
            if val2 in self.graph[val]:
                del self.graph[val][val2]
                return
            raise IndexError("No such edge")
        raise IndexError("Your first value is not present in the graph.")

    def neighbors(self, val):
        """Return all the neighbors of given value."""
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
        """Check whether one value is connected to another by an edge."""
        if val not in self.graph or val2 not in self.graph:
            raise IndexError("Value not in graph.")
        edges_list = self.edges()
        for edge in edges_list:
            try:
                if edge[(val, val2)] is not None or edge[(val2, val)] is not None:
                    return True
            except KeyError:
                pass
        return False

    def breadth_traversal(self, start):
        """Breadth-first traversal of our graph."""
        path = []
        breadth_queue = Queue()
        breadth_queue.enqueue(start)
        try:
            while start in self.graph:
                current = breadth_queue.dequeue()
                if current not in path:
                    path = path + [current]
                    for node in self.graph[current]:
                        breadth_queue.enqueue(node)
            return path
        except (IndexError, KeyError):
            return path

    def depth_traversal(self, start):
        """Depth-first traversal of our graph."""
        path = []
        depth_stack = Stack()
        depth_stack.push(start)
        try:
            while start in self.graph:
                current = depth_stack.pop()
                if current not in path:
                    path = path + [current]
                    for node in self.graph[current]:
                        depth_stack.push(node)
            return path
        except (IndexError, KeyError):
            return path

    def dijkstra(self, start, end):
            unique = count()
            visited = []
            heap = [(0, unique, start, [start])]
            while heap:
                weight, secondary_num, node, path = heapq.heappop(heap)
                if node == end:
                    return path[::-1], weight
                if node not in visited:
                    visited.append(node)
                    for neighbor, next_weight in self.graph[node].items():
                        heapq.heappush(heap, (weight + next_weight,
                                              next(unique),
                                              neighbor,
                                              [neighbor] + path))

if __name__ == '__main__':
    from test_graph import my_graph, deep_cyclic_graph
    print('Given the following cyclic graph:')
    print(deep_cyclic_graph().graph)
    print('The depth traversal will appear as follows:')
    print(deep_cyclic_graph().depth_traversal('A'))
    print('The breadth traversal will appear as follows:')
    print(deep_cyclic_graph().breadth_traversal('A'))
    print('On the other hand, given this short non-cyclic graph:')
    this_graph = my_graph()
    this_graph.add_edge("monkeybutler", "penguinbutler")
    this_graph.add_edge("penguinbutler", "koalabutler")
    this_graph.add_edge("monkeybutler", "platypusbutler")
    print(this_graph.graph)
    print('The depth traversal will appear as follows:')
    print(this_graph.depth_traversal('monkeybutler'))
    print('The breadth traversal will appear as follows:')
    print(this_graph.breadth_traversal('monkeybutler'))
