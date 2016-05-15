"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Subtraction.py
@title: Subtraction
@description: Subtraction is a type of Expression, implements  Expression abstract class
              It simply returns the difference between two values.
"""

import abc
from Expression import Expression
from Memory import Memory

class Subtraction(Expression):
    def __init__(self, lhs, rhs):
        super(Subtraction, self).__init__(lhs, '-', rhs)
    
    def compute(self, memory):
        return memory.get_value(self.lhs) - memory.get_value(self.rhs)

