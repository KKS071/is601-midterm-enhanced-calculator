########################
# Calculator Operations #
########################

from decimal import Decimal
from app.exceptions import OperationError


class Operation:
    """Base class for all calculator operations."""

    def execute(self, a, b):
        raise NotImplementedError("Execute method not implemented")

    def __str__(self):
        """Return operation name as string."""
        return self.__class__.__name__.lower()


class Add(Operation):
    def execute(self, a, b):
        return float(a + b)

    def __str__(self):
        return "add"


class Subtract(Operation):
    def execute(self, a, b):
        return float(a - b)

    def __str__(self):
        return "subtract"


class Multiply(Operation):
    def execute(self, a, b):
        return float(a * b)

    def __str__(self):
        return "multiply"


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero")
        return float(a / b)

    def __str__(self):
        return "divide"


class Power(Operation):
    def execute(self, a, b):
        return float(a ** b)

    def __str__(self):
        return "power"


class Root(Operation):
    def execute(self, a, b):
        if a < 0 and b % 2 == 0:
            raise OperationError("Cannot take even root of negative number")
        return float(a ** (1 / b))

    def __str__(self):
        return "root"


class Modulus(Operation):
    def execute(self, a, b):
        return float(a % b)

    def __str__(self):
        return "modulus"


class IntDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot integer-divide by zero")
        return float(a // b)

    def __str__(self):
        return "int_divide"


class Percent(Operation):
    def execute(self, a, b):
        return float((a * b) / 100)

    def __str__(self):
        return "percent"


class AbsDiff(Operation):
    def execute(self, a, b):
        return float(abs(a - b))

    def __str__(self):
        return "abs_diff"


class OperationFactory:
    """Factory to create operation instances dynamically."""

    OPERATIONS = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntDivide,
        "percent": Percent,
        "abs_diff": AbsDiff
    }

    @classmethod
    def create_operation(cls, name: str) -> Operation:
        name = name.lower()
        if name not in cls.OPERATIONS:
            raise OperationError(f"Unknown operation: {name}")
        return cls.OPERATIONS[name]()