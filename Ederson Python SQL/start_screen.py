from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App


class Start_Sceen(Screen):
    def __init__(self, **sm):
        super().__init__(**sm)
        
        layout = BoxLayout(orientation = 'vertical')
        
        welcome_lbl = Label(text = 'Registration System', font_size = '50sp')
        main_screen_button = Button(text = 'Enter', font_size = '45sp')
        close_button = Button(text = 'Exit', font_size = '45sp')
        main_screen_button.bind(on_press = self.to_main_screen)
        close_button.bind(on_press = self.exit)
        
        layout.add_widget(welcome_lbl)
        layout.add_widget(main_screen_button)
        layout.add_widget(close_button)
        self.add_widget(layout)
        
    
    def to_main_screen(self, x):
        self.manager.current = 'main_screen'
        
    
    def exit(self, x):
        App.get_running_app().stop()
        
        
        
        
        