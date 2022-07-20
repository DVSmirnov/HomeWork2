class Figure:

    @property
    def get_area(self):
        return True

    @property
    def get_pr(self):
        return True

    def add_area(self, figure):
        isinstance(figure, Figure)
            raise ValueError("Передана не геометрическая фигура")
        return self.get_area + figure.get_area

