"""File to define River class."""

__author__ = "730772504"


from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines new River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []  # creates new list with type Fish (see fish.py)
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks ages to see if animals are too old (RIP)."""
        copy_fish: list[Fish] = []
        copy_bear: list[Bear] = []

        # check fish ages:
        for fish in self.fish:
            # when function is called, its a reference to specific River class type
            # so for each fish in my_river's fish list:
            if fish.age <= 3:  # calls on age attribute for self.fish
                copy_fish.append(fish)

        # check bear ages:
        for bear in self.bears:
            if bear.age <= 5:
                copy_bear.append(bear)

        # updates self.fish and self.bears with new fish/bear populations
        self.fish = copy_fish
        self.bears = copy_bear

        return None

    def remove_fish(self, amount: int) -> None:
        """Removes <amount> fish from the river."""
        copy_fish: list = []  # create empty list to append remaining fish in

        for num in range(amount, len(self.fish)):
            copy_fish.append(self.fish[num])
            # skips over the fish that need to be removed

        self.fish = copy_fish  # reassigns self.fish to new list w removed fish

    def bears_eating(self) -> None:
        """Simulates bears eating fish in river."""
        for bear in self.bears:  # for each bear in list of bears in river
            if len(self.fish) >= 5:
                # if fish in river is at least 5 then, bear eats 3 fish
                bear.eat(3)
                self.remove_fish(3)

        return None

    def check_hunger(self) -> None:
        """Removes bears from self.bears if they are starving (RIP)."""
        copy_bears: list = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                # appends all bears that aren't starved to new list
                copy_bears.append(bear)

        self.bears = copy_bears
        return None

    def repopulate_fish(self) -> None:
        """Adds four fish for every pair of fish in the population."""
        n: int = len(self.fish)

        if n % 2 == 0:
            # if population of fish is even
            for num in range(0, (n // 2) * 4):
                self.fish.append(Fish())  # adds new object of type Fish to list

        if n % 2 == 1:
            n -= 1
            # if population of fish is odd, make it even
            for num in range(0, (n // 2) * 4):
                self.fish.append(Fish())

        return None

    def repopulate_bears(self) -> None:
        """Adds one bear for every pair of bears in the population."""
        n: int = len(self.bears)

        if n % 2 == 0:
            for num in range(0, n // 2):
                self.bears.append(Bear())

        if n % 2 == 1:
            for num in range(1, n // 2):
                self.bears.append(Bear())

        return None

    def view_river(self):
        """Prints the river status out."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week in the River."""
        for repeat in range(0, 7):
            self.one_river_day()
