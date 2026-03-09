########################
# History Management   #
########################

from abc import ABC, abstractmethod
import logging
from typing import Any
from app.calculation import Calculation


class HistoryObserver(ABC):
    """
    Base class for calculator observers.

    Observers watch for new calculations and react to them.
    Subclasses must implement the update() method.
    """

    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        """
        Receive notification of a new calculation.

        Args:
            calculation (Calculation): The calculation that was just done.
        """
        pass  # pragma: no cover


class LoggingObserver(HistoryObserver):
    """
    Logs each calculation to the logging system.
    """

    def update(self, calculation: Calculation) -> None:
        if calculation is None:
            raise AttributeError("Calculation cannot be None")

        logging.info(
            f"Calculation performed: {calculation.operation} "
            f"({calculation.operand1}, {calculation.operand2}) = {calculation.result}"
        )


class AutoSaveObserver(HistoryObserver):
    """
    Automatically saves calculator history when a new calculation occurs.
    """

    def __init__(self, calculator: Any):
        # Ensure the calculator has the required attributes
        if not hasattr(calculator, 'config') or not hasattr(calculator, 'save_history'):
            raise TypeError("Calculator must have 'config' and 'save_history' attributes")

        self.calculator = calculator

    def update(self, calculation: Calculation) -> None:
        if calculation is None:
            raise AttributeError("Calculation cannot be None")

        if getattr(self.calculator.config, 'auto_save', False):
            # Save history if auto-save is enabled
            self.calculator.save_history()
            logging.info("History auto-saved")