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

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from Layouts.Expressions.ExpressionLayout import ExpressionLayout

kivy.require('1.0.6') # current kivy version !


class LetLayout(ExpressionLayout):
    
    """
    Let Layout represents Let expression. It extends the Expression Layout
    """
    def __init__(self, line, var_list=[], **kwargs):
        super(LetLayout, self).__init__(line, "LET",var_list, **kwargs)

        self.cols = 7
        self.padding = 4
        self.height = 40
        self.width = 400
        

        self.txt_var_name = TextInput(multiline = False, size_hint=(.1,1))
        self.lbl_equal = Label(text="=",  size_hint=(.1,1))
    
        self.txt_val1 = self.get_cmb_variables()

        self.spn_operator = Spinner(text = '', values =('','-', '+','*', '/'), size_hint=(.1,1))
     
        self.txt_val2 = self.get_cmb_variables()


    """
    Add the widgets to the layout
    """
    def draw(self):
        super(LetLayout, self).draw()
        self.add_widget(self.txt_var_name)
        self.add_widget(self.lbl_equal)
        self.add_widget(self.txt_val1)
        self.add_widget(self.spn_operator)
        self.add_widget(self.txt_val2)
   
    """
    Get the expression list
    """
    def get_expression(self):
        super(LetLayout, self).get_expression()
        if self.txt_var_name.text == ""  or self.txt_var_name.text.isnumeric():
           msg = "Line number: " + str(self.get_line_number()) + ". Please enter a valid variable name. "
           return ["Error", msg]
        #if self.txt_val1.text.isnumeric() == False and self.spn_operator.text!='':
        #   msg = "Line number: " + str(self.get_line_number()) + ". String operation is not allowed."
        #   return ["Error", msg]
        else:
           return [self.name, self.txt_var_name.text, self.lbl_equal.text, str(self.txt_val1.text), self.spn_operator.text, str(self.txt_val2.text)]
