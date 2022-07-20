import pytest
from math import *
from src.Triangle import Triangle
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square

def test_creation_rectangle():
    assert Rectangle(5, 5)

def test_creation_rectangle_2():
        assert Rectangle(5, 10)


def test_no_creation_rectangle():
    with pytest.raises(ValueError):
        assert Rectangle(5, -5)

def test_no_creation_rectangle_2():
    with pytest.raises(ValueError):
        assert Rectangle(5, 0)
