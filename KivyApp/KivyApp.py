
import kivy
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

class LetLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(LetLayout,self).__init__(**kwargs)
        self.cols = 6
        self.padding = 4
        self.height = 40
        self.width = 300

        self.add_widget(Label(text="LET"))
        
        self.variable_name = TextInput(multiline = False)
        self.add_widget(self.variable_name)

        self.add_widget(Label(text="="))

        self.value1 = TextInput(multiline = False, text ="0")
        self.add_widget(self.value1)

        self.spinner = Spinner( text = '+', values =('-', '=='))
        self.add_widget(self.spinner)

        self.value2 = TextInput(multiline = False, text ="0")
        self.add_widget(self.value2)
        
        #self.operator = Button(text="+")
        #self.add_widget(self.operator)
             
    

class PrintLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(PrintLayout, self).__init__(**kwargs)
        self.cols = 2
        self.padding = 4
        self.height = 40
        self.width = 300
        self.add_widget(Label(text="PRINT"))

        self.value = TextInput(multiline = False)
        self.add_widget(self.value)


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password) 
        self.button = Button(text="Click")
        self.add_widget(self.button)
        self.button.bind(on_press = self.callback)

    def callback(self, instance):
        print('The button <%s> is pressed'% instance.text)

class MyWidget(BoxLayout):
    pass

class MainWidget(Widget):
    #def __init__(self, **kwargs):
    #    super(MainWidget, self).__init__(**kwargs)
    #    self.add_widget(MyWidget())
    pass  


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.cols = 2
        self.orientation = "vertical"
        self.padding = 10
        self.y_pos= .8

        self.left_layout = FloatLayout(orientation="vertical")      
        self.add_widget(self.left_layout)

        self.spinner = Spinner( text = 'Menu', values =('New', 'Work', 'Other', 'Custom'), size_hint =(None, None), size=(200,44), pos_hint={'x':.1, 'y':.9})
        self.left_layout.add_widget(self.spinner)

        self.new_button = Button(text="New Program", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.8})
        self.left_layout.add_widget(self.new_button)

        self.let_button = Button(text="LET", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.7})
        self.left_layout.add_widget(self.let_button)
        
        self.print_button = Button(text="PRINT", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        self.left_layout.add_widget(self.print_button) 

       
        self.orientation = "horizontal"
        self.right_layout = FloatLayout(padding=10, orientation ="vertical")
        self.add_widget(self.right_layout)
       
        self.new_button.bind(on_press=self.new_program)
        self.let_button.bind(on_press =self.add_let)
        self.print_button.bind(on_press = self.add_print)
        self.spinner.bind(text = self.new_program_option)
   

    def new_program_option(self, instance, option):
        if option == 'New':
             self.right_layout.clear_widgets()
             self.y_pos = .8
             self.spinner.text = 'Menu'

    def new_program(self,instance):
        self.right_layout.clear_widgets()
        self.y_pos = .8

    def add_let(self, instance):
        self.right_layout.add_widget(LetLayout(size_hint=(None, None),  pos_hint={'x':.1,'y':self.y_pos}))
        self.y_pos -= .1

    def add_print(self, instance):
        self.right_layout.add_widget(PrintLayout( size_hint=(None, None),  pos_hint={ 'x':.1,'y':self.y_pos}))
        self.y_pos -= .1


class MyApp(App):
    def build(self):
        #main_layout = BoxLayout(padding=10, orientation = "vertical")
        #for i in range(3):
        #     h_layout = LetLayout(padding = 10)
        #     main_layout.add_widget(h_layout)
        #return main_layout 

             
        #return LoginScreen()
        #return LetLayout()
        #return MainWidget()
        #pass
        return MainLayout()

if __name__ == '__main__':
    MyApp().run()