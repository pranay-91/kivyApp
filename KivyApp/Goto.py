"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Goto.py
@title: Goto
@description: Goto is a type of Expression and implement Expression abstract class.
             Goto simply refers to the operation specified by the line number and operates the operation
"""

import abc
from Operation import Operation


class Goto(Operation):
    def __init__(self, operation):
        self.operation= operation

    """
    Operate the referred operation and return the result
    """
    def operate(self, memory):
        result = self.operation.operate(memory)
        return result
