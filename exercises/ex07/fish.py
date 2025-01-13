"""File to define Fish class."""

__author__ = "730772504"


class Fish:
    """Defines new Fish Class."""

    age: int  # gives the class the attribute age

    def __init__(self):
        """Initializing fish class."""
        self.age = 0  # assigns the attribute age a value (initializes)

        return None

    def one_day(self):
        """Increases value of age attribute by 1."""
        self.age += 1

        return None
