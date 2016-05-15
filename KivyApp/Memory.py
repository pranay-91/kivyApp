"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Memory.py
@title: Memory
@description: Memory stores the value of all the variables in the context.
              Variables is a dictionary type where variable name is the key. 
"""
class Memory(object):
    
    def __init__(self):
        self.variables = {}

    """
    Get the value of the variable from the memory
    """
    def get_value(self, variable):
        if variable in self.variables.keys():
            return self.variables[variable];
        else:
            return int(variable)

    """
    Checks whther the variable exists in memory.
    """
    def is_variable(self, var):
        if var in self.variables.keys():
            return True

    """
    Get the list of the variable from the memory
    """
    def get_variables(self):
        return self.variables

    """
    Store the value in the variable allocated in the memory
    """
    def set_value(self, name, value):
        # METHOD 1: STORING VARIABLES SAME AS THE ORIGINAL TYPE
        self.variables[name] = value
        # METHOD 2: STORING ALL THE VARIABLE VALUES AS STRING
        #self.variables[name] = str(value)
            
