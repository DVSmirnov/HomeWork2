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


def test_negative_triangle():
    with pytest.raises(ValueError):
        Triangle(10, 10, -10)


def test_negative_triangle_2():
    with pytest.raises(ValueError):
        Triangle(10, 10, 0)
