class Memory(object):
    """description of class"""
    def __init__(self):
        self.variables = {}
    def get_value(self, variable):
        if variable in self.variables.keys():
            return self.variables[variable];
        else:
            return int(variable)

    def is_variable(self, var):
        if var in self.variables.keys():
            return True

    def set_value(self, name, value):
        # METHOD 1: STORING VARIABLES SAME AS THE ORIGINAL TYPE
        #self.variables[name] = value
        # METHOD 2: STORING ALL THE VARIABLE VALUES AS STRING
        self.variables[name] = str(value)
            
