"""tests function in find_max.py"""

__author__ = "730772504"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_use1() -> None:
    """function should return 5 as maximum for list a"""

    a: list[int] = [5, 1, 2, 3, 4, 5]

    assert find_and_remove_max(a) == 5


def test_find_and_remove_max_use2() -> None:
    """function should remove all instances of 5 from list a"""
    a: list[int] = [5, 1, 2, 3, 4, 5]

    find_and_remove_max(a)

    assert a == [1, 2, 3, 4]


def test_find_and_remove_max_edge() -> None:
    """function should return -1 if given an empty list"""

    assert find_and_remove_max([]) == -1
