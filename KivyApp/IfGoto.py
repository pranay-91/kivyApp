"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: IFGoto.py
@title: IfGoto
@description: IfGoto is a type of Expression and implement Expression abstract class.
             IfGoto simply computes the If expression. If the expression result is true then operates the operation referred by goto 
"""
import abc
from Operation import Operation


class IfGoto(Operation):
    def __init__(self, expression, goto):
        self.expression = expression
        self.goto = goto

    """
    Compute the If expression and operate goto opration if true
    """
    def operate(self, memory):
        if (self.expression.compute(memory)):
            return self.goto.operate(memory)
