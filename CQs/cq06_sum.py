"""Summing the elements of a list using different loops"""

__author__ = "730772504"


def w_sum(vals: list[float]) -> float:
    """sums each value in a list using a while loop"""

    index: int = 0
    sum: float = 0.0
    # created an empty variable to store the value of the sum as we loop through

    while index < len(vals):
        sum += vals[index]
        index += 1

    return sum


def f_sum(vals: list[float]) -> float:
    """sums each value in a list using a for loop"""

    sum: float = 0.0

    for num in vals:
        # for each number in the list, vals, add it to the sum
        sum += num

    return sum


def f_range_sum(vals: list[float]) -> float:
    """sums each value in a list using a for loop and range()"""

    sum: float = 0.0

    for index in range(0, len(vals)):
        # range doesn't include the end point, and step = 1
        # for each index in the list, add the associated value to the sum
        sum += vals[index]

    return sum
