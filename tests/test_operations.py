import pytest
from app.operations import Operation

# -----------------------------
# Test data for addition
# -----------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 5, 4),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ]
)
def test_addition(a, b, expected):
    assert Operation.addition(a, b) == expected

# -----------------------------
# Test data for subtraction
# -----------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 5, -5),
        (-3, -2, -1),
        (2.5, 1.0, 1.5),
    ]
)
def test_subtraction(a, b, expected):
    assert Operation.subtraction(a, b) == expected

# -----------------------------
# Test data for multiplication
# -----------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 5, 0),
        (1.5, 2, 3.0),
    ]
)
def test_multiplication(a, b, expected):
    assert Operation.multiplication(a, b) == expected

# -----------------------------
# Test data for division
# -----------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
        (1.5, 0.5, 3.0),
    ]
)
def test_division(a, b, expected):
    assert Operation.division(a, b) == expected

# -----------------------------
# Division by zero
# -----------------------------
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operation.division(5, 0)

# -----------------------------
# Float precision test
# -----------------------------
def test_division_float_precision():
    result = Operation.division(1, 3)
    assert abs(result - 0.3333333) < 1e-6