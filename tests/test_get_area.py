from src.Triangle import Triangle
from src.Circle import Circle
from src.Triangle import Rectangle
from src.Triangle import Square

def test_get_area_good1():
    def test_negative_triangle():
        with pytest.raises(ValueError):
            Triangle(12, 13, 26)
