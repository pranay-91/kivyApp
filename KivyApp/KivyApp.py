
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
from kivy.uix.scrollview import ScrollView

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


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
      
        self.cols = 2
        self.orientation = "vertical"
        self.padding = 10
        self.y_pos= .8
       

        self.left_layout = GridLayout(cols=1,  pos=(5,-10), size_hint=(.4,1))      
        

        self.spinner = Spinner( text = 'Menu', values =('New', 'Work', 'Other', 'Custom'), size_hint =(None, None), size=(200,44), pos_hint={'x':.1, 'y':.9})
        self.left_layout.add_widget(self.spinner)

        self.new_button = Button(text="New Program", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.8})
        self.left_layout.add_widget(self.new_button)

        self.let_button = Button(text="LET", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.7})
        self.left_layout.add_widget(self.let_button)
        
        self.print_button = Button(text="PRINT", size_hint =(None, None), size=(200,44),pos_hint={'x':.1, 'y':.6})
        self.left_layout.add_widget(self.print_button) 

        self.add_widget(self.left_layout)

        self.orientation = "horizontal"

        self.grid_layout = GridLayout(cols=1,  padding=10, spacing=10, size_hint=(None, None), width=500)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.right_layout = ScrollView(size_hint=(None, None),size=(500, 320), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False, do_scroll_y=True)
        self.add_widget(self.right_layout)
        
       
        self.right_layout.add_widget(self.grid_layout)
        
        


        #self.right_layout = FloatLayout(pos=(200, -10) ,  size_hint=(.5,1))
        #self.right_layout = GridLayout(cols=1, pos=(300,-10))  
        #self.add_widget(self.right_layout)

        self.bottom_layout = GridLayout( cols=1,pos=(5,-200), size_hint=(1,.4))
        self.comment = TextInput(text='Comment' )    
        
        self.bottom_layout.add_widget(self.comment)
        self.add_widget(self.bottom_layout)       
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
        self.grid_layout.clear_widgets() # clear just the widgets inside the grid layout
        #self.right_layout.clear_widgets() # right layout is scroll view, grid layout is containd in this layout. do not clear this widget
        self.y_pos = .8

    def add_let(self, instance):
        #self.right_layout.add_widget(LetLayout(size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos}))
        self.grid_layout.add_widget(LetLayout(size_hint=(None, None),  pos_hint={'x':.2,'y':self.y_pos}))
        self.y_pos -= .1

    def add_print(self, instance):
        #self.right_layout.add_widget(PrintLayout( size_hint=(None, None),  pos_hint={ 'x':.2,'y':self.y_pos}))
        self.grid_layout.add_widget(PrintLayout( size_hint=(None, None),  pos_hint={ 'x':.2,'y':self.y_pos}))
        
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

        #layout = GridLayout(cols=1, padding=10, spacing=10,
        #        size_hint=(None, None), width=500)

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required to
        # contain all the childs. (otherwise, we'll child outside the bounding
        # box of the childs)
        
        #layout.bind(minimum_height=layout.setter('height'))

        # add button into that grid
        #for i in range(30):
        #    btn = Button(text=str(i), size=(480, 40),
        #                 size_hint=(None, None))
        #    layout.add_widget(btn)


        #layout = MainLayout()
        #layout.bind(minimum_height=layout.setter('height'))
        ## create a scroll view, with a size < size of the grid
        #root = ScrollView(size_hint=(None, None), size=(500, 320),
        #        pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        #root.add_widget(layout)

        #return root



        return MainLayout()

if __name__ == '__main__':
    MyApp().run()