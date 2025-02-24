"""
calculus.py
Expert-level module for calculus operations.
"""

import logging
from typing import Callable

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_call(func: Callable) -> Callable:
    """Decorator to log function calls and results."""
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def derivative(func: Callable[[float], float], x: float, h: float = 1e-4) -> float:
    """
    Compute the numerical derivative of a function at a given point.

    Expected derivative formula: (f(x+h) - f(x)) / h

    :param func: The function to differentiate.
    :param x: The point at which the derivative is evaluated.
    :param h: A small increment for computing the derivative.
    :return: The numerical derivative.
    """
    try:
        return (func(x + h) - func(x)) / h
    except Exception as e:
        logging.error("Error computing derivative", exc_info=True)
        raise e

# Unit test for the derivative function
def test_derivative() -> None:
    """Unit test for derivative."""
    def square(x: float) -> float:
        return x ** 2
    result = derivative(square, 2.0)
    expected = 4.0  # derivative of x^2 at x=2 is 4
    assert abs(result - expected) < 1e-4, f"Expected {expected}, got {result}"
    print("calculus.py: Test passed!")

if __name__ == "__main__":
    test_derivative()
