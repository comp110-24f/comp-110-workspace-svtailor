"""Exercise 08, Implementing algorithms for a singly-linked list data structure."""

from __future__ import annotations

__author__ = "730772504"


class Node:
    """Defines Node class with attributes for value and next."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Defines attributes for Node Class."""
        self.value = value
        self.next = next

    # A new magic method.
    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"

        # TODO: figure out the rest of the list.
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    rest: int = 0

    # Base case: when head is the last node.
    if head.next is None:
        return head.value

    # Recursive case:
    else:
        rest = last(head.next)
        return rest


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    if start == end:
        return None

    if start > end:
        raise ValueError("invalid arguments")

    else:
        # First value in your list:
        first: int = start
        # Assign the rest of your list a value:
        rest: Node | None = recursive_range(start + 1, end)
        # Return new node that is first followed by rest:
        return Node(first, rest)


print(recursive_range(110, 113))


def value_at(head: Node | None, index: int) -> int:
    """Returns the data value stored in a linked list at a given index."""
    # Base case:
    if index == 0 and head is not None:
        return head.value

    # Edge case: if list is empty.
    elif head is None:
        raise IndexError("Index is out of bounds on the list.")

    # Recursive case: calls on value_at again.
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")

    # Base Case: if head.next is None.
    if head.next is None:
        return head.value

    max_val: int = max(head.next)

    # Recursive case: checks if the current node's value is greater than the stored max
    if head.value > max_val:
        max_val = head.value
        return max_val

    else:
        return max_val


def linkify(input: list[int]) -> Node | None:
    """Returns a linked list of Nodes with values of the inputted list."""
    # Base Case: when the input list is empty.
    if input == []:
        return None

    # Recursive case: adds a new node within the current one for each item in list
    else:
        return Node(input[0], linkify(input[1:]))
        # Will return value to be first item in the list and use recursion for the rest


def scale(head: Node | None, factor: int) -> Node | None:
    """Function to scale up each value in a linked list by given factor."""
    # Base case: when head is None.
    if head is None:
        return None

    # Recursive case: multiplies value of current node by factor,
    # calls funciton on rest of linked list
    else:
        return Node(head.value * factor, scale(head.next, factor))
