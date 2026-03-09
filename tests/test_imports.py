# tests/test_imports.py

import pytest
from app.operations import (
    Operation, Add, Subtract, Multiply, Divide, Power, Root,
    Modulus, IntDivide, Percent, AbsDiff, OperationFactory
)
from app.calculation import Calculation
from app.calculator import Calculator
from app.calculator_memento import CalculatorMemento
from app.input_validators import InputValidator
from app.history import HistoryObserver, LoggingObserver, AutoSaveObserver
from app.exceptions import ValidationError, OperationError, ConfigurationError


def test_operations_import():
    """Ensure all operations exist and inherit from Operation"""
    for cls in [Add, Subtract, Multiply, Divide, Power, Root,
                Modulus, IntDivide, Percent, AbsDiff]:
        op = cls()
        assert isinstance(op, Operation)
        assert hasattr(op, "execute")
        assert callable(op.execute)


def test_factory_import():
    """OperationFactory must return correct instances matching keys"""
    for name in OperationFactory.OPERATIONS:
        op = OperationFactory.create_operation(name)
        # Compare __str__ with factory key
        assert op.__class__.__name__.lower() == name.replace("_", "").lower() or str(op) == name


def test_calculation_import():
    """Ensure Calculation class can be instantiated and converted to dict"""
    calc = Calculation(operand1=1, operand2=2, operation="add", result=3.0)
    d = calc.to_dict()
    assert d["operation"] == "add"
    calc2 = Calculation.from_dict(d)
    assert calc2.result == 3.0


def test_calculator_import():
    """Ensure Calculator class can be instantiated"""
    calc = Calculator()
    assert hasattr(calc, "perform_operation")
    assert hasattr(calc, "set_operation")


def test_calculator_memento_import():
    """Ensure CalculatorMemento can save and restore history"""
    memento = CalculatorMemento(history=[])
    d = memento.to_dict()
    restored = CalculatorMemento.from_dict(d)
    assert isinstance(restored.history, list)


def test_input_validator_import():
    """Ensure InputValidator validates numbers correctly"""
    from decimal import Decimal
    from app.calculator_config import CalculatorConfig

    config = CalculatorConfig()
    val = InputValidator.validate_number("123", config)
    assert isinstance(val, Decimal)


def test_exceptions_import():
    """Ensure custom exceptions inherit from base"""
    for exc in [ValidationError, OperationError, ConfigurationError]:
        assert issubclass(exc, Exception)


def test_history_import():
    """Ensure observers exist and inherit from HistoryObserver"""
    # Instantiate LoggingObserver correctly
    log_obs = LoggingObserver()
    auto_obs = AutoSaveObserver(Calculator())
    for obs in [log_obs, auto_obs]:
        assert isinstance(obs, HistoryObserver)