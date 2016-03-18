# _*_ encoding: utf-8 _*_
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
    print(full_graph.graph)
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
    assert new_graph.graph["monkeybutler"] == ["penguinbutler"]
    assert new_graph.graph["penguinbutler"] == []


def test_edges(full_graph):
    """Test edges function."""
    assert sorted(full_graph.edges()) == [('a', 'b'), ('a', 'd'),
                                          ('b', 'd'), ('c', 'b'),
                                          ('c', 'd'), ('d', 'a')]


def test_has_node(full_graph):
    """Test has_node function."""
    assert full_graph.has_node("a") is True
    assert full_graph.has_node("z") is False
    assert full_graph.has_node("") is False


def test_delete_node(full_graph):
    """Test delete function."""
    full_graph.delete_node("a")
    assert full_graph.graph == {'d': [], 'c': ['d', 'b'], 'b': ['d']}


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


def test_delete_edge(full_graph):
    """Test delete edge function."""
    full_graph.delete_edge('d', 'a')
    assert sorted(full_graph.edges()) == [('a', 'b'), ('a', 'd'),
                                          ('b', 'd'), ('c', 'b'),
                                          ('c', 'd')]
