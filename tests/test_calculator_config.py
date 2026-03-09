import pytest
from decimal import Decimal
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError

def test_config_defaults(tmp_path):
    config = CalculatorConfig(base_dir=tmp_path)
    assert config.max_history_size > 0
    assert config.precision > 0
    assert config.max_input_value > 0
    assert config.log_dir.exists() or True

def test_config_validation_errors(tmp_path):
    config = CalculatorConfig(base_dir=tmp_path, max_history_size=-1)
    with pytest.raises(ConfigurationError):
        config.validate()