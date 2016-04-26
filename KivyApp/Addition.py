import abc
from Expression import Expression
from Memory import Memory

class Addition(Expression):
    """description of class"""

    def __init__(self, lhs, rhs):
        super(Addition, self).__init__(lhs, '+', rhs)
    
    def compute(self, memory):
        return memory.get_value(self.lhs) + memory.get_value(self.rhs)


