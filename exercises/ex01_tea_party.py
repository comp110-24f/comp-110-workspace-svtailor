"""a program to gain practice with functions by taking the number of guests at a tea party and returning the resources needed to throw the party"""

__author__: str = "730772504"


def main_planner(guests: int) -> None:
    """executes the actual program - prints the actual details of the tea party"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # can't add str and int, must convert all numbers to str
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # calls on tea_bags fn, uses guests variable as the argument
    print(
        "Treats: " + str(treats(people=guests))
    )  # calls on treats fn, uses guests variable as the argument
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treats_count=treats(people=guests))
        )
    )  # calls on functions tea_count and treats_count within the cost fn to calculate cost of the tea party


def tea_bags(people: int) -> int:
    """function to return the number of tea bags needed based on how many people are at the party"""
    return people * 2


def treats(people: int) -> int:
    """tells you how many treats you need based on the number of people attending the party"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treats_count: int) -> float:
    """tells you how much it will cost to purchase your teabags and treats"""
    return 0.50 * tea_count + 0.75 * treats_count


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # takes input from user and uses it as an argument for the main_planner fn
    # must place at the end after all functions have been defined otherwise main_planner wouldn't work
