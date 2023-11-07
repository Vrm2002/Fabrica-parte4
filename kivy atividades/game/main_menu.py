from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Main_Menu(Screen):
    def __init__(self, **screen_manager):
        super().__init__(**screen_manager)
        
        layout = BoxLayout(orientation = 'vertical')

        lbl = Label(text = 'Welcome to the Game!', font_size = '60sp')
        play_button = Button(text = 'play', font_size = '50sp')
        play_button.bind(on_press = self.go_to_game_window)
        
        layout.add_widget(lbl)
        layout.add_widget(play_button)
        self.add_widget(layout)
        
    def go_to_game_window(self, x):
        self.manager.current = 'game_window'
    
    
        
        