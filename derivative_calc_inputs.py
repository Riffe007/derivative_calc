# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:25:21 2023

@author: timot
"""

import sympy as sp

def parse_func(expression: str) -> Callable[[float], float]:
    x = sp.Symbol('x')
    func = sp.lambdify(x, sp.sympify(expression))
    return func

# Test the function
def test_parse_func():
    f = parse_func("x**2 + 3*x + 1")
    assert abs(f(2.0) - 9.0) < 1e-4
    print("Test passed!")
    
test_parse_func()
