from math import *

from src.Figure import Figure

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi * self.r * self.r

    def get_pr(self):
        return 2 * pi * self.r
