import pytest

from ..sorting import Sorting


# Test for sorting an array using insertion sort
def test_insertion_sort_normal_case():
    arr = [5, 3, 8, 4, 2]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [2, 3, 4, 5, 8]


def test_insertion_sort_second_case():
    arr = [10, 94, 104, 76]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [10, 76, 94, 104]


# Test for an empty array
def test_insertion_sort_empty():
    arr = []
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == []


# Test for an array with one element
def test_insertion_sort_single_element():
    arr = [42]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [42]


# Test for an already sorted array
def test_insertion_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [1, 2, 3, 4, 5]


# Test for an array with duplicate elements
def test_insertion_sort_duplicates():
    arr = [5, 1, 5, 2, 5]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [1, 2, 5, 5, 5]


# Test for array with negative numbers
def test_insertion_sort_negative_numbers():
    arr = [5, -3, 8, -1, 2]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [-3, -1, 2, 5, 8]

def test_merge_sort_normal_case():
    arr = [5, 3, 8, 4, 2]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [2, 3, 4, 5, 8]


def test_merge_sort_second_case():
    arr = [10, 94, 104, 76]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [10, 76, 94, 104]


# Test for an empty array
def test_imerge_sort_empty():
    arr = []
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == []


# Test for an array with one element
def test_imerge_sort_single_element():
    arr = [42]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [42]


# Test for an already sorted array
def test_merge_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [1, 2, 3, 4, 5]


# Test for an array with duplicate elements
def test_merge_sort_duplicates():
    arr = [5, 1, 5, 2, 5]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [1, 2, 5, 5, 5]


# Test for array with negative numbers
def test_merge_sort_negative_numbers():
    arr = [5, -3, 8, -1, 2]
    sorter = Sorting(arr)
    sorter.insertion_sort()
    assert sorter.array == [-3, -1, 2, 5, 8]