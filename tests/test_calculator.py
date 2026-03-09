import pytest
from decimal import Decimal
from pathlib import Path
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.calculation import Calculation
from app.operations import Add, Subtract
from app.exceptions import OperationError
from app.history import HistoryObserver
import pandas as pd

# ----------------- Basic Operations -----------------

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

# ----------------- Undo / Redo -----------------

def test_undo_redo(tmp_path):
    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    op = Add()
    calc.set_operation(op)
    calc.perform_operation(2, 3)
    assert len(calc.history) == 1

    # Undo
    assert calc.undo() is True
    assert len(calc.history) == 0
    # Redo
    assert calc.redo() is True
    assert len(calc.history) == 1
    # Edge cases: nothing to undo/redo
    calc.undo_stack.clear()
    calc.redo_stack.clear()
    assert calc.undo() is False
    assert calc.redo() is False

# ----------------- History Management -----------------

def test_history_management(tmp_path):
    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    calc.clear_history()
    assert calc.history == []

    op = Add()
    calc.set_operation(op)
    calc.perform_operation(1, 1)

    # Save / Load history
    calc.save_history()
    calc.load_history()
    assert len(calc.history) == 1
    entry = calc.history[0]
    assert isinstance(entry, Calculation)

# ----------------- Observer Notification -----------------

def test_notify_observer(tmp_path):
    class DummyObserver(HistoryObserver):
        def __init__(self):
            self.called = False
        def update(self, calculation):
            self.called = True

    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    observer = DummyObserver()
    calc.add_observer(observer)

    op = Add()
    calc.set_operation(op)
    calc.perform_operation(1, 2)
    assert observer.called

# ----------------- History Size Limit -----------------

def test_history_size_limit(tmp_path):
    cfg = CalculatorConfig(base_dir=tmp_path, max_history_size=2)
    calc = Calculator(cfg)
    op = Add()
    calc.set_operation(op)
    calc.perform_operation(1, 1)
    calc.perform_operation(2, 2)
    calc.perform_operation(3, 3)
    assert len(calc.history) == 2  # oldest should be removed
    assert calc.history[0].result == 4  # second operation remains
    assert calc.history[1].result == 6  # last operation

# ----------------- Load History Failure -----------------

def test_load_history_failure(monkeypatch, tmp_path):
    config = CalculatorConfig(base_dir=tmp_path)
    calc = Calculator(config=config)

    # create dummy history file so load_history tries to read it
    config.history_file.write_text("dummy")

    def mock_read_csv(*args, **kwargs):
        raise Exception("fail")

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)
    with pytest.raises(OperationError):
        calc.load_history()

# ----------------- Multiple Operations -----------------

def test_different_operations(tmp_path):
    calc = Calculator(config=CalculatorConfig(base_dir=tmp_path))
    
    add_op = Add()
    calc.set_operation(add_op)
    assert calc.perform_operation(2, 3) == 5
    
    sub_op = Subtract()
    calc.set_operation(sub_op)
    assert calc.perform_operation(5, 2) == 3