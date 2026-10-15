def _validate_inputs(a: int, b: int) -> None:
    """Ensure both inputs are positive integers."""
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Inputs must be integers.")
        if value <= 0:
            raise ValueError("Inputs must be positive integers.")


def add(a: int, b: int) -> int:
    _validate_inputs(a, b)
    return a + b


def subtract(a: int, b: int) -> int:
    _validate_inputs(a, b)
    return a - b


def multiply(a: int, b: int) -> int:
    _validate_inputs(a, b)
    return a * b
