import pytest
from src.Triangle import Triangle
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square


def test_creation_square():
    assert Square(5)

def test_no_creation_square():
    with pytest.raises(ValueError):
        assert Square(-5)

def test_no_creation_square_2():
    with pytest.raises(ValueError):
        assert Square(0)
