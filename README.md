# derivative_calc
derivative calculator with slider inputs
# Derivative Calculator
This app allows you to compute the derivative of a function at a given point using the finite difference method. You can input the function and the value of the derivative using sliders or by typing in an expression.

# Requirements
Python 3.6 or higher
PyQt5
SymPy (optional, for typed input of functions)
# Usage
To run the app, simply run the following command:

Copy code
python derivative_calculator.py
The app will open a graphical user interface with two sliders, one for the function and one for the value of the derivative, and a button to compute the derivative. You can adjust the sliders to change the function and the value of the derivative, and then click the "Compute derivative" button to compute the derivative. The result will be displayed in the result label.

You can also input the function as a typed expression by clicking the "Type expression" button. This will open a dialog box where you can type in the expression for the function. The function label will update to show the expression, and you can use the slider to adjust the value of the derivative as usual.

# Examples
Here are some examples of functions you can use with the app:

Linear function: f(x) = 2*x + 1
Quadratic function: f(x) = x^2 + 2*x + 1
Exponential function: f(x) = 2^x
# Limitations
The finite difference method is a simple and general method for approximating derivatives, but it can be less accurate for functions with rapid changes or for values of the derivative that are far from the center point. The step size h used in the approximation can be adjusted to improve the accuracy, but a smaller step size will increase the computation time.





