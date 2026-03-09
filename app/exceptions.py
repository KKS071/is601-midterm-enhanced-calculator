########################
# Exception Hierarchy  #
########################

class CalculatorError(Exception):
    """
    Base exception for the calculator.

    All custom calculator exceptions inherit from this class.
    """
    pass


class ValidationError(CalculatorError):
    """
    Raised when input validation fails.

    Examples:
        - Non-numeric input
        - Input exceeding maximum allowed value
    """
    pass


class OperationError(CalculatorError):
    """
    Raised when a calculation operation fails.

    Examples:
        - Division by zero
        - Invalid root or negative exponent
    """
    pass


class ConfigurationError(CalculatorError):
    """
    Raised when calculator configuration is invalid.

    Examples:
        - Negative max history size
        - Invalid precision or input limits
    """
    pass