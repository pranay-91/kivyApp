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
        self.variables[name] = value
            
