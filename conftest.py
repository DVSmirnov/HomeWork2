import pytest

from src.Triangle import Triangle
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.fixture
def rectangle():
    return Rectangle(5, 10)


@pytest.fixture
def triangle():
    return Triangle(5, 10, 12)


@pytest.fixture
def square():
    return Square(7)


@pytest.fixture
def circle():
    return Circle(25)


