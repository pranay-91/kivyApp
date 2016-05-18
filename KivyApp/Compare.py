"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Comnpare.py
@title: Compare
@description: Compare is a type of Expression, implements  Expression abstract class
              It consisist of three expression: Greater than(>), Lesser than (<) and  Equality(==)
"""
import abc
from Expression import Expression
from Memory import Memory

class Compare(Expression):
    """description of class"""

    def __init__(self, lhs, op, rhs):
        super(Compare, self).__init__(lhs, op, rhs)
    
    def compute(self, memory):
        if memory.is_variable(self.lhs):
        # if its a variable in the memory
            lhs_val = memory.get_value(self.lhs)
        else:
            lhs_val = str(self.lhs)  
        
        if memory.is_variable(self.rhs):
        #  if its a variable in the memory
           rhs_val = memory.get_value(self.rhs)
        else:
            rhs_val = str(self.rhs)  
       
        if self.operand == '>':
            return (int(lhs_val) > int(rhs_val))
        elif self.operand == '<':
            return (int(lhs_val) < int(rhs_val))
        elif self.operand == '==':
            return (str(lhs_val) ==  str(rhs_val))
       


