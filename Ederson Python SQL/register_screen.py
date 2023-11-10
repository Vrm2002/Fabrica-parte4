from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from mysql_connection import MYSQL_Info


class Register_Screen(Screen):
    def __init__(self, **sm):
        super().__init__(**sm)
        
        
        grid = BoxLayout(orientation = 'vertical')
        
        self.input_name = TextInput(hint_text = 'Name')
        self.input_age = TextInput(hint_text = 'Age', input_filter = 'int')
        self.input_cpf = TextInput(hint_text = 'CPF')
        
        button_layout = BoxLayout(orientation = 'horizontal')
        button_save = Button(text = 'Save', font_size = '20sp')
        button_save.bind(on_press = self.save_user_info)
        button_return = Button(text = '<-', font_size = '20sp')
        button_return.bind(on_press = self.return_to_start)
        button_layout.add_widget(button_return)
        button_layout.add_widget(button_save)
        
        
        grid.add_widget(self.input_name)
        grid.add_widget(self.input_age)
        grid.add_widget(self.input_cpf)
        grid.add_widget(button_layout)

        
        self.add_widget(grid)
        
    def return_to_start(self, x):
        self.manager.current = 'start'
        
    
    def save_user_info(self, x):
        name = self.input_name.text
        age = self.input_age.text
        cpf = self.input_cpf.text
        self.sql = MYSQL_Info().register_info(name, age, cpf)
        
