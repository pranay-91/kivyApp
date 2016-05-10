import abc
from Operation import Operation
#from abc import Operation

class Print(Operation):
   
    def __init__(self, val):
        self.val = val

    def operate(self, memory):
        val = self.val
        if len(self.val) < 2 and memory.is_variable(self.val):
            val= memory.get_value(self.val)  
        print val
        return val


