import abc

class Expression(object):
    __metaclass__ = abc.ABCMeta
    """description of class"""
   
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.operand = op

    @abc.abstractmethod
    def compute(self, memory):
        return


