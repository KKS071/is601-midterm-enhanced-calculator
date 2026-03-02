"""
Application entry point for the Advanced Calculator CLI.

This file simply starts the calculator REPL.
"""

from app.calculator import calculator


if __name__ == "__main__":
    # Start the calculator application
    calculator()