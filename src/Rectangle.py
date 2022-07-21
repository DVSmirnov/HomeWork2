from src.Figure import Figure


class Rectangle(Figure):
    NAME = 'Rectangle'

    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше нуля")
        self.x = x
        self.y = y

    @property
    def get_area(self):
        return self.x * self.y

    @property
    def get_pr(self):
        return 2 * (self.x + self.y)


