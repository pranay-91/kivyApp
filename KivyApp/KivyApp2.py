"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: KivyApp2.py
@title: KivyApp2
@description: This is the main program for the Scratchbasic application. 
              It consists of four major layout panel: Main Layout, Command Panel Layout, Workspace Layout, Output Layout
              MainLayout is the base layout that instantiates Command Panel, Workspace and Output layout in order
              Each Expression Layout PRINT, LET, IF/GOTO, GOTO is a subclass of Expression Layout
              Such design consideration allows one to add a new expression by simply extending Expression Layout
              This program reuses existing Dumbasic program written in Python to compute the expressions and operations
              An instance of Interpreter class is used to integrate with Dumbasic program """
import kivy
import sys
import abc



kivy.require('1.0.6')  # current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

from Layouts.Expressions.ExpressionLayout import ExpressionLayout
from Layouts.Expressions.LetLayout import LetLayout
from Layouts.Expressions.PrintLayout import PrintLayout
from Layouts.Expressions.GotoLayout import GotoLayout
from Layouts.Expressions.IfLayout import IfLayout
from Layouts.Expressions.GoSubLayout import GoSubLayout
from Layouts.Expressions.ReturnLayout import ReturnLayout
from Layouts.Expressions.EndLayout import EndLayout




#import ExpressionLayout

from Expression import Expression
from Interpreter import Interpreter


class CommandPanel(GridLayout):
    """
    This layout contains all the necessary expression commands such as LET, PRINT, IF/GOTO, GOTO
    """
    def __init__(self, workspace, **kwargs):
        super(CommandPanel, self).__init__(**kwargs)
        self.cols = 1
        self.pos = (5,-10)
        self.workspace = workspace
        self.expression_buttons = []       
      
       
    """
    Draw the menu widget on this workspace.
    """
    def draw(self, menu):
       self.add_widget(menu)

    """
    Create buttons for expression and add them in the layout. Bind the button to click event
    """
    def add_expression_btn(self, name):
        btn =  Button(text=str(name), size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        btn.bind(on_press = self.btn_clicked_event)
        self.add_widget(btn)
        self.expression_buttons.append(btn)
    """
    When user click on each expression button would create an expression layout in workspace
    """
    def btn_clicked_event(self, instance):
        self.workspace.add_expression(instance)

class Workspace(ScrollView):
    """
    Workspace is where user can view expression, configure them or simply choose to delete expressions.
    """
    def __init__(self, **kwargs):
        super(Workspace, self).__init__(**kwargs)
        self.line_number = 1
        self.expression_list = []
        self.y_pos = .8
        self.current_variable_names = []
        self.layout = GridLayout(cols=1, padding=10, spacing=10, size_hint=(None, None), width = 500)
        self.layout.bind(minimum_height=self.layout.setter('height'))
      
    """
    Draw the expression to the workspace layout
    """
    def draw(self):
        self.add_widget(self.layout)

    """
    Update the current list of variable names after a program is run
    """
    def update_variable_names(self, var):
        self.current_variable_names = var

    """
    "Clear the workspace when a new program is selected by the user
    """        
    def clear(self):
        self.expression_list = []
        self.y_pos = .8
        self.line_number = 1
        self.layout.clear_widgets()

    """
    Create relevant expression according to the expression buttons clicked in the command panel
    """

    def add_expression(self, instance):
        #exp = LetLayout(line, size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos})
        if instance.text == 'LET':
            exp = LetLayout(self.line_number, self.current_variable_names, pos_hint={'x': .2, 'y': self.y_pos})
        elif instance.text == 'PRINT':
            exp = PrintLayout(self.line_number, pos_hint={'x': .2, 'y': self.y_pos})
        elif instance.text == 'GOTO':
            exp = GotoLayout(self.line_number, pos_hint={'x': .2, 'y': self.y_pos})
        elif instance.text == 'IF':
            exp = IfLayout(self.line_number, self.current_variable_names, pos_hint={'x': .2, 'y': self.y_pos})
        elif instance.text == 'GOSUB':
            exp = GoSubLayout(self.line_number, pos_hint={'x': .2, 'y': self.y_pos})
        elif instance.text == 'RETURN':
            exp = ReturnLayout(self.line_number,  pos_hint={'x': .2, 'y': self.y_pos})
        elif instance.text == 'END':
            exp = EndLayout(self.line_number, pos_hint={'x': .2, 'y': self.y_pos})

        self.line_number += 1
        # bind the delete event when user clicks on the delete button
        exp.btn_delete.fbind('on_press', self.delete_expression, expression=exp)
        
        exp.draw()
        self.layout.add_widget(exp)
        
        self.y_pos -= .1
        self.expression_list.append(exp)

    def on_touch_down(self, t):
        super(Workspace, self).on_touch_down(t)

        #t.apply_transform_2d(self.layout.to_local)
       # for widget in self.layout.walk():
            #print widget.on_touch_down(t)
           # print t
            #if widget.id == 'LET':
            #       print widget.on_touch_down(t)
    #            print "\n"
    #            print widget.collide_point(*t.pos)
    #            print widget
    #            print t
    #            print widget.x
    #            print widget.y

        #if self.collide_point(*t.pos):
        #    for widget in self.layout.walk():
        #        #if widget.collide_point(*t.pos):
        #        if widget.id == 'LET':
        #           print widget.on_touch_down(t)
                   #print widget.get_line_number()
                       #print("\n{} -> {}".format("Line number", widget.get_line_number()))
                   



    """
    Delete each expression from the workspace. This method is triggered when delete button is clicked
    """

    def delete_expression(self, instance, expression):
        self.layout.remove_widget(expression)
        self.expression_list.remove(expression)
        #self.line_number -= 1

    """
    Get all the expressions from the workspace
    """
    def get_expressions(self):
        return self.expression_list


class Output(GridLayout):
    """
    This is where the result is printed out after the app is run successfully
    """
    def __init__(self, **kwargs):
        super(Output, self).__init__(**kwargs)
        
        self.comment = TextInput(text='Output is shown here..', width=800, height=200)
        self.btn_clear = Button(text='Clear', size_hint=(None, None), size=(200, 44), pos=(600, 0))
        self.btn_clear.bind(on_press=self.clear_event)
    
    def draw(self):
        self.add_widget(self.comment)
        self.add_widget(self.btn_clear)

    def clear_event(self, instance):
        self.clear()

    def clear(self):
        self.comment.text = ""

    def write_error(self, msg):
        self.comment.insert_text("\n ERROR!!! \n")
        
        for errors in msg:
            self.comment.insert_text(errors)
            self.comment.insert_text('\n')

    """
    Add lines to the output box
    """
    def add_text(self, text):
        self.comment.insert_text(text)


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.Interpreter = Interpreter()
        self.command_stack = []

        self.cols = 2
        self.orientation = "vertical"
        self.padding = 10

        self.workspace = Workspace()
        self.command_panel = CommandPanel(self.workspace)
        self.output = Output()

        self.spn_menu = Spinner(text='Menu', values=('New', 'Save', 'RUN', 'Exit'), size_hint =(None, None), size=(200, 44), pos_hint={'x': .1, 'y': .9})
        self.spn_menu.bind(text=self.menu_option_selected_event)
        
        self.command_panel.draw(self.spn_menu)
        self.command_panel.add_expression_btn('LET')
        self.command_panel.add_expression_btn('PRINT')
        self.command_panel.add_expression_btn('GOTO')
        self.command_panel.add_expression_btn('IF')
        self.command_panel.add_expression_btn('GOSUB')
        self.command_panel.add_expression_btn('RETURN')
        self.command_panel.add_expression_btn('END')
        self.add_widget(self.command_panel)

        self.orientation = "horizontal"
        self.workspace.draw()
        self.add_widget(self.workspace)
        
        self.output.draw()
        self.add_widget(self.output)

    #def on_touch_down(self, touch):
    #    super(MainLayout, self).on_touch_down(touch)
    #    for widget in self.workspace.layout.walk():
    #        if widget.id == 'LET':
    #            x = (touch.x- self.command_panel.x)
    #            y = (touch.y - self.command_panel.y)
    #            print widget.collide_point(x,y )
    #            print x
    #            print y

    """
    This is where the the program is run when user clicks Run from menu
    """
    def run_app(self):
        i = self.Interpreter

        has_expressions = False
        error_msgs = []

        for each_exp in self.workspace.get_expressions():
            expression_line = each_exp.get_expression()
            has_expressions = True
            if expression_line[0] is "Error":
                error_msgs.append(expression_line[1])
            else:            
                
                i.add_line(each_exp.get_line_number(), expression_line)

        if has_expressions is False:
            self.output.clear()
            self.output.write_error(["Nothing to run"])
            return 0

        if len(error_msgs) > 0:
            self.output.clear()
            self.output.write_error(error_msgs)
            return 0           
        i.clear_output()
        i.run()
        output = i.get_output()
        variables = i.get_variables()
        self.workspace.update_variable_names(sorted(variables))

        self.output.add_text("\n Output : \n")
        for value in output:
            self.output.add_text(' ' + str(value)+'\n')

        self.output.add_text('\n Memory: \n')
        self.output.add_text(' Variable \t Value \n')
        for var in sorted(variables):
            value = ' \t' + var + ' \t\t\t ' + str(variables[var]) + '\n'
            self.output.add_text(' ' + str(value))
        self.output.add_text('-------------------------------------------')
    
    """
    When user selects a menu option from the spinner
    """
    def menu_option_selected_event(self, instance, option):
        
        if option == 'New':
            self.spn_menu.text = 'Menu'
            self.workspace.clear()
            #self.Interpreter = Interpreter()
            
        elif option == 'Exit':
            sys.exit()
        elif option == 'RUN':
            self.spn_menu.text = 'Menu'
            self.run_app()


class KivyApp2(App):
    """
    Main Kivy Class to run the app.Simply creates instance of Mainlayout to initiate.
    """
    def build(self):
        main = MainLayout()
        return main


if __name__ == '__main__':
    KivyApp2().run()