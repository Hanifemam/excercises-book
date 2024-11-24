import pytest

from ..linked_list import Node
from ..linked_list import LinkedList


# Test initialized node value
def test_initialize_node_value_case():
    node = Node(12)
    assert node.value == 12


# Test initialized node next
def test_initialized_node_next_case():
    node = Node(12)
    assert node.next is None


# Test setter
def test_set_value():
    node = Node(12)
    node.value = 14
    assert node.value == 14


# Test next of the node
def test_next_node():
    node1 = Node(12, Node(14))
    assert node1.next.value == 14


# Test insertion first item
def test_insertion_first_element_head_tail():
    linked_list = LinkedList()
    linked_list.insert(value=5)
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 5


# Test insertion first item
def test_insertion_tail():
    linked_list = LinkedList()
    linked_list.insert(value=5)
    linked_list.insert(value=6)
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 6
    assert linked_list.head.next.value == 6


# Test get_at(i) item
def test_get_at_values():
    linked_list = LinkedList()
    linked_list.insert(value=0)
    linked_list.insert(value=1)
    linked_list.insert(value=2)
    linked_list.insert(value=3)
    assert linked_list.get_at(0).value == 0
    assert linked_list.get_at(1).value == 1
    assert linked_list.get_at(2).value == 2
    assert linked_list.get_at(3).value == 3


# Test get_at(i) out of range
def test_get_at_values_out_of_range():
    linked_list = LinkedList()
    linked_list.insert(value=0)
    linked_list.insert(value=1)
    linked_list.insert(value=2)
    linked_list.insert(value=3)
    print(linked_list.get_at(4))
    assert linked_list.get_at(4) is None


# Test size
def test_size_def():
    linked_list = LinkedList()
    linked_list.insert(value=0)
    assert len(linked_list) == 1
    linked_list.insert(value=1)
    assert len(linked_list) == 2
    linked_list.insert(value=2)
    assert len(linked_list) == 3
    linked_list.insert(value=3)
    assert len(linked_list) == 4


# Test itterator with elements
def test_iteration_test():
    linked_list = LinkedList()
    linked_list.insert(value=0)
    linked_list.insert(value=1)
    linked_list.insert(value=2)
    linked_list.insert(value=3)
    test_list = [0, 1, 2, 3]
    for linked_list_item, list_item in zip(linked_list, test_list):
        assert linked_list_item == list_item
