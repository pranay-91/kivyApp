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
        return int(memory.get_value(self.lhs)) + int(memory.get_value(self.rhs))


