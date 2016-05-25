"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Multiplication.py
@title: Multiplication
@description: Multiplication is a type of Expression, implements  Expresssion abstract class. Simoply Multiplies two operands and rerturn the value when compute() method is invoked
"""

import abc
from Expression import Expression
from Memory import Memory

class Multiplication(Expression):
    def __init__(self, lhs, rhs):
        super(Multiplication, self).__init__(lhs, '*', rhs)
    
    def compute(self, memory):
        # METHOD 1: STATIC TYPING
        #return memory.get_value(self.lhs) + memory.get_value(self.rhs)
        # METHOD 2: CONVERT STRINGS TO NUMBERS AT EVALUATION TIME
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

        return lhs * rhs


