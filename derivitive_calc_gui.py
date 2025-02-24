"""
gui.py
Expert-level PyQt5 GUI for computing the numerical derivative of a user-defined function.
"""

import sys
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from typing import Callable

# Import our core modules
from calculus import derivative
from parser import parse_func

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

class DerivativeGUI(QWidget):
    """
    PyQt5 GUI for computing the numerical derivative of a function.
    
    The function is defined as f(x) = x^n, where n is set by the slider.
    """
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        
    def initUI(self) -> None:
        self.setWindowTitle("Derivative Calculator")
        self.setGeometry(100, 100, 400, 300)
        
        # Create labels and sliders
        self.func_label = QLabel("f(x) = x^2", self)
        self.x_label = QLabel("x = 2.0", self)
        self.result_label = QLabel("f'(x) = N/A", self)
        
        self.func_slider = QSlider(Qt.Horizontal, self)
        self.func_slider.setMinimum(1)
        self.func_slider.setMaximum(10)
        self.func_slider.setValue(2)
        self.func_slider.setTickPosition(QSlider.TicksBelow)
        self.func_slider.setTickInterval(1)
        
        self.x_slider = QSlider(Qt.Horizontal, self)
        self.x_slider.setMinimum(-10)
        self.x_slider.setMaximum(10)
        self.x_slider.setValue(2)
        self.x_slider.setTickPosition(QSlider.TicksBelow)
        self.x_slider.setTickInterval(1)
        
        # Button to compute the derivative
        self.compute_button = QPushButton("Compute Derivative", self)
        self.compute_button.clicked.connect(self.compute_derivative)
        
        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.func_label)
        layout.addWidget(self.func_slider)
        layout.addWidget(self.x_label)
        layout.addWidget(self.x_slider)
        layout.addWidget(self.compute_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
        
        # Connect slider changes to update methods
        self.func_slider.valueChanged.connect(self.update_func)
        self.x_slider.valueChanged.connect(self.update_x)
        
    @log_call
    def update_func(self, value: int) -> None:
        """
        Update the function label based on the slider value.
        
        Assumes the function is of the form f(x)=x^n.
        """
        self.func_label.setText(f"f(x) = x^{value}")
        
    @log_call
    def update_x(self, value: int) -> None:
        """
        Update the x label based on the slider value.
        """
        self.x_label.setText(f"x = {value}")
        
    @log_call
    def compute_derivative(self) -> None:
        """
        Compute the derivative of the function at the given x value and update the result label.
        """
        try:
            # Extract exponent from the function label ("f(x) = x^n")
            func_text = self.func_label.text()
            exponent_str = func_text.split("^")[1]
            exponent = float(exponent_str)
            
            # Build the function expression string
            expression = f"x**{int(exponent)}"
            
            # Parse the function
            func = parse_func(expression)
            
            # Get the current x value from the label
            x_value = float(self.x_label.text().split("=")[1])
            
            # Compute the derivative
            deriv = derivative(func, x_value)
            
            self.result_label.setText(f"f'({x_value}) = {deriv:.4f}")
        except Exception as e:
            logging.error("Error computing derivative", exc_info=True)
            self.result_label.setText("Error computing derivative.")

def main() -> None:
    app = QApplication(sys.argv)
    gui = DerivativeGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
