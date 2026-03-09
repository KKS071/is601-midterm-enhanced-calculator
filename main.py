########################
# Main Application     #
########################

"""
Application entry point for the Advanced Calculator CLI.

This file starts the calculator REPL with all supported operations.
"""

from app.calculator_repl import calculator_repl

if __name__ == "__main__":
    # Start the calculator REPL
    calculator_repl()