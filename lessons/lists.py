"""basic syntax with lists"""

# creating an empty list with the name my_numbers

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal


# adding an item to a list
my_numbers.append(1.5)
my_numbers.append(2.5)

# print(my_numbers)

# creating an already populated list
game_points: list[int] = [102, 86, 94]

# indexing a list -> subscription notation/indexing
recent_game: int = game_points[2]  # would return 94
# stores the list item as a new variable

# print(recent_game)
# print(game_points)

# modifying items in a list by index
game_points[1] = 72
# print(game_points)  # prints [102, 72, 94]

# length of a list
len(game_points)  # returns 3 bc 3 objects in game_points

# removing an item from a list
game_points.pop(1)

print(game_points)
game_points.append(102)
game_points.append(102)


# practice! write a function:


def display(int_list: list[int]) -> None:
    # make sure you define the type of the items in a list

    # prints every item in the input list
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(game_points)
