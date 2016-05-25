"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Division.py
@title: Division
@description: Division is a type of Expression, implements  Expresssion abstract class. Simply divides two operands and rerturn the value when compute() method is invoked
"""

import abc
from Expression import Expression
from Memory import Memory

class Division(Expression):
    def __init__(self, lhs, rhs):
        super(Division, self).__init__(lhs, '/', rhs)
    
    def compute(self, memory):
        # METHOD 1: STATIC TYPING
        #return memory.get_value(self.lhs) + memory.get_value(self.rhs)
        # METHOD 2: CONVERT STRINGS TO NUMBERS AT EVALUATION TIME
        lhs = 0
        rhs = 1

        if self.lhs.isdigit():
            lhs = float(self.lhs)
        elif memory.is_variable(self.lhs):
            lhs =  float(memory.get_value(self.lhs))
        else:
            return (self.lhs) + " variable does not exist."

        if self.rhs.isdigit():
            rhs = float(self.rhs)
            if rhs == 0 :
                return "Cannot be divisible by zero."
        else:
            if memory.is_variable(self.rhs):
                rhs =  float(memory.get_value(self.rhs))
                if rhs == 0 :
                    return "Cannot be divisible by zero."
            else:
                return (self.rhs) + " variable does not exist."
        
        return lhs / rhs


