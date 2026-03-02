# tests/test_calculator.py

import pytest
from unittest.mock import patch
from app.calculator import calculator, display_help, display_history
from app.calculation import AddCalculation, SubtractCalculation, MultiplyCalculation, DivideCalculation


def test_display_help(capsys):
    display_help()
    captured = capsys.readouterr()
    assert "Calculator Help" in captured.out
    # Update expected example to match actual help
    assert "add 5 10" in captured.out


@pytest.mark.parametrize(
    "inputs, expected_outputs",
    [
        (["add 2 3", "exit"], ["Result: AddCalculation: 2.0 Add 3.0 = 5.0"]),
        (["subtract 5 2", "exit"], ["Result: SubtractCalculation: 5.0 Subtract 2.0 = 3.0"]),
        (["multiply 3 4", "exit"], ["Result: MultiplyCalculation: 3.0 Multiply 4.0 = 12.0"]),
        (["divide 6 2", "exit"], ["Result: DivideCalculation: 6.0 Divide 2.0 = 3.0"]),
    ]
)
def test_calculator_basic_operations(inputs, expected_outputs, capsys):
    with patch("builtins.input", side_effect=inputs):
        with pytest.raises(SystemExit):
            calculator()
    captured = capsys.readouterr()
    for expected in expected_outputs:
        assert expected in captured.out


def test_calculator_divide_by_zero(capsys):
    inputs = ["divide 10 0", "exit"]
    with patch("builtins.input", side_effect=inputs):
        with pytest.raises(SystemExit):
            calculator()
    captured = capsys.readouterr()
    # Updated to match actual message
    assert "Error: division by zero is not allowed." in captured.out


def test_calculator_unknown_command(capsys):
    inputs = ["foobar 1 2", "exit"]
    with patch("builtins.input", side_effect=inputs):
        with pytest.raises(SystemExit):
            calculator()
    captured = capsys.readouterr()
    assert "Unsupported calculation type" in captured.out


def test_calculator_help_and_history(capsys):
    inputs = ["add 1 1", "history", "help", "exit"]
    with patch("builtins.input", side_effect=inputs):
        with pytest.raises(SystemExit):
            calculator()
    captured = capsys.readouterr()
    # Check that history shows the calculation
    assert "1. AddCalculation" in captured.out
    # Check that help content is printed
    assert "Calculator Help" in captured.out
    # Update expected example to match actual help
    assert "add 5 10" in captured.out