import pytest
from decimal import Decimal
from app.input_validators import InputValidator
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError

def test_validate_number_valid(tmp_path):
    config = CalculatorConfig(base_dir=tmp_path)
    validator = InputValidator()
    assert validator.validate_number(5, config) == Decimal(5)
    assert validator.validate_number(" 3.5 ", config) == Decimal("3.5")

def test_validate_number_invalid(tmp_path):
    config = CalculatorConfig(base_dir=tmp_path)
    validator = InputValidator()
    with pytest.raises(ValidationError):
        validator.validate_number("abc", config)
    with pytest.raises(ValidationError):
        validator.validate_number(config.max_input_value * 2, config)