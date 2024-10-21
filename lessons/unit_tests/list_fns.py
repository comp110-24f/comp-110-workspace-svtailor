"""practice with returning and modifying lists"""


def get_first(list: list[str]) -> str:
    """takes list[str] as input and returns the first element"""
    if len(list) == 0:
        return ""

    return list[0]


def remove_first(list: list[str]) -> None:
    """takes a list[str] as input and removes first element"""
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    """remove and return first element"""
    first: str = list[0]

    list.pop(0)
    return first
