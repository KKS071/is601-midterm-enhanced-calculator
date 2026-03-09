########################
# Calculator REPL       #
########################

from decimal import Decimal
from colorama import Fore, Style, init
import logging

from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.history import LoggingObserver, AutoSaveObserver
from app.operations import OperationFactory

# Initialize colorama
init(autoreset=True)

COMMANDS = [
    "add", "subtract", "multiply", "divide", "power", "root",
    "modulus", "int_divide", "percent", "abs_diff",
    "history", "clear", "undo", "redo", "save", "load", "help", "exit"
]

def calculator_repl(): # pragma: no cover
    """Command-line interface for the calculator."""

    calc = Calculator()
    calc.add_observer(LoggingObserver())
    calc.add_observer(AutoSaveObserver(calc))

    print(Fore.GREEN + "Calculator started. Type 'help' for commands.")

    while True:
        try:
            command = input(Fore.CYAN + "\nEnter command: " + Style.RESET_ALL).strip().lower()

            if command == "help":
                print(Fore.YELLOW + "Available commands:")
                for cmd in COMMANDS:
                    print(Fore.YELLOW + f"  {cmd}")
                continue

            if command == "exit":
                try:
                    calc.save_history()
                    print(Fore.GREEN + "History saved successfully.")
                except Exception as e:
                    print(Fore.RED + f"Warning: Could not save history: {e}")
                print(Fore.GREEN + "Goodbye!")
                break

            if command == "history":
                history = calc.show_history()
                if not history:
                    print("No calculations in history")
                else:
                    print("\nCalculation History:")
                    for i, entry in enumerate(history, 1):
                        print(f"{i}. {entry}")
                continue

            if command == "clear":
                calc.clear_history()
                print("History cleared")
                continue

            if command == "undo":
                if calc.undo():
                    print("Operation undone")
                else:
                    print("Nothing to undo")
                continue

            if command == "redo":
                if calc.redo():
                    print("Operation redone")
                else:
                    print("Nothing to redo")
                continue

            if command == "save":
                try:
                    calc.save_history()
                    print("History saved successfully")
                except Exception as e:
                    print(f"Error saving history: {e}")
                continue

            if command == "load":
                try:
                    calc.load_history()
                    print("History loaded successfully")
                except Exception as e:
                    print(f"Error loading history: {e}")
                continue

            if command in OperationFactory.OPERATIONS:
                try:
                    a = input("First number: ")
                    if a.lower() == "cancel":
                        print("Operation cancelled")
                        continue
                    b = input("Second number: ")
                    if b.lower() == "cancel":
                        print("Operation cancelled")
                        continue

                    operation = OperationFactory.create_operation(command)
                    calc.set_operation(operation)
                    result = calc.perform_operation(a, b)

                    print(Fore.GREEN + f"\nResult: {result}")

                except (ValidationError, OperationError) as e:
                    print(Fore.RED + f"Error: {e}")
                continue

            print(Fore.RED + f"Unknown command: '{command}'. Type 'help' for available commands.")

        except (KeyboardInterrupt, EOFError):
            print("\nInput terminated. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")