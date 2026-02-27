import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition_positive():
    assert addition(2, 3) == 5
    assert addition(0, 0) == 0
    assert addition(2.5, 3.5) == 6.0
    assert addition(-2, 3) == 1

def test_addition_negative():
    assert addition(-2, -3) == -5
    assert addition(-2, 3) == 1
    assert addition(2, -3) == -1
    assert addition(-2.5, -3.5) == -6.0
    assert addition(-2.5, 3.5) == 1.0

def test_subtraction_positive():
    assert subtraction(5, 2) == 3
    assert subtraction(0, 0) == 0
    assert subtraction(5.5, 2.5) == 3.0
    assert subtraction(-5, -2) == -3

def test_subtraction_negative():
    assert subtraction(-5, -2) == -3
    assert subtraction(-5, 2) == -7
    assert subtraction(5, -2) == 7
    assert subtraction(-5.5, -2.5) == -3.0
    assert subtraction(-5.5, 2.5) == -8.0

def test_multiplication_positive():
    assert multiplication(4, 3) == 12
    assert multiplication(0, 5) == 0
    assert multiplication(2.5, 3.5) == 8.75
    assert multiplication(-4, -3) == 12

def test_multiplication_negative():
    assert multiplication(-4, 3) == -12
    assert multiplication(4, -3) == -12
    assert multiplication(-4.5, 3.5) == -15.75
    assert multiplication(4.5, -3.5) == -15.75

def test_division_positive():
    assert division(10, 2) == 5
    assert division(5.5, 2.5) == 2.2
    assert division(-10, -2) == 5

def test_division_negative():
    assert division(-10, 2) == -5
    assert division(10, -2) == -5
    assert division(-10.5, 2.5) == -4.2
    assert division(10.5, -2.5) == -4.2

def test_division_by_zero():
    with pytest.raises(ValueError):
        division(10, 0)
    with pytest.raises(ValueError):
        division(-10, 0)
    with pytest.raises(ValueError):
        division(0, 0)

def test_division_zero_numerator():
    assert division(0, 5) == 0
    assert division(0, -5) == 0

def test_division_floats():
    assert division(5.5, 2.5) == 2.2
    assert division(-5.5, 2.5) == -2.2
    assert division(5.5, -2.5) == -2.2
    assert division(-5.5, -2.5) == 2.2

def test_division_result_precision():
    assert division(1, 3) == pytest.approx(0.3333333333333333)
    assert division(2, 3) == pytest.approx(0.6666666666666666)
    assert division(1, 7) == pytest.approx(0.14285714285714285)
    assert division(1, 9) == pytest.approx(0.1111111111111111)

def test_division_negative_result():
    assert division(-10, 2) == -5
    assert division(10, -2) == -5
    assert division(-10, -2) == 5


