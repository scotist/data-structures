# _*_ encoding: utf-8 _*_
"""Test simple hash table implementation."""

from hash_table import HashTable
import pytest


BAD_TYPES = [None, 1.0, 8, True, [], (1,), {}, set()]
SAMPLE_STRINGS = ["Word", "Something", "Hey", "What", "etc", "chump" "Buddy",
                  "", "a", "ab", "supercalifragilisticexpialidocious" * 10]
TABLES = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]


def get_words():
    """Get a big set of values for thorough tests."""
    with open("/usr/share/dict/words", "r") as get_file:
        for line in get_file:
            yield line


@pytest.fixture(params=TABLES)
def sample_table(request):
    """Sample hash tables fixture."""
    return HashTable(request.param)


@pytest.fixture
def words_table(request):
    """Big set of sample values."""
    big_table = HashTable(1024)
    for word in get_words():
        big_table.set(word, word)
    return big_table


@pytest.mark.parametrize("value", SAMPLE_STRINGS)
def test_hash_int(sample_table, value):
    """Test hash function returns integer."""
    assert isinstance(sample_table._hash(value), int)


@pytest.mark.parametrize("value", BAD_TYPES)
def test_hash_type_error(sample_table, value):
    """Test that any input but string raises type error."""
    with pytest.raises(TypeError):
        sample_table._hash(value)


@pytest.mark.parametrize("value", SAMPLE_STRINGS)
def test_set_get(sample_table, value):
    """Test hash function sets and returns values."""
    sample_table.set(value, value)
    assert sample_table.get(value) == value


def test_get_fail(sample_table):
    """Test table return none when key not present."""
    for string in SAMPLE_STRINGS:
        sample_table.set(string, string)
    assert sample_table.get("bub") is None


@pytest.mark.parametrize("value", SAMPLE_STRINGS)
def test_table_size(sample_table, value):
    """Test size of hash table."""
    assert -1 < sample_table._hash(value) < sample_table.slots


def test_correct_hash(sample_table):
    """Test hash puts key in correct slot."""
    sample_table.set("a", "bob")
    slot = ord("a") % sample_table.slots
    assert ("a", "bob") in sample_table._table[slot]


def test_collision():
    """Test hash puts multiple buckets in one slot where needed."""
    small_table = HashTable(2)
    small_table.set("a", "hello")
    small_table.set("c", "world")
    assert ("a", "hello") in small_table._table[1]
    assert ("c", "world") in small_table._table[1]
    assert small_table._table[0] == []


def test_set_get_big(words_table):
    """Test hashing and retrieving on big set of values."""
    for word in get_words():
        assert words_table.get(word) == word
