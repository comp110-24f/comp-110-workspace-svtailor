"""Some happy, little trees!"""

from lessons.art.turtle import Turtle
from math import pi

# from random import random


__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0  # Constant


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas + draws line!"""
    t: Turtle = Turtle()
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)

    length: float = 150.0
    while length > 0.0:
        t.forward(length)
        t.left(pi / 2.0)
        length -= 2.0
    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)
    # magic art happens
    if length > 3.0:
        branch(t, 0.75 * length, angle + 35 * DEGREE)
        branch(t, 0.75 * length, angle - 35 * DEGREE)

    t.turnTo(angle + pi)
    t.forward(length)
