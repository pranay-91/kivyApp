"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: EndLayout.py
@title: EndLayout
@description: This is the main program for the Scratchbasic application. 
              It consists of four major layout panel: Main Layout, Command Panel Layout, Workspace Layout, Output Layout
              MainLayout is the base layout that instantiates Command Panel, Workspace and Output layout in order
              Each Expression Layout PRINT, LET, IF/GOTO, GOTO is a subclass of Expression Layout
              Such design consideration allows one to add a new expression by simply extending Expression Layout
              This program reuses existing Dumbasic program written in Python to compute the expressions and operations
              An instance of Interpreter class is used to integrate with Dumbasic program 
"""

import kivy
from Layouts.Expressions.ExpressionLayout import ExpressionLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

kivy.require('1.0.6') # current kivy version !



class EndLayout(ExpressionLayout):
    """
    Goto Layout represents Gosub expression. It extends the Expression Layout
    """
    def __init__(self, line,  **kwargs):
        super(EndLayout, self).__init__(line, 'END', **kwargs)

        self.cols = 4
        self.padding = 4
        self.height = 40
        self.width = 100

       
    """
    Add the widgets to the layout
    """
    def draw(self):
        super(EndLayout, self).draw()
     
   
    """
    Get the expression list
    """
    def get_expression(self):
        super(EndLayout, self).get_expression()
        return [self.name]