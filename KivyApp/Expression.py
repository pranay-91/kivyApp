"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Expression.py
@title: Expression
@description: Abstract class representing an Expression.  
              Any new concrete Expression should inherit this class. Implement the abstract methods and pass relevant objects to the constructor.
              This allows an Expression to compute without needing to know about the concrete Expression class.
"""
import abc

class Expression(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.operand = op
    """
    Each subclass expression class must implement compute method. Compute runs the expression amd returns the result
    """
    @abc.abstractmethod
    def compute(self, memory):
        return


