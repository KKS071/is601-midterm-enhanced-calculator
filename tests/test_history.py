import logging
from app.history import LoggingObserver, AutoSaveObserver
from app.calculation import Calculation
from unittest.mock import Mock

def test_logging_observer(caplog):
    calc_entry = Calculation(1, 2, "add", 3)
    observer = LoggingObserver()
    with caplog.at_level(logging.INFO):
        observer.update(calc_entry)
        assert "Calculation performed" in caplog.text

def test_autosave_observer(tmp_path):
    class FakeCalculator:
        def __init__(self):
            self.config = Mock(auto_save=True)
            self.save_history = Mock()

    calc_entry = Calculation(1, 2, "add", 3)
    observer = AutoSaveObserver(FakeCalculator())
    observer.update(calc_entry)
    assert observer.calculator.save_history.called