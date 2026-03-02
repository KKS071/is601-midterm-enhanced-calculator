# tests/test_imports.py

import pytest

# Import directly from the packages since all code is in __init__.py
from app.operations import Operation
from app.calculation import (
    Calculation,
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation
)
from app.calculator import calculator, display_help, display_history


def test_operations_import():
    assert hasattr(Operation, "addition")
    assert hasattr(Operation, "subtraction")
    assert hasattr(Operation, "multiplication")
    assert hasattr(Operation, "division")


def test_calculation_imports():
    # Test that all calculation classes exist
    for cls in [
        Calculation,
        CalculationFactory,
        AddCalculation,
        SubtractCalculation,
        MultiplyCalculation,
        DivideCalculation,
    ]:
        assert cls is not None


def test_calculator_imports():
    # Test that the main functions exist
    assert callable(calculator)
    assert callable(display_help)
    assert callable(display_history)