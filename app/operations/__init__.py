"""
Utility module containing basic arithmetic operations.

All methods are static because they do not depend on any
instance-specific state. They simply take inputs and return results.
"""


class Operation:
    """
    Provides basic arithmetic operations used by the calculator.

    Keeping these operations separate from Calculation classes
    helps maintain clean separation of concerns.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Return the result of subtracting b from a."""
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Return the result of dividing a by b.

        """
        return a / b