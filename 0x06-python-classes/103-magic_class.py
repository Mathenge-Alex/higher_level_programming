#!/usr/bin/python3
"""Define a MagicClass matching the function of a Holberton school bytecode."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initializing a MagicClass.
        Arg:
            radius (float or int): Radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
