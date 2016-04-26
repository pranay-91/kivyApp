from Memory import Memory
from Addition import Addition
from Subtraction import Subtraction

class ExpressionFactory(object):
    """description of class"""
    def create_expression(self, lhs, op, rhs):
        if op == '+':
            return Addition(lhs, rhs)
        elif op == '-':
            return Subtraction(lhs,rhs)

