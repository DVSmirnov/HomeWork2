import pytest
from math import *
from src.Triangle import Triangle
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square

def test_creation_circle():
    assert Circle(5)

def test_no_creation_circle():
    assert Circle(-5)

def test_no_creation_circle_2():
    assert Circle(0)