########################
# Calculator Class      #
########################

from decimal import Decimal
import logging
import os
from pathlib import Path
from typing import List, Optional, Union

import pandas as pd

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.exceptions import OperationError, ValidationError
from app.history import HistoryObserver
from app.input_validators import InputValidator
from app.operations import Operation

# Type aliases
Number = Union[int, float, Decimal]


class Calculator:
    """
    Core calculator class implementing Strategy, Observer, and Memento patterns.
    """

    def __init__(self, config: Optional[CalculatorConfig] = None):
        if config is None:
            project_root = Path(__file__).parent.parent
            config = CalculatorConfig(base_dir=project_root)

        self.config = config
        self.config.validate()

        os.makedirs(self.config.log_dir, exist_ok=True)
        self._setup_logging()
        self.history: List[Calculation] = []
        self.operation: Optional[Operation] = None
        self.observers: List[HistoryObserver] = []
        self.undo_stack: List[CalculatorMemento] = []
        self.redo_stack: List[CalculatorMemento] = []
        self.validator = InputValidator()

        os.makedirs(self.config.history_dir, exist_ok=True)

        try:
            self.load_history()
        except Exception as e:
            logging.warning(f"Could not load history: {e}")

        logging.info("Calculator initialized")

    def _setup_logging(self):
        log_file = self.config.log_file
        logging.basicConfig(
            filename=str(log_file),
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True,
        )
        logging.info(f"Logging initialized at: {log_file}")

    def add_observer(self, observer: HistoryObserver):
        self.observers.append(observer)
        logging.info(f"Added observer: {observer.__class__.__name__}")

    def remove_observer(self, observer: HistoryObserver):
        if observer in self.observers:
            self.observers.remove(observer)
            logging.info(f"Removed observer: {observer.__class__.__name__}")

    def notify_observers(self, calculation: Calculation):
        for observer in self.observers:
            observer.update(calculation)

    def set_operation(self, operation: Operation):
        self.operation = operation
        logging.info(f"Set operation: {operation}")

    def perform_operation(self, a: Union[str, Number], b: Union[str, Number]) -> float:
        """
        Perform the currently set operation on validated operands.
        Returns float result.
        """
        if not self.operation:
            raise OperationError("No operation set")

        # Validate and convert inputs
        num1 = self.validator.validate_number(a, self.config)
        num2 = self.validator.validate_number(b, self.config)

        try:
            result = self.operation.execute(num1, num2)
        except Exception as e:
            raise OperationError(f"Operation failed: {e}") from e

        # Store in history
        calculation = Calculation(
            operand1=num1,
            operand2=num2,
            operation=str(self.operation),
            result=float(result)
        )
        self._add_to_history(calculation)
        return float(result)

    def _add_to_history(self, calculation: Calculation):
        # Save current state for undo
        self.undo_stack.append(CalculatorMemento(self.history.copy()))
        self.redo_stack.clear()
        self.history.append(calculation)
        # Limit history size
        if len(self.history) > self.config.max_history_size:
            self.history.pop(0)
        self.notify_observers(calculation)

    # ---------------- History Management ----------------

    def save_history(self):
        try:
            os.makedirs(self.config.history_dir, exist_ok=True)
            data = [
                {
                    "operation": calc.operation,
                    "operand1": str(calc.operand1),
                    "operand2": str(calc.operand2),
                    "result": str(calc.result),
                    "timestamp": calc.timestamp.isoformat(),
                }
                for calc in self.history
            ]
            df = pd.DataFrame(data)
            df.to_csv(self.config.history_file, index=False)
            logging.info(f"History saved to {self.config.history_file}")
        except Exception as e:
            logging.error(f"Failed to save history: {e}")
            raise OperationError(f"Failed to save history: {e}")

    def load_history(self):
        try:
            if self.config.history_file.exists():
                df = pd.read_csv(self.config.history_file)
                self.history = [
                    Calculation.from_dict({
                        "operation": row["operation"],
                        "operand1": row["operand1"],
                        "operand2": row["operand2"],
                        "result": row["result"],
                        "timestamp": row["timestamp"]
                    })
                    for _, row in df.iterrows()
                ]
                logging.info(f"Loaded {len(self.history)} calculations from history")
        except Exception as e:
            logging.error(f"Failed to load history: {e}")
            raise OperationError(f"Failed to load history: {e}")

    def show_history(self) -> List[str]:
        return [
            f"{calc.operation}({calc.operand1}, {calc.operand2}) = {calc.result}"
            for calc in self.history
        ]

    def clear_history(self):
        self.history.clear()
        self.undo_stack.clear()
        self.redo_stack.clear()
        logging.info("History cleared")

    # ---------------- Undo / Redo ----------------

    def undo(self) -> bool:
        if not self.undo_stack:
            return False
        memento = self.undo_stack.pop()
        self.redo_stack.append(CalculatorMemento(self.history.copy()))
        self.history = memento.history.copy()
        return True

    def redo(self) -> bool:
        if not self.redo_stack:
            return False
        memento = self.redo_stack.pop()
        self.undo_stack.append(CalculatorMemento(self.history.copy()))
        self.history = memento.history.copy()
        return True