# _*_ encoding: utf-8 _*_
"""Test graph.py."""
import pytest


@pytest.fixture()
def my_graph():
    """Fixture for graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node("monkeybutler")
    new_graph.add_node("penguinbutler")
    return new_graph


@pytest.fixture()
def full_graph():
    """Fixture that makes a full graph."""
    from graph import Graph
    full_graph = Graph()
    full_graph.add_edge("a", "b")
    full_graph.add_edge("c", "d")
    full_graph.add_edge("c", "b")
    full_graph.add_edge("a", "d")
    full_graph.add_edge("b", "d")
    full_graph.add_edge("d", "a")
    return full_graph


@pytest.fixture()
def deep_cyclic_graph():
    """Fixture that makes a deeper graph."""
    from graph import Graph
    full_graph = Graph()
    # full_graph.graph = {'A': ['B', 'C'], 'B': ['D', 'E'],
    #                     'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
    full_graph.graph = {'A': {'B': 0, 'C': 0}, 'B': {'D': 0, 'E': 0},
                        'C': {'D': 0, 'E': 0}, 'D': {'E': 0}, 'E': {'A': 0}}
    return full_graph


def test_init(my_graph):
    """Test init function."""
    from graph import Graph
    assert isinstance(my_graph, Graph)


def test_add_node(my_graph):
    """Test add_node function."""
    assert "penguinbutler" in my_graph.nodes()


def test_nodes(my_graph):
    """Test nodes function."""
    assert "monkeybutler" in my_graph.nodes()
    assert "penguinbutler" in my_graph.nodes()


def test_add_edge():
    """Test add_edge function for nodes in empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_edge("monkeybutler", "penguinbutler")
    assert new_graph.graph["monkeybutler"] == {"penguinbutler": 0}
    assert new_graph.graph["penguinbutler"] == {}


def test_edges(full_graph):
    """Test edges function."""
    print(full_graph.graph)
    assert sorted(full_graph.edges()) == [{('a', 'b'): 0}, {('a', 'd'): 0},
                                          {('b', 'd'): 0}, {('c', 'b'): 0},
                                          {('c', 'd'): 0}, {('d', 'a'): 0}]


def test_has_node(full_graph):
    """Test has_node function."""
    assert full_graph.has_node("a") is True
    assert full_graph.has_node("z") is False
    assert full_graph.has_node("") is False


def test_delete_node(full_graph):
    """Test delete function."""
    full_graph.delete_node("a")
    assert full_graph.graph == {'d': {}, 'c': {'d': 0, 'b': 0}, 'b': {'d': 0}}


def test_delete_node_0(full_graph):
    """Test delete function when no value is passed in.."""
    with pytest.raises(IndexError):
        full_graph.delete_node("")


def test_delete_node_1():
    """Test delete function when no value is passed in.."""
    from graph import Graph
    empty_graph = Graph()
    with pytest.raises(IndexError):
        empty_graph.delete_node('a')


# def test_delete_edge(full_graph):
#     """Test delete edge function."""
#     full_graph.delete_edge('d', 'a')
#     assert sorted(full_graph.edges()) == [('a', 'b'), ('a', 'd'),
#                                           ('b', 'd'), ('c', 'b'),
#                                           ('c', 'd')]


def test_neighbors(full_graph):
    """Test neighbors function."""
    assert sorted(full_graph.neighbors('b')) == ['a', 'c', 'd']


def test_neighbors_1(full_graph):
    """Test neighbors function."""
    with pytest.raises(IndexError):
        full_graph.neighbors('z')


def test_adjacent(full_graph):
    """Test adjacent function with bad values."""
    with pytest.raises(IndexError):
        full_graph.adjacent('y', 'z')


def test_adjacent_0(full_graph):
    """Test adjacent function with good values."""
    assert full_graph.adjacent('a', 'b')


def test_adjacent_1(full_graph):
    """Test adjacent function with good values."""
    assert not full_graph.adjacent('a', 'c')


def test_depth_traversal(deep_cyclic_graph):
    """Test depth-first traversal method on a cyclic graph."""
    assert deep_cyclic_graph.depth_traversal('A') in [['A', 'B', 'D', 'E', 'C'],
                                                      ['A', 'C', 'D', 'E', 'B'],
                                                      ['A', 'C', 'E', 'D', 'B'],
                                                      ['A', 'B', 'E', 'D', 'C']]


def test_depth_traversal_01(my_graph):
    """Test depth-first traversal method on a non-cyclic graph."""
    my_graph.add_edge("monkeybutler", "penguinbutler")
    assert my_graph.depth_traversal('monkeybutler') == ['monkeybutler',
                                                        'penguinbutler']


def test_depth_traversal_02():
    """Test depth-first traversal method on an empty graph."""
    from graph import Graph
    empty_graph = Graph()
    assert empty_graph.depth_traversal('A') == []
    assert empty_graph.depth_traversal('') == []


def test_breadth_traversal(deep_cyclic_graph):
    """Test breadth-first traversal method on a cyclic graph."""
    assert deep_cyclic_graph.breadth_traversal('A') in [['A', 'B', 'C', 'D', 'E'],
                                                        ['A', 'B', 'C', 'D', 'E'],
                                                        ['A', 'C', 'B', 'D', 'E'],
                                                        ['A', 'C', 'B', 'E', 'D']]


def test_breadth_traversal_01(my_graph):
    """Test breadth-first traversal method on a non-cyclic graph."""
    my_graph.add_edge("monkeybutler", "penguinbutler")
    assert my_graph.breadth_traversal('monkeybutler') == ['monkeybutler',
                                                          'penguinbutler']


def test_breadth_traversal_02():
    """Test depth-first traversal method on an empty graph."""
    from graph import Graph
    empty_graph = Graph()
    assert empty_graph.breadth_traversal('A') == []
    assert empty_graph.breadth_traversal('') == []
