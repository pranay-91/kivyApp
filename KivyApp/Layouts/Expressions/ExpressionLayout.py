import kivy

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

kivy.require('1.0.6') # current kivy version !

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


from Layouts.ComboEdit import ComboEdit


class ExpressionLayout(BoxLayout):
  
    """
    Expression Layout class is the base class for each expression.
    One can extend this class to add new  Expression.
    """
    def __init__(self, line, name,  var_list=[], **kwargs):
        super(ExpressionLayout, self).__init__(**kwargs)
        self.line = line
        self.name = name
        self.size_hint=(None, None)
        self.var_list = var_list
        self.current_touch = False
     
            
        
        self.txtbox_lineno = TextInput(text=str(self.line), size_hint=(.1,1))
        self.btn_delete = Button(text="Del", size_hint =(.1,1))
        self.lbl_name = Label(text=self.name, size_hint=(.1,1))
     
    """
    Creates and returns a new combo edit for list of variables
    """
    def get_cmb_variables(self):
        btn_variables = []
        for var in self.var_list:
           btn_variables.append(Button(text = str.strip(str(var)),size_hint_y=None,height=40))
        return ComboEdit( size_hint= (.1, 1), height=50, options=btn_variables)

    """
    Add the widgets to the layout
    """
    def draw(self):
        self.add_widget(self.btn_delete)
        self.add_widget(self.txtbox_lineno)
        self.add_widget(self.lbl_name)

    """
    Deletes the expression from the workspace
    """
    def delete_btn_click_event(self, instance):
        self.btn_delete._bind(on_press, instance)

    """
    Get the line number
    """
    def get_line_number(self):
        return self.line

    def set_line_number(self, number):
        self.set_line_number = number

    def on_touch_down(self, touch):
        super(ExpressionLayout, self).on_touch_down(touch)
        if self.collide_point(*touch.pos):
            return self.get_line_number()

    """
    Get all the values from the layout interface and convert it into list that gets sent to interpreter for computation
    All the Expression must implement this method.
    """
    def get_expression(self):
        self.line = int(self.txtbox_lineno.text)
        pass

    
    def on_touch_down(self, touch):
        super(ExpressionLayout, self).on_touch_down(touch)
        if self.collide_point(*touch.pos):
            self.current_touch = True
            print 'touch'
          
            print touch