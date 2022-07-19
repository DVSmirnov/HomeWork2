from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_area(self):
        return self.x * self.y

    @property
    def get_pr(self):
        return 2 * (self.x + self.y)


rectangle = Rectangle(10, 15)
print(rectangle.get_area)
print(rectangle.get_pr)