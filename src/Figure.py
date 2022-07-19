class Figure:

    @property
    def get_area(self):
        return True

    @property
    def get_pr(self):
        return True

    def add_Area(self, figure):
        return self.get_area + figure.get_area

