import pytest
from decimal import Decimal
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.calculation import Calculation
from app.operations import Add
from app.exceptions import OperationError

def test_set_operation_and_perform_operation(tmp_path):
    config = CalculatorConfig(base_dir=tmp_path)
    calc = Calculator(config=config)
    op = Add()
    calc.set_operation(op)
    result = calc.perform_operation(5, 3)
    assert result == 8
    assert len(calc.history) == 1
    entry = calc.history[0]
    assert isinstance(entry, Calculation)

def test_perform_operation_without_operation(tmp_path):
    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    with pytest.raises(OperationError):
        calc.perform_operation(5, 3)

def test_undo_redo(tmp_path):
    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    op = Add()
    calc.set_operation(op)
    calc.perform_operation(2, 3)
    assert len(calc.history) == 1

    assert calc.undo() is True
    assert len(calc.history) == 0
    assert calc.redo() is True
    assert len(calc.history) == 1

def test_history_management(tmp_path):
    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    calc.clear_history()
    assert calc.history == []
    op = Add()
    calc.set_operation(op)
    calc.perform_operation(1, 1)
    calc.save_history()
    calc.load_history()
    assert len(calc.history) == 1