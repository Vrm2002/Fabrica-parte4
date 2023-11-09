from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput



class Main_Screen(Screen):
    def __init__(self, **sm):
        super().__init__(**sm)
        
        box_layout = BoxLayout(orientation = 'vertical')
        
        return_button = Button(text = '<-', font_size = '35sp', size_hint = (0.2, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return_button.bind(on_press = self.return_to_start)
        
        title_lbl = Label(text = 'Registered Users', font_size = '40sp', size_hint = (1, None), height = 50)
        
        info_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        info_layout.bind(minimum_height=info_layout.setter('height'))
        info_lbl = Label(text = 'ID                 NAME                AGE                 CPF', font_size = '20sp', size_hint = (1, None), height = 50)
        info_scroll = ScrollView(size_hint=(1, 1), do_scroll_y=True, do_scroll_x=False, pos_hint={'center_x': 0.5})
        
        for i in range(30):
            info_test_button = Button(text = str('ID                 NAME                AGE                 CPF'), size_hint_y=None, height= 40, font_size = '20sp')
            info_layout.add_widget(info_test_button)
        
        info_search_layout = BoxLayout(orientation = 'horizontal', size_hint = (None, None), width = 500, height = 95)
        info_spacing_lbl = Label(size_hint = (None, 1), width = 190)
        info_search_lbl = Label(text = 'Search:', font_size = '30sp', size_hint = (None, 1), width = 220)
        info_search_input = TextInput(font_size = '30sp', hint_text = 'ID', input_filter = 'int', multiline = False, size_hint=(None, None), width = 150, height = 50, pos_hint={'center_y': 0.5})
        # info_search_input.padding_y = (self.height - info_search_input.line_height) / 2
        info_search_layout.add_widget(info_spacing_lbl)
        info_search_layout.add_widget(info_search_lbl)
        info_search_layout.add_widget(info_search_input)
        
        
        box_layout.add_widget(return_button)
        box_layout.add_widget(title_lbl)
        box_layout.add_widget(info_search_layout)
        box_layout.add_widget(info_lbl)
        info_scroll.add_widget(info_layout)
        box_layout.add_widget(info_scroll)
        self.add_widget(box_layout)
        
    def return_to_start(self, x):
        self.manager.current = 'start'
    
        
        