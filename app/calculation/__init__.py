"""
Core calculation classes for the calculator application.

Implements:
- Abstract base class for calculations
- Factory pattern for dynamic creation
- Concrete classes for add, subtract, multiply, divide

Each operation delegates arithmetic to the Operation module.
"""

from abc import ABC, abstractmethod
from app.operations import Operation


# ------------------------------------------------------------------
# Base Calculation Class
# ------------------------------------------------------------------

class Calculation(ABC):
    """
    Abstract base class for all calculator operations.

    Every calculation stores two operands and must implement execute().
    """

    def __init__(self, a: float, b: float) -> None:
        # store operands as instance state
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        """
        Perform the calculation.

        Subclasses must implement this method.
        """
        pass  # pragma: no cover

    def __str__(self) -> str:
        """
        Human-readable representation of the calculation.
        """
        result = self.execute()
        operation_name = self.__class__.__name__.replace("Calculation", "")
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


# ------------------------------------------------------------------
# Factory
# ------------------------------------------------------------------

class CalculationFactory:
    """
    Factory responsible for creating calculation objects.

    Uses decorator-based registration so new calculations
    can be added without modifying factory logic.
    """

    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """
        Decorator used to register calculation subclasses.
        """

        def decorator(subclass):
            key = calculation_type.lower()

            if key in cls._calculations: #pragma: no cover
                raise ValueError(
                    f"Calculation type '{calculation_type}' is already registered."
                )

            cls._calculations[key] = subclass
            return subclass

        return decorator

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        """
        Create a calculation instance based on its string type.
        """
        key = calculation_type.lower()
        calculation_class = cls._calculations.get(key)

        if calculation_class is None:
            available = ", ".join(cls._calculations.keys())
            raise ValueError(
                f"Unsupported calculation type: '{calculation_type}'. "
                f"Available types: {available}"
            )

        return calculation_class(a, b)


# ------------------------------------------------------------------
# Concrete Calculations
# ------------------------------------------------------------------

@CalculationFactory.register_calculation("add")
class AddCalculation(Calculation):
    """Handles addition."""

    def execute(self) -> float:
        return Operation.addition(self.a, self.b)


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    """Handles subtraction."""

    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    """Handles multiplication."""

    def execute(self) -> float:
        return Operation.multiplication(self.a, self.b)


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    """Handles division with zero check."""

    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Operation.division(self.a, self.b)