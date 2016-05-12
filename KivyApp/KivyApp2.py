import kivy
import sys
import abc

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


class ExpressionLayout(BoxLayout):
    #__metaclass__ = abc.ABCMeta

    def __init__(self, line, name, **kwargs):
        super(ExpressionLayout, self).__init__(**kwargs)
        self.line = line
        self.name = name
        self.txtbox_lineno = TextInput(text=str(self.line), size_hint=(.1,1))
        self.btn_delete = Button(text="Del", size_hint =(.1,1))
        self.lbl_name = Label(text=self.name, size_hint=(.1,1))
        
    def draw(self):
        self.add_widget(self.btn_delete)
        self.add_widget(self.txtbox_lineno)
        self.add_widget(self.lbl_name)

    def delete_btn_click_event(self, instance):
        self.btn_delete._bind(on_press, instance)

    def get_command(self):
        pass

class LetLayout(ExpressionLayout):

    def __init__(self, line, **kwargs):
        super(LetLayout, self).__init__(line, "LET", **kwargs)

        self.cols = 7
        self.padding = 4
        self.height = 40
        self.width = 400
        

        self.txt_var_name = TextInput(multiline = False, size_hint=(.1,1))
        self.lbl_equal = Label(text="=",  size_hint=(.1,1))
        self.txt_val1 = TextInput(multiline = False, text ="0", size_hint=(.1,1))       
        self.spn_operator = Spinner(text = '+', values =('-', '=='), size_hint=(.1,1))
        self.txt_val2 = TextInput(multiline = False, text ="0", size_hint=(.1,1))
         

    def draw(self):
        super(LetLayout, self).draw()
        self.add_widget(self.txt_var_name)
        self.add_widget(self.lbl_equal)
        self.add_widget(self.txt_val1)
        self.add_widget(self.spn_operator)
        self.add_widget(self.txt_val2)

    def get_expression(self):
        return [self.name, self.txt_var_name.text, lbl_equal.text, self.txt_val1.text, self.spn_operator.text, self.txt_val2.text]


class PrintLayout(ExpressionLayout):

    def __init__(self, line, **kwargs):
        super(PrintLayout, self).__init__(line, "PRINT", **kwargs)

        self.cols = 4
        self.padding = 4
        self.height = 40
        self.width = 350

        self.txt_value = TextInput(multiline = False, size_hint=(.6,1))

    def draw(self):
        super(PrintLayout, self).draw()
        self.add_widget(self.txt_value)

    def get_command(self):
        return [self.name, self.txt_value.text]


class CommandPanel(GridLayout):
    def __init__(self, workspace, **kwargs):
        super(CommandPanel, self).__init__(**kwargs)
        self.cols = 1
        self.pos = (5,-10)
        self.workspace = workspace
        self.expression_buttons = []

        self.spn_menu = Spinner( text = 'Menu', values =('New', 'Save','Exit'), size_hint =(None, None), size=(200,44), pos_hint={'x':.1, 'y':.9})
        self.spn_menu.bind(text = self.menu_option_selected_event)
        
    def draw(self):
        self.add_widget(self.spn_menu)


    def add_expression_btn(self, name):
        btn =  Button(text=str(name), size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        btn.bind(on_press = self.btn_clicked_event)
        self.add_widget(btn)
        self.expression_buttons.append(btn)


    def btn_clicked_event(self, instance):
        self.workspace.add_expression(instance)

    def menu_option_selected_event(self, instance, option):
        
        if option == 'New':
            self.spn_menu.text = 'Menu'
            self.workspace.clear()

        elif option == 'Exit':
            sys.exit()
        


class Workspace(ScrollView):
    def __init__(self, **kwargs):
        super(Workspace, self).__init__(**kwargs)
        self.expression_list = []
        self.y_pos = .8
        self.layout = GridLayout(cols =1, padding=10, spacing =10, size_hint=(None, None), width = 500)
        self.layout.bind(minimum_height=self.layout.setter('height'))
      

    def draw(self):
        self.add_widget(self.layout)

    def clear(self):
        self.expression_list=[]
        self.y_pos = .8
        self.layout.clear_widgets()


    def add_expression(self, instance):
        line = len(self.expression_list) + 1
        #exp = LetLayout(line, size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos})

        if instance.text == 'LET':
            exp = LetLayout(line, size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos})   
        elif instance.text == 'PRINT':
            exp = PrintLayout(line, size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos})

        
        exp.btn_delete.fbind('on_press', self.delete_expression, expression = exp)
        
        exp.draw()
        self.layout.add_widget(exp)
        
        self.y_pos -= .1
        self.expression_list.append(exp)

    def delete_expression(self,instance, expression):
       
        self.layout.remove_widget(expression)
        self.expression_list.remove(expression)

    def get_expressions(self):
        pass

class Output(GridLayout):
    def __init__(self, **kwargs):
        super(Output, self).__init__(**kwargs)
        
        self.comment = TextInput(text='Output is shown here..', width= 800, height=200)
        self.btn_clear = Button(text='Clear', size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        self.btn_clear.bind(on_press =self.clear)
    
    def draw(self):
        self.add_widget(self.comment)
        self.add_widget(self.btn_clear)

    def clear(self, insance):
        self.comment.text = ""

    def add_text(self, text):
        self.comment.insert_text(text)


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.command_stack = []
        self.cols =2
        self.orientation = "verical"
        self.padding = 10
        
        self.workspace = Workspace()
        self.command_panel = CommandPanel(self.workspace)
        self.output = Output()

        self.command_panel.draw()
        self.command_panel.add_expression_btn('LET')
        self.command_panel.add_expression_btn('PRINT')
        self.add_widget(self.command_panel)

        self.orientation = "horizontal"
        self.workspace.draw()
        self.add_widget(self.workspace)
        
        self.output.draw()
        self.add_widget(self.output)

class KivyApp2(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    KivyApp2().run()
                    