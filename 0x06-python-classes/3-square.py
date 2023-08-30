#!/usr/bin/python3

"""Define a class Sq."""


class Square:
    """Represent a sq."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new sq.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the sq."""
        return (self.__size * self)
