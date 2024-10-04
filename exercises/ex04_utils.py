"""exercise 04! implementing alogrithms to practice computational thinking"""

__author__ = "730772504"

a: list[int] = [3, 2, 0]
b: list[int] = [4, 5, 6]


def all(list: list[int], num: int) -> bool:
    """checks to see if each element in list matches the given input number"""
    index: int = 0

    if list == []:
        # check to see if list is empty first
        return False

    while index < len(list):

        if list[index] != num:
            # checks to see if element does not match the number
            return False

        index += 1

    return True
    # will only return True if it doesn't return False in the if loop


def max(list: list[int]) -> int:
    """returns the maximum value of a list"""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
        # checks to see if list is empty - if so returns a ValueError

    index: int = 0
    max: int = list[index]
    # stores the max value  as we loop through the list

    while index < len(list):
        if list[index] > max:
            max = list[index]

        index += 1

    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """checks to see if two lists are DEEPLY EQUAL (every element in list matches other list)"""
    index: int = 0

    if len(list_1) != len(list_2):
        # checks to see if they are the same length
        return False

    while index < len(list_1) and index < len(list_2):
        if list_1[index] != list_2[index]:
            return False
            # exits the function once return False

        index += 1

    return True
    # only returns True if it doesn't return false in the if loop


def extend(list_1: list[int], list_2: list[int]) -> None:
    """appends each element of one list onto another list"""
    index: int = 0

    while index < len(list_2):
        # for each element in list 2, append it onto list 1
        list_1.append(list_2[index])
        index += 1
