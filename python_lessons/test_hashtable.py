import pytest

@pytest.mark.skip
def test_always_pass():
    assert 2 + 2 == 4, 'this is a passing test' 
    assert 2 + 2 != 22, 'this is failure test'
    # assert 5 * 5 == 6, 'this test fails'

from .understanding_hashfn import HashTable

# must create a object instance with a capacity
@pytest.mark.skip
def test_should_create_ht():
    assert HashTable(capacity=100) is not None
# must have length attribute
@pytest.mark.skip
def test_ht_must_have_len():
    assert len(HashTable(capacity=100)) == 100
# must have empty slots
@pytest.mark.skip
def test_ht_must_have_empty_slots():
    assert HashTable(capacity=3).value == [None, None, None]


# writing the above function using given-when-then
def test_should_create_empty_value_slots():
    # Given
    # blanks = object()  # Using this blank will lead to test failure, as the 
    # objects created are difference
    from .understanding_hashfn import blanks
    # expected_pairs = [None, None, None]
    expected_pairs = [blanks, blanks, blanks]
    hash_table = HashTable(capacity=3)

    # When
    actual_pairs = hash_table.pairs

    # then
    assert actual_pairs == expected_pairs
# The "given" part describes the initial state and preconditions to your test case, while "when" represents the action of your code under test, and then is responsible for asserting the resulting outcome.


def test_should_insert_kv_pair():
    ht = HashTable(capacity=100)

    ht['hola'] = 'hello'
    ht[968.5] = 775
    ht[False] = True

    assert ('hola', 'hello') in ht.pairs
    assert (968.5, 775) in ht.pairs
    assert (False, True) in ht.pairs

    assert len(ht) == 100


@pytest.mark.skip
def test_remove_elements_should_not_shrink_ht():
    pass


# start by writing the test for desired behaviour
def test_should_not_contain_none_when_created():
    assert None not in HashTable(capacity=100).pairs


# inserting None value
def test_should_insert_none_value():
    ht = HashTable(capacity=100)
    ht['key'] = None
    assert None in ht.pairs


# fixture exposed by pytest
@pytest.fixture
def hash_table():
    sd = HashTable(capacity=100)
    sd['hola'] = 'hello'
    sd[86.6] = 775
    sd[False] = True
    return sd

def test_should_find_value_by_key(hash_table):
    assert hash_table['hola'] == 'hello'
    assert hash_table[86.6] == 775
    assert hash_table[False] == True


# raising keyerror when trying to access a missing key
def test_should_raise_error_on_missing_key():
    ht_empty = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        ht_empty["missing_key"]
    assert exception_info.value.args[0] == "missing_key"


# implementing the 'in' key
def test_should_find_key(hash_table):
    assert 'hola' in hash_table


def test_should_not_find_key(hash_table):
    assert "missing" not in hash_table


def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"


def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None


def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"


def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"

def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert "hello" in hash_table.pairs
    assert len(hash_table) == 100

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert "hello" not in hash_table.pairs
    assert len(hash_table) == 100

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[86.6] == 775
    assert hash_table[False] is True
    assert len(hash_table) == 100