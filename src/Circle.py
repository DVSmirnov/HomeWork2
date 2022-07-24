from math import *

from src.Figure import Figure


class Circle(Figure):
    NAME ='Circle'

    def __init__(self, r):
        if r <= 0:
            raise ValueError("Радиус должен быть больше нуля")
        self.r = r

    @property
    def get_area(self):
        return pi * self.r * self.r

    @property
    def get_pr(self):
        return 2 * pi * self.r

