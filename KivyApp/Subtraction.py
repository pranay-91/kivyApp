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
        lhs = 0
        rhs =0

        if self.lhs.isdigit():
            lhs = int(self.lhs)
        elif memory.is_variable(self.lhs):
            lhs =  int(memory.get_value(self.lhs))
        else:
            return (self.lhs) + " variable does not exist."
        
        if self.rhs.isdigit():
            rhs = int(self.rhs)
        elif memory.is_variable(self.rhs):
            rhs =  int(memory.get_value(self.rhs))
        else:
            return (self.rhs) + " variable does not exist."

        return lhs - rhs


       