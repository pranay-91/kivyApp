"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: OperationFactory.py
@title: OperationFfactory
@description: Operation Factory is responsible for creating relevant concrete Operation object depending upon the command. 
              Any new concrete Operation requires to update create_operation method.  
"""

from Expression import Expression
from Print import Print
from ExpressionFactory import ExpressionFactory
from Let import Let
from Goto import Goto
from IfGoto import IfGoto
from Operation import Operation

class OperationFactory(object):
    """description of class"""
    def __init__(self, memory, operations, lines):
        self.exp_maker = ExpressionFactory()
        self.memory = memory
        self.operations = operations
        self.lines = lines
        

    """
    Checks the type of operation and returns an instance of the relevant command
    """
    def create_operation(self, line):
        op =line[0]
        if op == 'LET':
            # create LET operation
           var_name = line[1]
           value = line[3:]

           if value[1]=='':
              # if no exprssion to be computed. eg. LET X = 10
               value = value[0]
               if isinstance(value, str) and self.memory.is_variable(value):
                   value = self.memory.get_value(value)
               
                 
               return Let(var_name, value)
           else:
              # if there is an expression that needs to be computed eg. LET X = X + 10
              exp = self.exp_maker.create_expression(value[0], value[1], value[2])
              value = exp.compute(self.memory) 
              if isinstance(value, str):
                return value
              return Let(var_name, value)    

          

        elif op == 'PRINT':
            # create PRINT operation
           return Print(line[1])

        elif op =='GOTO':
            # create GOTO operation
    
           if line[1].isdigit() == False:
                self.memory.is_variable(line[1])
                goto_number = int(self.memory.get_value(line[1]))
           else:
                goto_number = int(line[1])        
           
           if goto_number in self.lines.keys():
               goto_op = self.create_operation(self.lines[goto_number])
               return Goto(goto_op)
           else:
               return "Line number " + str(goto_number) + " doesnt exist"

           #if goto_number in self.operations.keys():

           #    return Goto(self.operations[goto_number])
           #else:
           #    return "Line number " + str(goto_number) + " doesnt exist"

       
        elif op == 'IF':
            # create IF GOTO operation
            if  line[5].isdigit() == False:
                self.memory.is_variable(line[5])
                goto_number = int(self.memory.get_value(line[5]))
            else:
                goto_number = int(line[5])
            exp = self.exp_maker.create_expression(line[1], line[2], line[3])
          
            if goto_number in self.lines.keys():
               goto_op = self.create_operation(self.lines[goto_number])
               return IfGoto(exp, Goto(goto_op))
            else:
               return "Line number " + str(goto_number) + " doesnt exist"
          