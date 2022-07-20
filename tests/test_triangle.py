import pytest
from math import *
from src.Triangle import Triangle
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square


def test_creation_triangle():
    assert Triangle(5, 15, 12)


def test_no_creation_triangle():
    with pytest.raises(ValueError):
        Triangle(5, 15, 25)


def test_equilateral_triangle():
    assert Triangle(10, 10, 10)


def test_right_triangle():
    assert 9.433981132056603 == sqrt((5 ** 2) + (8 ** 2))


def test_negative_triangle():
    assert Triangle(10, 10, -10)


def test_negative_triangle_2():
    assert Triangle(10, 10, 0)
