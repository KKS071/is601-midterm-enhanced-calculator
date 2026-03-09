########################
# Calculator Config    #
########################

from dataclasses import dataclass
from decimal import Decimal
from numbers import Number
from pathlib import Path
import os
from typing import Optional

from dotenv import load_dotenv
from app.exceptions import ConfigurationError

# Load environment variables from .env file
load_dotenv()


def get_project_root() -> Path:
    """Return the project root directory (two levels up from this file)."""
    return Path(__file__).parent.parent


@dataclass
class CalculatorConfig:
    """
    Calculator configuration.

    Holds all settings for the calculator like directories, precision,
    history limits, auto-save, and max input values.
    Can read from environment variables or be set manually.
    """

    def __init__(
        self,
        base_dir: Optional[Path] = None,
        max_history_size: Optional[int] = None,
        auto_save: Optional[bool] = None,
        precision: Optional[int] = None,
        max_input_value: Optional[Number] = None,
        default_encoding: Optional[str] = None
    ):
        project_root = get_project_root()

        # Base directory for logs, history, etc.
        self.base_dir = base_dir or Path(
            os.getenv("CALCULATOR_BASE_DIR", str(project_root))
        ).resolve()

        # Max number of calculations in history
        self.max_history_size = max_history_size or int(
            os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "1000")
        )

        # Auto-save history on each calculation
        auto_save_env = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower()
        self.auto_save = auto_save if auto_save is not None else (
            auto_save_env in ("true", "1")
        )

        # Number of decimal places to use in calculations
        self.precision = precision or int(os.getenv("CALCULATOR_PRECISION", "10"))

        # Maximum input value allowed
        self.max_input_value = max_input_value or Decimal(
            os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e999")
        )

        # Default encoding for files
        self.default_encoding = default_encoding or os.getenv(
            "CALCULATOR_DEFAULT_ENCODING", "utf-8"
        )

    @property
    def log_dir(self) -> Path:
        """Directory where log files are stored."""
        return Path(os.getenv(
            "CALCULATOR_LOG_DIR", str(self.base_dir / "logs")
        )).resolve()

    @property
    def history_dir(self) -> Path:
        """Directory where calculation history files are stored."""
        return Path(os.getenv(
            "CALCULATOR_HISTORY_DIR", str(self.base_dir / "history")
        )).resolve()

    @property
    def history_file(self) -> Path:
        """File path for the calculation history CSV."""
        return Path(os.getenv(
            "CALCULATOR_HISTORY_FILE", str(self.history_dir / "calculator_history.csv")
        )).resolve()

    @property
    def log_file(self) -> Path:
        """File path for the log file."""
        return Path(os.getenv(
            "CALCULATOR_LOG_FILE", str(self.log_dir / "calculator.log")
        )).resolve()

    def validate(self) -> None:
        """Validate configuration values."""
        if self.max_history_size <= 0:
            raise ConfigurationError("max_history_size must be positive")
        if self.precision <= 0:
            raise ConfigurationError("precision must be positive")
        if self.max_input_value <= 0:
            raise ConfigurationError("max_input_value must be positive")