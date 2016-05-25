"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: Operation.py
@title: Operation
@description: Abstract class representing an Operation.  
              Any new concrete Operation should inherit this class. Implement the abstract methods and pass relevant objects to the constructor.
              This allows an Operation to operate without needing to know about the concrete Operation class.

"""
from abc import ABCMeta, abstractmethod


class Operation(object):
    __metaclass__ = ABCMeta

    """
    Each subclass operation class must implement compute method. Compute runs the operation amd returns the result
    """
    @abstractmethod
    def operate(self, memory):
        print('here')


 

    




