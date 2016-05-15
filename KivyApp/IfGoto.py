import abc
from Operation import Operation


class IfGoto(Operation):
    """description of class"""
    
    def __init__(self, expression, goto):
        self.expression = expression
        self.goto = goto

    def operate(self, memory):
        if (self.expression.compute(memory)):
            return self.goto.operate(memory)
