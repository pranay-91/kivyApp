from Interpreter import Interpreter

class MainApp(object):
    """description of class"""
    
    if __name__ == '__main__':

       i = Interpreter()
       f = open('input.bas', 'r')
       for line in f:   
           line = line.strip()
           split_line = line.split(" ")
           line_number = int(split_line[0])
           i.add_line(line_number, split_line[1:])
         
       i.run()

