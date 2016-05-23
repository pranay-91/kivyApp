"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: If.py
@title: If
@description: IfGoto is a type of Expression and implement Expression abstract class.
             IfGoto simply computes the If expression. If the expression result is true then operates the operation referred by goto 
"""
import abc
from Operation import Operation


class If(Operation):
    def __init__(self, expression):
        self.expression = expression
        

    """
    Compute the If expression and operate goto opration if true
    """
    def operate(self, memory):
        return self.expression.compute(memory)
