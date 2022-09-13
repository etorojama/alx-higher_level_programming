#!/usr/bin/python3
"""A class Square"""


class Square:
    """Square class initialized with size"""

    def __init__(self, size=0):
        """Square class initialized with size"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method"""
        return self.__size * self.__size
