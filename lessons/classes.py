"""practice with classes and methods"""

import math


class Circle:
    radius: float  # radius attribute

    def __init__(self, r: float):
        """defines a circle with radius r"""
        # you can have multiple parameters in the __init__ method
        self.radius = r

    def area(self):
        return math.pi * (self.radius**2)


class Rectangle:
    width: float  # width attribute
    height: float  # height attribute

    def __init__(self, w, h):
        """defines a rectangle with width and height"""
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height
