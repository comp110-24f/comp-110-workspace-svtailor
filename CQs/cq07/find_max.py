"""a function that will find and remove maximum value in list"""

__author__ = "730772504"


def find_and_remove_max(input: list[int]) -> int:
    if input == []:
        # if list is empty then return -1
        return -1

    max: int = 0
    index: int = 0
    index2: int = 0

    # used a while loop because in order to pop you need to reference the index
    while index < len(input):

        if input[index] > max:
            # makes sure the list removes all instances of the maximum
            max = input[index]

        index += 1

    while index2 < len(input):
        # made a seperate while loop so once max is established, then remove from list
        if input[index2] == max:
            input.pop(index2)
        else:
            index2 += 1

    return max
