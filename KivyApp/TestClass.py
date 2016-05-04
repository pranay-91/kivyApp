from Memory import Memory
from Interpreter import Interpreter
import time

class TestClass(object):
    """description of class"""
    def test_one(self,benchmark):
        
        n=1
        while(n<100):
            i = Interpreter()
            f = open('input.bas', 'r')
            for line in f:   
                line = line.strip()
                split_line = line.split(" ")
                line_number = int(split_line[0])
                i.add_line(line_number, split_line[1:])
            i.run()
            f.close()
            n=n+1
        benchmark(time.sleep, 0.000001)

