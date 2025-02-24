"""
parser.py
Expert-level module for parsing mathematical expressions into callable functions.
"""

import logging
import sympy as sp
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
def parse_func(expression: str) -> Callable[[float], float]:
    """
    Parse a string expression into a callable function.

    :param expression: A string representation of a mathematical function.
    :return: A callable function of one variable.
    """
    try:
        x = sp.Symbol('x')
        func = sp.lambdify(x, sp.sympify(expression), "math")
        return func
    except Exception as e:
        logging.error("Error parsing function", exc_info=True)
        raise e

# Unit test for the parse_func function
def test_parse_func() -> None:
    """Unit test for parse_func."""
    f = parse_func("x**2 + 3*x + 1")
    result = f(2.0)
    expected = 2.0 ** 2 + 3 * 2.0 + 1  # 4 + 6 + 1 = 11
    assert abs(result - expected) < 1e-4, f"Expected {expected}, got {result}"
    print("parser.py: Test passed!")

if __name__ == "__main__":
    test_parse_func()
