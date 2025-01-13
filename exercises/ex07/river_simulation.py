"""File to test river simulation out."""

__author__ = "730772504"


from exercises.ex07.river import River


my_river: River = River(10, 2)
# creates new variable with type River and initalizes it with 10 fish and 2 bears

my_river.view_river()
my_river.one_river_day()
my_river.one_river_day()
my_river.one_river_day()
my_river.one_river_day()
my_river.check_ages()


"""my_river.repopulate_bears()
my_river.view_river()

my_river.repopulate_fish()
my_river.view_river()"""
