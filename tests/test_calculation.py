import pytest
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)
from app.operations import Operation

# -----------------------------
# Test data for parameterized tests
# -----------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 8),          # Add positive numbers
        (-2, 2, 0),         # Add negative and positive
        (0, 0, 0),          # Add zeros
        (1.5, 2.5, 4.0),    # Add floats
    ]
)
def test_addition(a, b, expected):
    calc = AddCalculation(a, b)
    assert calc.execute() == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (3, 5, -2),
        (0, 0, 0),
        (2.5, 1.5, 1.0),
    ]
)
def test_subtraction(a, b, expected):
    calc = SubtractCalculation(a, b)
    assert calc.execute() == expected

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
    calc = MultiplyCalculation(a, b)
    assert calc.execute() == expected

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
    calc = DivideCalculation(a, b)
    assert calc.execute() == expected

def test_division_by_zero():
    calc = DivideCalculation(5, 0)
    with pytest.raises(ZeroDivisionError):
        calc.execute()

# -----------------------------
# Test CalculationFactory
# -----------------------------
@pytest.mark.parametrize(
    "op_class, op_type",
    [
        (AddCalculation, "add"),
        (SubtractCalculation, "subtract"),
        (MultiplyCalculation, "multiply"),
        (DivideCalculation, "divide"),
    ]
)
def test_factory_creates_correct_instance(op_class, op_type):
    instance = CalculationFactory.create_calculation(op_type, 1, 2)
    assert isinstance(instance, op_class)
    # Also test the execute method works without error (except divide by zero)
    if op_type == "divide":
        instance = CalculationFactory.create_calculation(op_type, 4, 2)
        assert instance.execute() == 2

# -----------------------------
# Test __str__ and __repr__
# -----------------------------
def test_str_and_repr():
    calc = AddCalculation(2, 3)
    s = str(calc)
    r = repr(calc)
    assert "AddCalculation" in s
    assert "a=2" in r
    assert "b=3" in r