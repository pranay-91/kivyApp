"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Let.py
@title: Let
@description: Let is a type of Expression creates a variable and stores given value in the memory.
              Inherits Expression abstract class
"""

import abc
from Operation import Operation


class Let(Operation):   
    def __init__(self, name, value):
        self.name = name
        self.value = value

    """
    Set the new value to the variable in the memory
    """
    def operate(self, memory):
        memory.set_value(self.name, self.value)
       

