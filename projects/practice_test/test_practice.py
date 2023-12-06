from .test_queue import Nodes, Queue
import pytest

def test_creates_node_instance():
    assert Nodes('a') is not None

def test_node_has_value():
    a = Nodes('a')
    assert a.value == 'a'

def test_node_has_next():
    a = Nodes('a')
    assert a.next is None

def test_node_returns_string():
    a = Nodes('a')
    assert str(a) == 'a'

def test_creates_queue_instance():
    assert Queue(Nodes('a')) is not None

@pytest.fixture
def make_queue():
    q1 = Queue(Nodes('a'))
    return q1

def test_queue_has_head(make_queue):
    assert make_queue.head is not None

def test_queue_has_size(make_queue):
    assert make_queue.size == 1

def test_enqueue_on_existing_queue(make_queue):
    make_queue.enqueue('b')  # will check if method is present, and execute

def test_enqueue_increases_size_by_1(make_queue):
    make_queue.enqueue('b') 
    assert make_queue.size == 2  # after enqueue the size has to be increased

def test_dequeue_from_queue(make_queue):
    make_queue.dequeue()

def test_dequeue_returns_head(make_queue):
    pop = make_queue.dequeue()
    assert pop == 'a'

def test_dequeue_reduces_size(make_queue):
    pop = make_queue.dequeue()
    assert make_queue.size == 0

def test_queue_has_contains(make_queue):
    make_queue.contains('a')

def test_contains_returns_bool(make_queue):
    assert make_queue.contains('a')
    assert not make_queue.contains('b')