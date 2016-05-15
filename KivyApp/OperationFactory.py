
from Expression import Expression
from Print import Print
from ExpressionFactory import ExpressionFactory
from Let import Let
from Goto import Goto
from IfGoto import IfGoto

class OperationFactory(object):
    """description of class"""
    def __init__(self, memory, operations):
        self.exp_maker = ExpressionFactory()
        self.memory = memory
        self.operations = operations
        

    def create_operation(self, line):
        op =line[0]
        if op == 'LET':
           var_name = line[1]
           value = line[3:]
           if len(value) > 1:
              exp = self.exp_maker.create_expression(value[0], value[1], value[2])
              value = exp.compute(self.memory) 
           return Let(var_name, value)
        elif op == 'PRINT':
           return Print(line[1])
        elif op =='GOTO':
           goto_number = line[1]
           return Goto(self.operations[goto_number])
        elif op == 'IF':
            goto_number = int(line[5])
            exp = self.exp_maker.create_expression(line[1], line[2], line[3])
            return IfGoto(exp, Goto(self.operations[goto_number]))