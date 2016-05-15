import abc
from Expression import Expression
from Memory import Memory

class Compare(Expression):
    """description of class"""

    def __init__(self, lhs, op, rhs):
        super(Compare, self).__init__(lhs, op, rhs)
    
    def compute(self, memory):
        if memory.is_variable(self.lhs):
            lhs_val = memory.get_value(self.lhs)
        else:
            lhs_val = int(self.lhs)  

        if memory.is_variable(self.rhs):
            rhs_val = memory.get_value(self.rhs)
        else:
            rhs_val = int(self.rhs)  
        
        if self.operand == '>':
            return (lhs_val > rhs_val)
        elif self.operand == '<':
            return (lhs_val < rhs_val)
        elif self.operand == '==':
            return (lhs_val == rhs_val)
       


