from Interpreter import Interpreter
import time


class MainApp(object):
    """description of class"""
    if __name__ == '__main__':
       start = time.clock()

       n = 1
       while(n < 1000):
            i = Interpreter()
            f = open('input.bas', 'r')
            for line in f:   
                line = line.strip()
                split_line = line.split(" ")
                line_number = int(split_line[0])
                i.add_line(line_number, split_line[1:])
            i.run()
            f.close()
            n = n + 1
       end = time.clock()
       
       print (end-start) 
   
       

