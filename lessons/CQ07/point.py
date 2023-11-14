"""Point Class."""

from __future__ import annotations


class Point:
    """Class to create a point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Sets inputed x and y to the value of attributes x and y.""" 
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Scales by inputed value."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Make a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point