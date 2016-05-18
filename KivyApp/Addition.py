"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Addition.py
@title: Addition
@description: Addition is a type of Expression, implements  Expresssion abstract class 
"""

import abc
from Expression import Expression
from Memory import Memory

class Addition(Expression):
    def __init__(self, lhs, rhs):
        super(Addition, self).__init__(lhs, '+', rhs)
    
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

        return lhs + rhs


