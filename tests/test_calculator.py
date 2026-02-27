#Test cases for calculator functionality:
import sys
import unittest
from app.calculator import calculator
#Using monkeypatch to simulate user input for REPL testing
from unittest.mock import patch
from io import StringIO

#Simulates user input for the calculator REPL and captures the output for verification

def run_calculator_with_input(monkeypatch, inputs):
    inputs = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    #Reset stdout
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

def test_addition(monkeypatch):
    inputs = ['add 2 3', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_subtraction(monkeypatch):
    inputs = ['subtract 5 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_multiplication(monkeypatch):
    inputs = ['multiply 4 3', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 12.0" in output

def test_division(monkeypatch):
    inputs = ['divide 10 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_division_by_zero(monkeypatch):
    inputs = ['divide 10 0', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: Division by zero is not allowed." in output

def test_invalid_operation(monkeypatch):
    inputs = ['modulo 10 3', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation. Please try again." in output

def test_invalid_input_format(monkeypatch):
    inputs = ['add 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input format. Please try again." in output

def test_exit(monkeypatch):
    inputs = ['exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Goodbye!" in output

def test_decimal_input(monkeypatch):
    inputs = ['add 2.5 3.5', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6.0" in output

def test_negative_numbers(monkeypatch):
    inputs = ['subtract -5 -2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: -3.0" in output
