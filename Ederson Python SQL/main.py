from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from start_screen import Start_Sceen
from main_screen import Main_Screen

class System(App):
    def build(self):
        
        screens = ScreenManager()
        screens.add_widget(Start_Sceen(name = 'start'))
        screens.add_widget(Main_Screen(name = 'main_screen'))
        
        
        return screens
        
        
if __name__ == '__main__':
    System().run()