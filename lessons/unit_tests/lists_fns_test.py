"""practice with unit tests"""

from lessons.unit_tests.list_fns import get_first, remove_first

# imports all three functions from the file lists_fns


# writing our unit test


def test_get_first() -> None:
    """get_first should return the first element"""

    food: list[str] = ["banana", "egg", "cereal", "bread"]

    assert get_first(food) == "banana"
    # RV should be "banana"


def test_remove_first() -> None:
    """remove_first should remove the first element from the input list"""

    food: list[str] = ["banana", "egg", "cereal", "bread"]

    remove_first(food)

    assert food == ["egg", "cereal", "bread"]


def test_get_first_edge_case() -> None:
    """get_first called on an empty list should return an empty string"""

    assert get_first([]) == ""
