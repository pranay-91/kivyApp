
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class LetLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(LetLayout,self).__init__(**kwargs)
        self.cols = 6
        self.add_widget(Label(text="LET"))
        
        self.variable_name = TextInput(multiline = False)
        self.add_widget(self.variable_name)

        self.add_widget(Label(text="="))

        self.value1 = TextInput(multiline = False, text ="0")
        self.add_widget(self.value1)

        self.value2 = TextInput(multiline = False, text ="+")
        self.add_widget(self.value2)
        
        #self.operator = Button(text="+")
        #self.add_widget(self.operator)
             
        self.value3 = TextInput(multiline = False, text ="0")
        self.add_widget(self.value3)



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
        self.orientation = "horizontal"
        self.padding = 10

        self.button = Button(text="LET")
        self.add_widget(self.button)
        
        self.right_layout = BoxLayout(padding=10, orientation ="vertical")
        self.add_widget(self.right_layout)
       

        self.button.bind(on_press =self.callback)

    def callback(self, instance):
        h_layout = LetLayout(padding = 10)
        self.right_layout.add_widget(h_layout)

        

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