from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Info_Screen(Screen):
    def __init__(self, **sm):
        super().__init__(**sm)
        
        grid = BoxLayout(orientation = 'vertical')
        
        layout_id = BoxLayout(orientation = 'horizontal')
        lbl_id = Label(text = 'ID', font_size = '20sp')
        txt_id = TextInput(text = '')   
        layout_id.add_widget(lbl_id) 
        layout_id.add_widget(txt_id)
        grid.add_widget(layout_id)
        
           
        layout_name = BoxLayout(orientation = 'horizontal')
        lbl_name = Label(text = 'Name', font_size = '20sp')
        txt_name = TextInput(text = '')
        layout_name.add_widget(lbl_name)
        layout_name.add_widget(txt_name)
        grid.add_widget(layout_name)
        
        
        layout_age = BoxLayout(orientation = 'horizontal')
        lbl_age = Label(text = 'Age', font_size = '20sp')
        txt_age = TextInput(text = '')
        layout_age.add_widget(lbl_age)
        layout_age.add_widget(txt_age)
        grid.add_widget(layout_age)
        
        
        layout_cpf = BoxLayout(orientation = 'horizontal')
        lbl_cpf = Label(text = 'CPF', font_size = '20sp')
        txt_cpf = TextInput(text = '')
        layout_cpf.add_widget(lbl_cpf)
        layout_cpf.add_widget(txt_cpf)
        grid.add_widget(layout_cpf)
        
        layout_buttons = BoxLayout(orientation = 'horizontal')
        button_delete = Button(text = 'Delete', font_size = '20sp')
        button_edit = Button(text = 'Edit', font_size = '20sp')
        button_return = Button(text = '<-', font_size = '20sp')
        button_return.bind(on_press = self.return_back)
        layout_buttons.add_widget(button_return)
        layout_buttons.add_widget(button_delete)
        layout_buttons.add_widget(button_edit)
        grid.add_widget(layout_buttons)
        
        
        self.add_widget(grid)
        
        
    def return_back (self, x):
        self.manager.current = 'main_screen'
        
    
        