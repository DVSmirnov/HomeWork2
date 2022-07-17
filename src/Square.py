from src.Figure import Figure

class Square(Figure):
    def __init__(self, z):
        self.z = z

    def get_area(self):
        return self.z * self.z

    def get_pr(self):
        return 4 * self.z