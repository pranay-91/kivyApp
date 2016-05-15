"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: ExpressionFactory.py
@title: ExpressionFactory
@description: Expression Factory is responsible for creating relevant concrete Expression object depending upon the operator. 
              Any new concrete expression requires to update create_expression method.   
"""

from Memory import Memory
from Addition import Addition
from Subtraction import Subtraction
from Compare import Compare

class ExpressionFactory(object):
    """
    Checks the operator and returns an instance of the relevant expression
    """
    def create_expression(self, lhs, op, rhs):
        if op == '+':
            return Addition(lhs, rhs)
        elif op == '-':
            return Subtraction(lhs,rhs)
        else:
            return Compare(lhs, op, rhs)

