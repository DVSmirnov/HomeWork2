import pytest
from src.Figure import Figure
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


class Triangle(Figure):
    def init(self, a, b, c):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError("Сумма двух сторон должны быть больше третьей стороны")
        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        semiperimeter = self.get_pr / 2
        return (semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c)) ** (
                    1 / 2)

    @property
    def get_pr(self):
        return self.a + self.b + self.c


circle = Circle(10)
triangle = Triangle(12, 13, 14)
print(triangle.add_Area(circle))
print(triangle.get_area)
print(triangle.get_pr)