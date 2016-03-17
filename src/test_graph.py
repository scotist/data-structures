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


def test_init():
    """Test init function."""
    from graph import Graph
    new_graph = my_graph()
    assert isinstance(new_graph, Graph)


def test_add_node():
    """Test add_node function."""
    assert "penguinbutler" in my_graph().nodes()


def test_nodes():
    """Test nodes function."""
    assert "monkeybutler" in my_graph().nodes()
    assert "penguinbutler" in my_graph().nodes()


def test_add_edge():
    """Test add_edge function for nodes in empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_edge("monkeybutler", "penguinbutler")
    assert new_graph.graph["monkeybutler"] == ["penguinbutler"]
    assert new_graph.graph["penguinbutler"] == []
