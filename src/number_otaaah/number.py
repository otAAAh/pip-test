"""Module Provides explicit number handling"""


from typing import Self


class Number:
    """Class for explicit Calculation"""
    x: float

    def __init__(self, x):
        self.x = x

    def add(self, y: float) -> Self:
        """Adds number y to Number x"""
        self.x += y
        return self

    def sub(self, y: float) -> Self:
        """Subs number y to Number x"""
        self.x -= y
        return self

    def times(self, y: float) -> Self:
        """Multiplies number y to Number x"""
        self.x *= y
        return self

    def div(self, y: float) -> Self:
        """Divides number y to Number x"""
        self.x /= y
        return self
