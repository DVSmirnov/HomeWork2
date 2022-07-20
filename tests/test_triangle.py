import pytest
from math import *

from src.Triangle import Triangle


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

def test_summ_area_11(rectangle):
    triangle = Triangle(2, 5, 4)
    assert triangle.add_area(rectangle) == triangle.get_area + rectangle.get_area


def test_summ_area_12(triangle):
    triangle = Triangle(2, 5, 4)
    assert triangle.add_area(triangle) == triangle.get_area + triangle.get_area


def test_summ_area_13(square):
    triangle = Triangle(2, 5, 4)
    assert triangle.add_area(square) == triangle.get_area + square.get_area


def test_summ_area_14(circle):
    triangle = Triangle(2, 5, 4)
    assert triangle.add_area(circle) == triangle.get_area + circle.get_area


def test_summ_area_15():
    with pytest.raises(ValueError):
        triangle = Triangle(2, 5, 4)
        assert triangle.add_area("str") == triangle.get_area + "str".get_area
