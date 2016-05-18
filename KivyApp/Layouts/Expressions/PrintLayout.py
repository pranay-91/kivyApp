"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: ExpressionLayout.py
@title: ExpressionLayout
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


class PrintLayout(ExpressionLayout):
    """
    Print Layout represents Print expression. It extends the Expression Layout
    """
    def __init__(self, line, **kwargs):
        super(PrintLayout, self).__init__(line, "PRINT", **kwargs)

        self.cols = 4
        self.padding = 4
        self.height = 40
        self.width = 350

        self.txt_value = TextInput(multiline = False, size_hint=(.6,1))

    """
    Add the widgets to the layout
    """
    def draw(self):
        super(PrintLayout, self).draw()
        self.add_widget(self.txt_value)

    
    """
    Get the expression list
    """
    def get_expression(self):
        if self.txt_value.text == "":
           msg = "Line number: " + str(self.get_line_number()) + ". Nothing to Print "
           return ["Error", msg]
        else:
            return [self.name, str(self.txt_value.text)]