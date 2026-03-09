import pytest
from app.exceptions import ValidationError, OperationError, ConfigurationError

def test_exceptions_inheritance():
    with pytest.raises(ValidationError):
        raise ValidationError("Test validation")
    with pytest.raises(OperationError):
        raise OperationError("Test operation")
    with pytest.raises(ConfigurationError):
        raise ConfigurationError("Test config")