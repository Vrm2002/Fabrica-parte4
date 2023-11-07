from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main_menu import Main_Menu
from game_window import Game_Window

class Application(App):
    def build(self):
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(Main_Menu(name = 'main_menu'))
        screen_manager.add_widget(Game_Window(name = 'game_window'))
        
        return screen_manager
    
    
if __name__ == '__main__':
    Application().run()