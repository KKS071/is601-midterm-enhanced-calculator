from datetime import datetime
from app.calculation import Calculation

def test_to_dict_and_from_dict():
    calc = Calculation(operand1=5, operand2=3, operation="add", result=8)
    d = calc.to_dict()
    assert d["operand1"] == "5"
    assert d["operand2"] == "3"
    assert d["operation"] == "add"
    assert d["result"] == "8"
    assert "timestamp" in d

    calc2 = Calculation.from_dict(d)
    assert calc2.operand1 == "5"
    assert calc2.operand2 == "3"
    assert calc2.operation == "add"
    assert calc2.result == 8.0
    assert isinstance(calc2.timestamp, datetime)