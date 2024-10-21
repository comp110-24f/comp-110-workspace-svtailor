"""exercise 05! practice writing functions to test """

__author__ = "730772504"


def only_evens(input: list[int]) -> list:
    """returns a new list with only the even values of the input"""

    even_list: list[int] = list()
    # new empty list, append even values into new list

    index: int = 0

    while index < len(input):
        if input[index] % 2 == 0:
            # uses mod function, if remainder of num/2 = 0 then even
            even_list.append(input[index])

        index += 1

    return even_list


def sub(input: list[int], start_idx: int, end_idx: int) -> list:
    """should create a sublist between the given index range"""
    sub_list: list = []
    # creates empty list to append sub list into

    for index in range(start_idx, end_idx):
        # for every index from given range

        if index >= 0 and index < len(input):
            # if the given inputs are within the index range for the input list
            sub_list.append(input[index])
            # add each element to the new sub list

    return sub_list


def add_at_index(input: list[int], num: int, idx: int) -> None:
    """should replace element at idx with inputted num in input list"""

    input.append(0)  # creates space to shift list elements in order to append

    if not (0 <= idx < len(input)):
        raise IndexError("Index is out of bounds for the input list")

    for index in range(idx, len(input) - 1):
        input[index + 1] = input[index]

    input[idx] = num
