"""
Interactive REPL calculator.

Supports:
- add
- subtract
- multiply
- divide

Features:
- Factory pattern for operation creation
- History tracking
- Help command
- Graceful error handling (LBYL + EAFP examples)
"""

import sys
import readline
from typing import List
from app.calculation import Calculation, CalculationFactory


def display_help() -> None:
    """Print usage instructions for the calculator."""
    print(
        """
Calculator Help
---------------
Format:
    <operation> <number1> <number2>

Supported operations:
    add
    subtract
    multiply
    divide

Commands:
    help      Show this message
    history   Show past calculations
    exit      Quit the program

Example:
    add 5 10
"""
    )


def display_history(history: List[Calculation]) -> None:
    """Print calculation history for current session."""
    if len(history) == 0: #pragma: no cover
        print("No calculations yet.\n") 
        return

    print("History:")
    for index, calc in enumerate(history, start=1):
        print(f"{index}. {calc}")
    print()


def _parse_input(user_input: str):
    """
    Attempt to parse user input into operation and operands.
    Demonstrates EAFP style parsing.
    """
    try:
        operation, value1, value2 = user_input.split()
        return operation.lower(), float(value1), float(value2)
    except ValueError: #pragma: no cover
        raise ValueError(
            "Invalid format. Use: <operation> <number1> <number2>"
        )


def calculator() -> None:
    """
    Start the interactive calculator loop.

    Demonstrates:
    - LBYL (checking empty input)
    - EAFP (handling conversion & execution errors)
    """
    history: List[Calculation] = []

    print("Professional Calculator")
    print("Type 'help' for instructions.\n")

    while True:
        try:
            user_input = input(">> ").strip()

            # LBYL: ignore empty input
            if not user_input:
                continue  # pragma: no cover

            command = user_input.lower()

            if command == "help":
                display_help()
                continue

            if command == "history":
                display_history(history)
                continue

            if command == "exit":
                print("Goodbye!\n")
                sys.exit(0)

            # --- Parse Input (EAFP) ---
            try:
                operation, num1, num2 = _parse_input(user_input)
            except ValueError as err: #pragma: no cover
                print(f"{err}\n")
                continue

            # --- Create Calculation via Factory ---
            try:
                calculation = CalculationFactory.create_calculation(
                    operation, num1, num2
                )
            except ValueError as err:
                print(f"{err}")
                print("Type 'help' to see supported operations.\n")
                continue

            # --- Execute Calculation ---
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                print("Error: division by zero is not allowed.\n")
                continue
            except Exception as err:  #pragma: no cover
                print(f"Unexpected error: {err}\n")
                continue

            # Display result
            print(f"Result: {calculation}\n")

            # Save to history
            history.append(calculation)

        except KeyboardInterrupt: #pragma: no cover
            print("\nInterrupted. Exiting...")
            sys.exit(0)
        except EOFError: #pragma: no cover
            print("\nSession ended.")
            sys.exit(0)


if __name__ == "__main__":
    calculator()  # pragma: no cover