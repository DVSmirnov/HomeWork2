class Figure:

    @property
    def get_area(self):
        return True

    @property
    def get_pr(self):
        return True

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Передана не геометрическая фигура")
        return float(self.get_area) + float(figure.get_area)

