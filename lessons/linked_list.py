"""practice w recursive structures -> linked list."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    # a new magic method
    def __str__(self) -> str:
        """produce a string representation of a linked list."""

        rest: str = "TODO"
        # TODO: figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""

    if head is None:
        return "None"

    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    rest: int = 0

    # base case: when head is the last node
    if head.next is None:
        return head.value

    # recursive case:
    else:
        rest: int = last(head.next)
        return rest


def recursive_range(start: int, end: int) -> Node | None:
    """build a list recursively from start to end."""

    if start == end:
        return None

    if start > end:
        raise ValueError("invalid arguments")

    else:
        # first value in your list:
        first: int = start
        # assign the rest of your list a value
        rest: Node | None = recursive_range(start + 1, end)
        # return new node that is first followed by rest
        return Node(first, rest)


print(recursive_range(110, 113))
