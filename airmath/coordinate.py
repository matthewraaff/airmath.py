# airmath.py
# Author: Matthew Raaff 2023

class Coordinate():
    """
    Represents a coordinate in 2D context.

    Parameters
    ----------
    point_a : float
        The x-axis point of the coordinate.
    point_b : float
        The y-axis point of the coordinate.

    Attributes
    ----------
    a : float
        The x-axis point of the coordinate.
    b : float
        The y-axis point of the coordinate.
    """
    def __init__(self, point_a: float, point_b: float):
        self.a = point_a
        self.b = point_b

    def __repr__(self) -> str:
        return "Coordinate<{0}, {1}>".format(
            self.a,
            self.b
            )
    
    def __str__(self) -> str:
        return "({0}, {1})".format(
            self.a,
            self.b
            )
    
    def __add__(self, other):
        return Coordinate(
            self.a + other.a,
            self.b + other.b
            )
    
    def __sub__(self, other):
        return Coordinate(
            self.a - other.a,
            self.b - other.b
            )
    
    def __mul__(self, other):
        return Coordinate(
            self.a * other.a,
            self.b * other.b
            )
    
    def mutate(self, point_a: float, point_b: float):
        self.a = point_a
        self.b = point_b

    def mutate_a(self, point_a: float):
        self.a = point_a

    def mutate_b(self, point_b: float):
        self.b = point_b
    
__all__ = ["Coordinate"]