########################
# Input Validation     #
########################

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError


@dataclass
class InputValidator:
    """
    Helper class to validate and sanitize calculator inputs.
    """

    @staticmethod
    def validate_number(value: Any, config: CalculatorConfig) -> Decimal:
        """
        Convert input to Decimal and check against limits.

        Args:
            value (Any): The input to validate
            config (CalculatorConfig): Calculator configuration

        Returns:
            Decimal: The validated number

        Raises:
            ValidationError: If the input is not a valid number or exceeds limits
        """
        try:
            # Convert strings to stripped form
            if isinstance(value, str):
                value = value.strip()

            # Convert to Decimal
            number = Decimal(str(value))

            # Check maximum allowed input
            if abs(number) > config.max_input_value:
                raise ValidationError(
                    f"Input {number} exceeds max allowed value ({config.max_input_value})"
                )

            # Normalize the number (remove trailing zeros)
            return number.normalize()

        except InvalidOperation:
            raise ValidationError(f"Invalid number: {value}")