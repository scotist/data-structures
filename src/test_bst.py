# _*_ encoding: utf-8 _*_
"""Tests for binary search tree."""
from bst import Bst
import pytest
import types
import random
from bst_graph_viz import render_viz_fixture
from collections import namedtuple
import math

Fixture = namedtuple('Fixture', ['seq', 'instance', 'size', 'depth',
                     'delete_value', 'insert_value', 'undeleted', 'in_order'])

EDGE_CASES = [[0, 1, 2], [2, 1, 0], [0, 2, 1], [2, 0, 1],
              [1, 2, 0], [1, 0, 2], [], [0], [0, 1], [1, 0]]

RANDOM_INSTANCES = [random.sample(range(1000),
                    random.randrange(1, 100)) for n in range(50)]


@pytest.fixture
def empty_instance():
    """Empty tree fixture."""
    tree = Bst()
    return tree


@pytest.fixture(params=EDGE_CASES + RANDOM_INSTANCES)
def multi_tree(request):
    """Simple tree fixture."""
    tree = Bst()
    for n in request.param:
        tree.insert(n)
    undeleted = request.param[:]
    if request.param:
        delete_value = random.choice(request.param)
        undeleted.remove(delete_value)
    else:
        delete_value = None
    size = len(request.param)
    try:
        depth = math.floor(math.log(size, 2)) + 1
    except ValueError:
        depth = 0
    in_order = list(sorted(request.param))
    return Fixture(request.param, tree, size,
                   depth,
                   delete_value,
                   random.choice(range(1001, 2000)),
                   undeleted,
                   in_order)


@pytest.fixture
def instance():
    """Full tree fixture."""
    tree = Bst()
    for n in range(20):
        tree.insert(n)
    return tree


@pytest.fixture
def left_left_instance():
    """Left-balanced fixture."""
    tree = Bst()
    for n in range(0, 20, -1):
        render_viz_fixture(tree, 'left_left' + str(n))
        tree.insert(n)
    return tree


@pytest.fixture
def instance2():
    """Fun tree fixture."""
    fun_tree = Bst()
    insertions = [11, 17, 9, 10, 8, 7, 4, 12, 19, 18]
    for fun in insertions:
        fun_tree.insert(fun)
    return fun_tree


@pytest.fixture
def deleteable_instance(instance2):
    """Fixture for deletion."""
    insertions = [11, 17, 9, 10, 8, 7, 4, 12, 19, 18]
    delete_value = random.choice(insertions)
    insertions.remove(delete_value)
    return (instance2, insertions, delete_value)


def test_tree_correct(multi_tree):
    """Test that any given tree is correct in relationships."""
    assert tree_checker(multi_tree.instance)


def tree_checker(tree):
    """"Help function to check binary tree correctness."""
    if tree is None or tree.value is None:
        return True

    if tree.right_child is not None and tree.right_child.value < tree.value:
        return False
    if tree.left_child is not None and tree.left_child.value > tree.value:
        return False

    return all([tree_checker(tree.left_child),
                tree_checker(tree.right_child)])


def test_new_empty_tree(empty_instance):
    """Test that an empty tree is still a tree."""
    assert all([
        empty_instance.value is None,
        empty_instance.parent is None,
        empty_instance.left_child is None,
        empty_instance.right_child is None])


def test_insert(empty_instance):
    """Test insert method on empty tree."""
    empty_instance.insert(0)
    assert empty_instance.contains(0)


def test_insert_many(empty_instance):
    """Test insert method with many values."""
    insertions = list(range(12))
    for chump in insertions:
        empty_instance.insert(chump)
    for chump in insertions:
        assert empty_instance.contains(chump)


def test_insert_fail(instance):
    """Test insert method with badly mixed values."""
    with pytest.raises(TypeError):
        instance.insert("This can't go here!")


def test_insert_fail_2(instance):
    """Test insert method with None value."""
    with pytest.raises(TypeError):
        instance.insert(None)


def test_contains(instance):
    """Test contains method."""
    for n in range(20):
        assert instance.contains(n)


def test_contains_false(instance):
    """Test false example for contains method."""
    assert not instance.contains(1000)


def test_size(instance):
    """Test size method."""
    assert instance.size() == 20


def test_size_empty(empty_instance):
    """Test size method on empty tree."""
    assert empty_instance.size() == 0


def test_depth(instance):
    """Test depth method."""
    assert instance.depth() == 5


def test_depth_empty(empty_instance):
    """Test depth method on empty tree."""
    assert empty_instance.depth() == 0


def test_balance(multi_tree):
    """Test balance."""
    assert -1 <= multi_tree.instance.balance() <= 1


def test_depth_simple(multi_tree):
    """Test depth method on simple instances."""
    if multi_tree.size < 5:
        assert multi_tree.instance.depth() == multi_tree.depth
    else:
        abs(multi_tree.instance.depth() - multi_tree.depth) < 2


def test_size_simple(multi_tree):
    """Test."""
    assert multi_tree.instance.size() == multi_tree.size


