"""
@author: Pranay Pradhananga, Damian Katsigiannis
@filename: KivyApp.py
@title: KivyApp
@description: This is the old version of the main app. Refer to KivyApp2 for the latest stable updated version
"""
import kivy
import sys
from kivy.uix.anchorlayout import AnchorLayout
kivy.require('1.0.6') # replace with your current kivy version !

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

from Let import Let
from Expression import Expression
from Interpreter import Interpreter


class LetLayout(BoxLayout):
    def __init__(self, line, **kwargs):
        super(LetLayout,self).__init__(**kwargs)
        self.line = line
        self.cols = 6
        self.padding = 4
        self.height = 40
        self.width = 400
        self.label = "LET"
       
        
        self.line_number = TextInput(text=str(self.line), size_hint=(.1,1))
        self.add_widget(self.line_number)

        self.add_widget(Label(text=self.label,  size_hint=(.1,1)))

        self.variable_name = TextInput(multiline = False, size_hint=(.1,1))
        self.add_widget(self.variable_name)

        self.add_widget(Label(text="=",  size_hint=(.1,1)))

        self.value1 = TextInput(multiline = False, text ="0", size_hint=(.1,1))
        self.add_widget(self.value1)

        self.operator = Spinner( text = '+', values =('-', '=='), size_hint=(.1,1))
        self.add_widget(self.operator)

        self.value2 = TextInput(multiline = False, text ="0", size_hint=(.1,1))
        self.add_widget(self.value2)

    def get_command(self):
        line = [self.label, self.variable_name.text, '=', self.value1.text, self.operator.text, self.value2.text]
        return line
       

class PrintLayout(BoxLayout):
    def __init__(self, line, **kwargs):
        super(PrintLayout, self).__init__(**kwargs)
        self.line = line
        self.cols = 2
        self.padding = 4
        self.height = 40
        self.width = 350
        self.label = "PRINT"

        self.line_number = TextInput(text=str(self.line), size_hint=(.2,1))
        self.add_widget(self.line_number)
        self.add_widget(Label(text=self.label, size_hint=(.3,1)))

        self.value = TextInput(multiline = False, size_hint=(.8,1))
        self.add_widget(self.value)

    def get_command(self):
        line = [self.label, self.value.text]
        return line


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)  
        self.command_stack = []
        self.cols = 2
        self.orientation = "vertical"
        self.padding = 10
        self.y_pos= .8
       
        self.left_layout = GridLayout(cols=1,  pos=(5,-10))      

        self.spinner = Spinner( text = 'Menu', values =('New', 'Save', 'Clear Message Box','Exit'), size_hint =(None, None), size=(200,44), pos_hint={'x':.1, 'y':.9})
        self.left_layout.add_widget(self.spinner)

        self.let_button = Button(text="LET", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.7})
        self.left_layout.add_widget(self.let_button)
        
        self.print_button = Button(text="PRINT", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        self.left_layout.add_widget(self.print_button) 

        self.run_button = Button(text="RUN", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        self.left_layout.add_widget(self.run_button)
         
        self.add_widget(self.left_layout)

        self.orientation = "horizontal"

        self.grid_layout = GridLayout(cols=1,  padding=10, spacing=10, size_hint=(None, None), width=500)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.right_layout = ScrollView(size_hint=(None, None),size=(500, 380), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False, do_scroll_y=True)
        self.add_widget(self.right_layout)
        
       
        self.right_layout.add_widget(self.grid_layout)
        
        #self.right_layout = FloatLayout(pos=(200, -10) ,  size_hint=(.5,1))
        #self.right_layout = GridLayout(cols=1, pos=(300,-10))  
        #self.add_widget(self.right_layout)

        self.bottom_layout = GridLayout()
        self.comment = TextInput(text='Output is shown here..', width= 800, height=200)    
        
        self.bottom_layout.add_widget(self.comment)
        #self.bottom_layout.add_widget(TextInput())
        
        self.add_widget(self.bottom_layout)       
        
        self.let_button.bind(on_press =self.add_let)
        self.print_button.bind(on_press = self.add_print)
        self.spinner.bind(text = self.new_program_option)
        self.run_button.bind(on_press = self.run_app)
   

    def new_program_option(self, instance, option):
        if option == 'New':
             self.new_program()
             self.spinner.text = 'Menu'
             self.command_stack=[]
        elif option == 'Exit':
            sys.exit()
        elif option == 'Clear Message Box':
            self.spinner.text = 'Menu'
            self.comment.text=""

    def new_program(self):
        self.grid_layout.clear_widgets() # clear just the widgets inside the grid layout
        self.y_pos = .8

    def add_let(self, instance):
        line = len(self.command_stack) + 1
        command = LetLayout(line,size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos})
        self.grid_layout.add_widget(command)
        self.y_pos -= .1
        self.command_stack.append(command)

    def add_print(self, instance):
        line = len(self.command_stack) + 1
        command = PrintLayout(line, size_hint=(None, None),  pos_hint={ 'x':.2,'y':self.y_pos})
        self.grid_layout.add_widget(command)
        self.y_pos -= .1
        self.command_stack.append(command)


    def run_app(self, instance):
        i = Interpreter()
        line_number = 1
        for cmd in self.command_stack:
            line = cmd.get_command()
            i.add_line(line_number, line)
            line_number = line_number + 1

        i.run()
        output = i.get_output()
        variables = i.get_variables()

        self.comment.text = ""
        self.comment.insert_text('\n Output : \n')
        for value in output:
            self.comment.insert_text(' ' + str(value)+ '\n')

        self.comment.insert_text('\n Memory: \n')
        self.comment.insert_text(' Variable \t Value \n')
        for var in variables.keys():
            value = ' \t' + var + ' \t\t\t ' + str(variables[var]) + '\n'
            self.comment.insert_text(' ' + str(value))



    def get_command_stack(self):
        return self.command_stack

class MyApp(App):
    def build(self):
       main = MainLayout();
      

       return main

if __name__ == '__main__':
    MyApp().run()