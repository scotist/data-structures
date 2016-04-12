"""Visualize Binary Search Tree."""

from bst import Bst
from queue import Queue
import graphviz as gv
import webbrowser


bst_graph = gv.Graph(format='svg')
bst_graph.node('A')
bst_graph.node('B')
bst_graph.edge('A', 'B')
bst_graph.render(filename='bst')


def render_viz_fixture(root, filename):
    """Traverse tree with breadth-first traversal."""
    bst_graph = gv.Digraph(format='svg')
    q = Queue()
    q.enqueue(root)
    while q.size() > 0:
        print(q.size())
        tree = q.dequeue()
        if tree.value is not None:
            bst_graph.node(str(tree.value))
        if tree.parent is not None:
            bst_graph.edge(str(tree.parent.value), str(tree.value))
        if tree.left_child is not None:
            q.enqueue(tree.left_child)
        if tree.right_child is not None:
            q.enqueue(tree.right_child)
    bst_graph.render(filename=filename)
    webbrowser.open(filename + '.svg')
