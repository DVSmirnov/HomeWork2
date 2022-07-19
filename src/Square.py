from src.Figure import Figure


class Square(Figure):
    def __init__(self, z):
        self.z = z

    @property
    def get_area(self):
        return self.z * self.z

    @property
    def get_pr(self):
        return 4 * self.z


square = Square(20)
print(square.get_area)
print(square.get_pr)