import pytest

from src.Square import Square


def test_creation_square():
    assert Square(5)


def test_no_creation_square():
    with pytest.raises(ValueError):
        assert Square(-5)


def test_no_creation_square_2():
    with pytest.raises(ValueError):
        assert Square(0)


def test_summ_area_6(rectangle):
    square = Square(7)
    assert square.add_area(rectangle) == square.get_area + rectangle.get_area


def test_summ_area_7(triangle):
    square = Square(7)
    assert square.add_area(triangle) == square.get_area + triangle.get_area


def test_summ_area_8(square):
    square = Square(7)
    assert square.add_area(square) == square.get_area + square.get_area


def test_summ_area_9(circle):
    square = Square(7)
    assert square.add_area(circle) == square.get_area + circle.get_area


def test_summ_area_10():
    with pytest.raises(ValueError):
        square = Square(7)
        assert square.add_area("str") == square.get_area + "str".get_area