def test_balance_left(instance2):
    """Test balance method on left-unbalanced tree."""
    assert instance2.balance() == -1


def test_balance_balanced(instance2):
    """Test balance method on balanced tree."""
    instance2.insert(20)
    instance2.insert(21)
    assert instance2.balance() == 0


def test_balance_right(instance2):
    """Test balance method further."""
    instance2.insert(20)
    instance2.insert(21)
    instance2.insert(22)
    assert instance2.balance() == 0


def test_balance_extreme_right(instance):
    """Test self-balance method on extremely-unbalanced tree."""
    assert -2 < instance.balance() < 2


def test_in_order(multi_tree):
    """Test in-order traversal method."""
    assert list(multi_tree.instance.in_order()) == multi_tree.in_order


def test_in_order_empty(empty_instance):
    """Test in-order traversal on empty tree."""
    assert list(empty_instance.in_order()) == []


def test_pre_order(instance2):
    """Test pre-order traversal method."""
    assert list(instance2.pre_order()) == [9, 7, 4, 8, 17, 11, 10, 12, 19, 18]


def test_pre_order_empty(empty_instance):
    """Test pre-order traversal on empty tree."""
    assert list(empty_instance.pre_order()) == []


def test_post_order(instance2):
    """Test post-order traversal method."""
    assert list(instance2.post_order()) == [4, 8, 7, 10, 12, 11, 18, 19, 17, 9]


def test_post_order_empty(empty_instance):
    """Test post-order traversal on empty tree."""
    assert list(empty_instance.post_order()) == []


def test_breadth_first(instance2):
    """Test breadth-first traversal method."""
    assert list(instance2.breadth_first()) == [9, 7, 17, 4, 8, 11, 19,
                                               10, 12, 18]


def test_breadth_first_empty(empty_instance):
    """Test breadth_first traversal on empty tree."""
    assert list(empty_instance.breadth_first()) == []


def test_generators(instance):
    """Test traversal methods yield generators."""
    assert all([isinstance(method(), types.GeneratorType) for method in
               [instance.pre_order,
                instance.post_order,
                instance.in_order,
                instance.breadth_first]])


def test_delete_contains(multi_tree):
    """Test that tree does not contain deleted value after delete."""
    multi_tree.instance.delete(multi_tree.delete_value)
    if multi_tree.size:
        assert not multi_tree.instance.contains(multi_tree.delete_value)


def test_size_after_delete(multi_tree):
    """Test that tree is one smaller after deletion."""
    if multi_tree.size:
        multi_tree.instance.delete(multi_tree.delete_value)
        new_size = multi_tree.instance.size()
        assert new_size == len(multi_tree.undeleted) == multi_tree.size - 1


def test_balance_after_delete(multi_tree):
    """Test that the tree is not worse balanced after deletion."""
    multi_tree.instance.delete(multi_tree.delete_value)
    assert -2 < multi_tree.instance.balance() < 2


def test_contains_undeleted(multi_tree):
    """Test that tree still contains all undeleted values."""
    multi_tree.instance.delete(multi_tree.delete_value)
    assert all([multi_tree.instance.contains(value)
                for value in multi_tree.undeleted])


def test_delete_not_contained(multi_tree):
    """Test that delete leaves the list intact if value not in tree."""
    balance_before = multi_tree.instance.balance()
    multi_tree.instance.delete(9999999999999)
    assert multi_tree.instance.balance() == balance_before


def test_delete_not_contained_2(multi_tree):
    """Test that delete leaves the list intact if value not in tree."""
    multi_tree.instance.delete(9999999999999)
    assert multi_tree.instance.size() == multi_tree.size


def test_delete_empty(empty_instance):
    """Test delete on empty tree."""
    assert empty_instance.delete(999) is None


def test_delete_root(instance2):
    """Test delete when deletable is root."""
    instance2.delete(11)
    values = ([17, 9, 10, 8, 7, 4, 12, 19, 18])
    assert list(instance2.in_order()) == sorted(values)
    assert instance2.size() == len(values)


def test_tree_correct_after_delete(multi_tree):
    """Make sure that the tree is correct after a deletion."""
    if multi_tree.size:
        multi_tree.instance.delete(multi_tree.delete_value)
        assert tree_checker(multi_tree.instance)


def test_delete_root_1(empty_instance):
    """Test delete root when root has no children."""
    empty_instance.insert(1)
    assert empty_instance.size() == 1
    empty_instance.delete(1)
    assert empty_instance.size() == 0


def test_delete_root_2(empty_instance):
    """Test delete root when root has one child."""
    empty_instance.insert(1)
    empty_instance.insert(2)
    assert empty_instance.size() == 2
    empty_instance.delete(1)
    assert empty_instance.size() == 1


def test_delete_root_3(empty_instance):
    """Test delete root when root has two children."""
    empty_instance.insert(1)
    empty_instance.insert(2)
    empty_instance.insert(3)
    assert empty_instance.size() == 3
    empty_instance.delete(1)
    assert empty_instance.size() == 2
