import pytest
from math import *

from src.Circle import Circle


def test_creation_circle():
    assert Circle(5)


def test_no_creation_circle():
    with pytest.raises(ValueError):
        Circle(-5)


def test_no_creation_circle_2():
    with pytest.raises(ValueError):
        Circle(0)


def test_summ_area(rectangle):
    circle = Circle(10)
    assert circle.add_area(rectangle) == circle.get_area + rectangle.get_area


def test_summ_area_2(triangle):
    circle = Circle(10)
    assert circle.add_area(triangle) == circle.get_area + triangle.get_area


def test_summ_area_3(square):
    circle = Circle(10)
    assert circle.add_area(square) == circle.get_area + square.get_area


def test_summ_area_4(circle):
    circle = Circle(10)
    assert circle.add_area(circle) == circle.get_area + circle.get_area


def test_summ_area_5():
    with pytest.raises(ValueError):
        circle = Circle(10)
        assert circle.add_area("str") == circle.get_area + "str".get_area
