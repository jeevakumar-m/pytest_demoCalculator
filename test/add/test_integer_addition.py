import pytest

from src.calculator import Calculator

math = Calculator()


def test_addition_integer():
    a = math.calculate(1, 2, "add")
    assert a == 3


def test_addition_integer_num1_below_lowerBoundary():
    with pytest.raises(Exception) as info:
        a = math.calculate(-1, 2, "add")


def test_addition_integer_num1_above_upper_Boundary():
    with pytest.raises(Exception) as info:
        a = math.calculate(1001, 2, "add")


def test_addition_integer_num2_below_lowerBoundary():
    with pytest.raises(Exception) as info:
        a = math.calculate(1, -1, "add")


def test_addition_integer_num2_above_upper_Boundary():
    with pytest.raises(Exception) as info:
        a = math.calculate(1, 1001, "add")
