"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Interpreter.py
@title: Interpreter
@description: Interpreter consists of Memory and collection of lines of operations.
              It also includes Operation factory as a member.    
"""
from Memory import Memory
from Operation import Operation
from OperationFactory import OperationFactory

class Interpreter(object):
    def __init__(self):
        self.memory = Memory()
        # list of operations stored as list
        self.lines = {}
        # list of actual operation objects that has been executed before
        self.operations = {}
        # list of output lines
        self.output=[]
        # instance of operation factory to create operations based on lines of operations
        self.op_maker = OperationFactory(self.memory, self.operations, self.lines)

    def add_line(self, number, line):  
        """
        Add operation lines to the Interpreter
        """
        self.lines[int(number)] = line

    def get_output(self):
        """
        Get the list of output
        """
        return self.output

    def get_variables(self):
        """
        Get the list of variables in the memory
        """
        return self.memory.get_variables()

    def write_error(self, msg):
        self.output = ["Error", msg]


    def run(self):
        """
        Sort the lines of operation and run them line by line
        Go through each line, create related operation then execute the operations
        """
        line_number = sorted(self.lines.keys())
        sub_stack = []
        i =0
        while i < len(line_number):
            current_no = line_number[i]
            current_line = self.lines[current_no]

            if current_line[0] == 'END':
                return 0
            
            elif current_line[0] == 'GOTO' or current_line[0] == 'GOSUB':
                if int(current_line[1]) == current_no:
                    self.write_error("Cannot Goto same line number")
                    return 0        

                if int(current_line[1]) in line_number:
                    i = line_number.index(int(current_line[1]))               
                else:
                    self.write_error("Line Number does not exist")
                    return 0
   
                if current_line[0] == 'GOSUB':
                    sub_stack.append(i+1)
                     
            elif current_line[0] == 'RETURN':
                if len(sub_stack) < 1:
                    #TODO throw an exception 'RETURN WITHOUT GOSUB'
                    self.write_error("RETURN WITHOUT GOSUB")
                    return 0
                else:
                    i = sub_stack.pop()
            
            else:           
                op = self.op_maker.create_operation(current_line)
                if isinstance(op, str):
                    self.write_error(op)
                    return 0
                self.operations[current_no] = op

                # Get the result of each operation
                result = op.operate(self.memory)
            
                # if an operation returns a value then add the result to output list
                if result is not None:
                    self.output.append(result)
           
                if current_line[0] == "IF" and result == True:
                    i =line_number.index(int(current_line[5]))
                else:
                    i+=1

            

        #for each_number in line_number:
        #    current_line = self.lines[each_number]
        #    op = self.op_maker.create_operation(current_line)
        #    if isinstance(op, str):
        #        self.output = ["Error", op]
        #        return 0
        #    self.operations[each_number] = op

        #    # Get the result of each operation
        #    result = op.operate(self.memory)
            
        #    # if an operation returns a value then add the result to output list
        #    if result is not None:
        #        self.output.append(result)

    

