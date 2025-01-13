""" quiz 04 practice """

# recursive structures

# 1a
from __future__ import annotations


class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next


def sum_node_values(node: Node | None) -> int:
    if node is None:
        return 0

    else:
        sum: int = 0
        for num in node.value:
            sum += num

        return sum + sum_node_values(node.next)


def increment_node_values(head: Node | None) -> Node | None:
    if head is None:
        return None

    else:
        for value in head.value:
            value += 1

        return Node(head.value, increment_node_values(head.next))


def print_nodes(head: Node | None) -> None:
    if head is None:
        return None

    else:
        print(head.value)
        print_nodes(head.next)
