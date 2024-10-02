def divide(a, b):
    """Divides first number by the second. Raises an error if division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b