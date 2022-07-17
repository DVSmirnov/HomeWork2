from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def get_pr(self):
        return 2*(self.x + self.y)