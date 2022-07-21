from src.Figure import Figure


class Square(Figure):
    NAME = 'Square'

    def __init__(self, z):
        if z <= 0:
            raise ValueError("Стороны квадрата должны быть больше нуля")
        self.z = z

    @property
    def get_area(self):
        return self.z * self.z

    @property
    def get_pr(self):
        return 4 * self.z
