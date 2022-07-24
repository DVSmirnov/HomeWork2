import pytest
from src.Figure import Figure


class Triangle(Figure):
    NAME = 'Triangle'

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть больше нуля")
        elif a + b < c or a + c < b or b + c < a:
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
