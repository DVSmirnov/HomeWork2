import pytest
from math import *

from src.Rectangle import Rectangle


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


def test_summ_area_16(rectangle):
    rectangle = Rectangle(2, 5)
    assert rectangle.add_area(rectangle) == rectangle.get_area + rectangle.get_area


def test_summ_area_17(triangle):
    rectangle = Rectangle(2, 5)
    assert rectangle.add_area(triangle) == rectangle.get_area + triangle.get_area


def test_summ_area_18(square):
    rectangle = Rectangle(2, 5)
    assert rectangle.add_area(square) == rectangle.get_area + square.get_area


def test_summ_area_19(circle):
    rectangle = Rectangle(2, 5)
    assert rectangle.add_area(circle) == rectangle.get_area + circle.get_area


def test_summ_area_20():
    with pytest.raises(ValueError):
        rectangle = Rectangle(2, 5)
        assert rectangle.add_area("str") == rectangle.get_area + "str".get_area
