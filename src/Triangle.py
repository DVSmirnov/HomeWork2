import pytest
from src.Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    #def creation_triangle():
        #with pytest.raises(ValueError):
            #Triangle(a, b)

    def get_area(self):
        return 1/2*(self.a * self.h)

    def get_pr(self):
        return self.a + self.b + self.c