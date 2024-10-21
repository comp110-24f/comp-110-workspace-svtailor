"""exercise 05! practice writing unit tests for functions"""

__author__ = "730772504"


from exercises.ex05.utils import only_evens, sub, add_at_index

# first, import functions so you can test them
import pytest

# must import in order to raise exception error for testing add_at_index


# ONLY_EVENS TESTING:
def test_only_evens() -> None:
    """should return a new list with only even values ([2, 2, 4, 6, 8])"""

    a: list = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8]

    assert only_evens(a) == [2, 2, 4, 6, 8]
    # RV should be [2, 2, 4, 6, 8]


def test_only_evens_creates_new_list() -> None:
    """tests that only_evens doesn't modify the original input list"""

    a: list = [3, 4, 5, 6, 8]

    only_evens(a)
    # calls on function which should store values in a new list

    assert a == [3, 4, 5, 6, 8]
    # makes sure a hasn't been modified


def test_only_evens_empty_list() -> None:
    """an empty list input should return an empty list"""

    assert only_evens([]) == []


# SUB TESTING:
def test_sub() -> None:
    """makes sure the function creates a sublist between the given index range"""
    a: list = [1, 2, 3, 4, 5, 6]

    assert sub(a, 1, 3) == [2, 3]
    # RV should be [2, 3] -> not inclusive of end input


def test_sub_new_list() -> None:
    """function should append sub list into new list, not modify the original list"""
    a: list = [1, 2, 3, 4, 5, 6]

    sub(a, 1, 3)

    assert a == [1, 2, 3, 4, 5, 6]
    # a should not have been modified


def test_sub_out_of_range_idx() -> None:
    """function should return an empty list for out of range indices"""
    a: list = [12, 14, 16]

    assert sub(a, 4, -1) == []


# ADD_AT_INDEX TESTING:
def test_add_at_index() -> None:
    """fn should return the same list w/ the given input inserted at the given index"""
    a: list = [10, 20, 40]

    add_at_index(a, 30, 2)

    assert a == [10, 20, 30, 40]
    # function should return a new list [10, 20, 30, 40]


def test_add_at_index_modify_og_list() -> None:
    """function should modify original list"""

    a: list = [3, 3, 3]

    add_at_index(a, 3, 3)

    assert a != [3, 3, 3]
    # list should not equal its original value


def test_add_at_index_raises_indexerror() -> None:
    """test that add_at_index raises an IndexError for an invalid index."""
    a: list = [1, 2, 4]

    with pytest.raises(IndexError):
        add_at_index(a, 3, 4)
        # an IndexError is raised when the input index is greater than the length of
        # the input list
