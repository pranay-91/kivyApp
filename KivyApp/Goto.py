import abc
from Operation import Operation


class Goto(Operation):
    """description of class"""
    
    def __init__(self, operation):
        self.operation= operation

    def operate(self, memory):
        result = self.operation.operate(memory)
        return result
