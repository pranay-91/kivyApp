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



class IfLayout(ExpressionLayout):

    def __init__(self, line, var_list=[], **kwargs):
        super(IfLayout, self).__init__(line, "IF", var_list,  **kwargs)
      
        self.cols = 9
        self.padding = 4
        self.height = 40
        self.width = 380
       

        self.txt_value1 = self.get_cmb_variables()
        self.spn_operator = Spinner(text = '==', values =('>', '<', '=='), size_hint=(.1,1))
        self.txt_value2 = self.get_cmb_variables()
        self.lbl_goto = Label(text="GOTO", size_hint=(.1,1))
        self.txt_value3 = TextInput(multiline = False, size_hint=(.1,1))
      
    """
    Add the widgets to the layout
    """
    def draw(self):
        super(IfLayout, self).draw()
        self.add_widget(self.txt_value1)
        self.add_widget(self.spn_operator)
        self.add_widget(self.txt_value2)
        self.add_widget(self.lbl_goto)
        self.add_widget(self.txt_value3)

    """
    Get the expression list
    """
    def get_expression(self):
        super(IfLayout, self).get_expression()
        if str(self.txt_value3.text.isdigit()):
            return [self.name, str(self.txt_value1.text), self.spn_operator.text, str(self.txt_value2.text), self.lbl_goto.text, str(self.txt_value3.text)]
        else:
            return ["Error", "Line number is not valid"]
        

