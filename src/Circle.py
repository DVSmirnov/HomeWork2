from math import *

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    @property
    def get_area(self):
        return pi * self.r * self.r

    @property
    def get_pr(self):
        return 2 * pi * self.r


circle = Circle(40)
print(circle.get_area)
print(circle.get_pr)
