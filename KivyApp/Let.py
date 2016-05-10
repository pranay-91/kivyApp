import abc
from Operation import Operation


class Let(Operation):
    """description of class"""
    
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def operate(self, memory):
        memory.set_value(self.name, self.value)
        #return 0

