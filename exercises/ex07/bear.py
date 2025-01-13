"""File to define Bear class."""

__author__ = "730772504"


class Bear:
    """Defines new Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases value of age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1

        return None

    def eat(self, num_fish: int) -> None:
        """Updates bear's hunger score by the amount of fish it ate (num_fish)."""
        self.hunger_score += num_fish
