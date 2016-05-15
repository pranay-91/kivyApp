
from Memory import Memory
from Operation import Operation
from OperationFactory import OperationFactory

class Interpreter(object):
    """description of class"""

    def __init__(self):
        self.memory = Memory()
        self.lines = {}
        self.operations = {}
        self.output=[]
        self.op_maker = OperationFactory(self.memory, self.operations)

    def add_line(self, number, line):  
        self.lines[int(number)] = line

    def get_output(self):
        return self.output

    def get_variables(self):
        return self.memory.get_variables()

    def run(self):
        line_number = sorted(self.lines.keys())
        print(self.lines)
        for each_number in line_number:
            current_line = self.lines[each_number]
            op = self.op_maker.create_operation(current_line)
            self.operations[each_number] = op
            result = op.operate(self.memory)
            if result is not None:
                self.output.append(result)

    

