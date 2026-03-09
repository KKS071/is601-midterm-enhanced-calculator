########################
# Calculator Memento   #
########################

from dataclasses import dataclass, field
from typing import Any, Dict, List
import datetime

from app.calculation import Calculation


@dataclass
class CalculatorMemento:
    """
    Memento class to save the calculator's history for undo/redo.

    Stores a snapshot of the calculator's history at a certain point in time.
    """

    history: List[Calculation]  # Current calculator history
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize memento to dictionary.

        Returns:
            Dict[str, Any]: Dictionary with history and timestamp.
        """
        return {
            'history': [calc.to_dict() for calc in self.history],
            'timestamp': self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CalculatorMemento':
        """
        Deserialize memento from dictionary.

        Args:
            data (Dict[str, Any]): Dictionary containing memento data.

        Returns:
            CalculatorMemento: Reconstructed memento instance.
        """
        history_data = data.get('history', [])
        calculations = [Calculation.from_dict(c) for c in history_data]
        ts_str = data.get('timestamp', datetime.datetime.now().isoformat())
        return cls(history=calculations, timestamp=datetime.datetime.fromisoformat(ts_str))