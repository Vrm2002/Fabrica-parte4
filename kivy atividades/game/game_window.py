from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from game_logic import Game_Logic

class Game_Window(Screen):
    def __init__(self, **screen_manager):
        super().__init__(**screen_manager)
        
        layout = BoxLayout(orientation = 'vertical')
        
        self.user_input = TextInput()
        lbl = Label(text = 'Try to guess the number!', font_size = '50sp')
        guess_button = Button(text = 'Guess', font_size = '50sp')
        reset_button = Button(text = 'Reset Game', font_size = '50sp')
        guess_button.bind(on_press = self.number_guesser)
        reset_button.bind(on_press = self.game_reset)
        
        self.game_start = Game_Logic()
        self.random_num = self.game_start.random_number_generator()
        
        
        layout.add_widget(self.user_input)
        layout.add_widget(lbl)
        layout.add_widget(guess_button)
        layout.add_widget(reset_button)
        self.add_widget(layout)
        
    def number_guesser(self, x):
        user_number = int(self.user_input.text)
        self.game_start.number_collector(user_number)
        self.output = self.game_start.number_confirmer(self.random_num)
        self.user_input.text = self.output
        
    
    def game_reset(self, x):
        self.random_num = self.game_start.random_number_generator()
