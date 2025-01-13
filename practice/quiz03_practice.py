"""practicing function writing for quiz 03"""

# class writing + magic methods:


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, whip: bool, flavor: str, marshmallows: int, sweetness: int):
        self.has_whip = whip
        self.flavor = flavor
        self.marshmallow_count = marshmallows
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness += 2 * mallows


def order_cost(drinks: list[HotCocoa]) -> float:
    cost: float = 0.0

    for drink in drinks:
        if drink.has_whip:
            cost += 2.50

        else:
            cost += 2.00

    return cost


# timespent class
class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes
        self.reset_min = minutes

    def add_time(self, added_time: int) -> None:
        self.minutes += added_time

    def reset(self) -> int:
        self.minutes = self.reset_min
        return self.minutes


# dictionary reinforcement questions
# 22
def even_keys(input: dict[str, int]) -> list:
    list_keys: list[int] = []

    for key in input:
        if input[key] % 2 == 0:
            list_keys.append(key)


# 23
def max_value(dictionary: dict[str, int]) -> str:
    max: int = 0
    store_key: str = ""

    for key in dictionary:
        if dictionary[key] > max:
            max = dictionary[key]
            store_key = key

    return store_key

#26
def swap(input: dict[float, int]) -> dict[int, float]:
    copy_dict: dict[int, float] = {}

    for key in input
        copy_dict[input[key]] = key

    return copy_dict