import pytest
from decimal import Decimal
from app.operations import (
    Add, Subtract, Multiply, Divide, Power, Root, Modulus, IntDivide,
    Percent, AbsDiff, OperationFactory, Operation
)
from app.exceptions import OperationError

@pytest.mark.parametrize("op_class,a,b,expected", [
    (Add, 5, 3, 8),
    (Subtract, 5, 3, 2),
    (Multiply, 5, 3, 15),
    (Divide, 6, 3, 2),
    (Power, 2, 3, 8),
    (Root, 9, 2, 3),
    (Modulus, 5, 3, 2),
    (IntDivide, 7, 3, 2),
    (Percent, 50, 10, 5),
    (AbsDiff, 5, 10, 5),
])
def test_operation_execute(op_class, a, b, expected):
    op = op_class()
    result = op.execute(a, b)
    assert result == expected

def test_divide_by_zero():
    op = Divide()
    with pytest.raises(OperationError):
        op.execute(5, 0)

def test_root_even_negative_error():
    op = Root()
    with pytest.raises(OperationError):
        op.execute(-4, 2)

def test_int_divide_by_zero():
    op = IntDivide()
    with pytest.raises(OperationError):
        op.execute(5, 0)

def test_factory_create_known_operations():
    for name, cls in OperationFactory.OPERATIONS.items():
        op = OperationFactory.create_operation(name)
        assert isinstance(op, cls)

def test_factory_create_unknown_operation():
    with pytest.raises(OperationError):
        OperationFactory.create_operation("unknown_op")