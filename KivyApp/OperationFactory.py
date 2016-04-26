
from Expression import Expression
from Print import Print
from ExpressionFactory import ExpressionFactory
from Let import Let

class OperationFactory(object):
    """description of class"""
    def __init__(self, memory):
        self.exp_maker = ExpressionFactory()
        self.memory = memory

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
              

    


