"""mutating functions"""

__author__ = "730772504"


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(list: list[int], num: int) -> None:
    """will add an element at the end of your list"""
    list.append(num)


def double(list: list[int]) -> None:
    """will double every element in your list"""
    index: int = 0

    while index < len(list):
        list[index] *= 2
        # same thing as list[index] = list[index] * 2
        index += 1


double(list_2)
# list_2 is a reference to list_1 -> when you double list_2 you double list_1

print(list_1)
print(list_2)
