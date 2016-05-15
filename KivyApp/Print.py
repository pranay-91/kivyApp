"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Print.py
@title: Print
@description: Print is a type of Expression and implement Expression abstract class.
              Print simply displays the value of the variable or a string 
"""


import abc
from Operation import Operation

class Print(Operation):
    def __init__(self, val):
        self.val = val

    """
    Prints the value of the variable or a string
    """
    def operate(self, memory):
        val = self.val
        if len(self.val) < 2 and memory.is_variable(self.val):
        # if it is a variable, get the value
            val= memory.get_value(self.val)  
        print val
        return val


