from app.calculator_memento import CalculatorMemento
from app.calculation import Calculation
from datetime import datetime

def test_memento_to_dict_and_from_dict():
    calc_entry = Calculation(1, 2, "add", 3)
    memento = CalculatorMemento(history=[calc_entry])
    d = memento.to_dict()
    assert "history" in d
    assert "timestamp" in d

    m2 = CalculatorMemento.from_dict(d)
    assert len(m2.history) == 1
    assert m2.history[0].operation == "add"