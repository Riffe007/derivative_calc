# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:03:32 2023

@author: timot
"""

from typing import Callable

def derivative(func: Callable[[float], float], x: float, h: float = 1e-4) -> float:
    return (func(x+h) - func(x)) / h

# Test the function
def test_derivative():
    def f(x: float) -> float:
        return x**2
    assert abs(derivative(f, 2.0) - 4.0) < 1e-4
    print("Test passed!")
    
test_derivative()
