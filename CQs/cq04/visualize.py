"""calls on functions defined in other files to practice imports"""

__author__ = "730772504"


from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# imports functions from others files

x: str = "123"
y: str = "abc"

print(concat(x, y))
# calls on function defined in another file

get_coords(x, y)
