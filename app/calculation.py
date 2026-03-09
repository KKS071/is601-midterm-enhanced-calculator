########################
# Calculation Class
########################

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict


@dataclass
class Calculation:
    """
    Represents a single calculator operation.

    Stores the operands, operation type, result, and timestamp.
    Used by Calculator to track history.
    """

    operand1: Any
    operand2: Any
    operation: str
    result: float = None  # Store numeric result as float
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Calculation instance to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary suitable for CSV or JSON serialization
        """
        return {
            "operand1": str(self.operand1),
            "operand2": str(self.operand2),
            "operation": self.operation,
            "result": str(self.result),
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Calculation":
        """
        Create a Calculation instance from a dictionary.

        Args:
            data (Dict[str, Any]): Dictionary containing keys:
                operand1, operand2, operation, result, timestamp

        Returns:
            Calculation: Restored Calculation object
        """
        return cls(
            operand1=data["operand1"],
            operand2=data["operand2"],
            operation=data["operation"],
            result=float(data["result"]),
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )