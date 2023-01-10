# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:23:28 2023

@author: timot
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout

class DerivativeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create a label and a slider for the function
        func_label = QLabel("f(x) = x^2")
        func_slider = QSlider(Qt.Horizontal)
        func_slider.setMinimum(1)
        func_slider.setMaximum(10)
        func_slider.setValue(2)
        func_slider.setTickPosition(QSlider.TicksBelow)
        func_slider.setTickInterval(1)
        
        # Create a label and a slider for the value of the derivative
        x_label = QLabel("x = 2.0")
        x_slider = QSlider(Qt.Horizontal)
        x_slider.setMinimum(-10)
        x_slider.setMaximum(10)
        x_slider.setValue(2)
        x_slider.setTickPosition(QSlider.TicksBelow)
        x_slider.setTickInterval(1)
        
        # Create a layout and add the labels and sliders
        layout = QVBoxLayout()
        layout.addWidget(func_label)
        layout.addWidget(func_slider)
        layout.addWidget(x_label)
        layout.addWidget(x_slider)
        self.setLayout(layout)
        
        # Connect the sliders to the update function
        func_slider.valueChanged.connect(self.update_func)
        x_slider.valueChanged.connect(self.update_x)
        
    def update_func(self, value: int):
        """Update the function label when the function slider is moved."""
        self.func_label.setText(f"f(x) = x^{value}")
        
    def update_x(self, value: int):
        """Update the x label when the x slider is moved."""
        self.x_label.setText(f"x = {value}")
        
    def compute_derivative(self):
        """Compute the derivative using the current function and x value."""
        # Parse the function from the label text
        expression = self.func_label.text().split("=")[1]
        func = parse_func(expression)
        
        # Get the x value from the x label
        x = float(self.x_label.text().split("=")[1])
        
        # Compute the derivative
        deriv = derivative(func, x)
        
        # Update the result label
        self.result_label.setText(f"f'({x}) = {deriv}")
        
    def create_button(self):
        """Create a button to compute the derivative."""
        btn = QPushButton("Compute derivative", self)
        btn.clicked.connect(self.compute_derivative)
        return btn
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DerivativeGUI()
    gui.show()
    sys.exit(app.exec_())
