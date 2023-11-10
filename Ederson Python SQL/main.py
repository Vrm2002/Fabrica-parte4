from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from start_screen import Start_Sceen
from main_screen import Main_Screen
from info_screen import Info_Screen
from register_screen import Register_Screen


class System(App):
    def build(self):
        
        screens = ScreenManager()
        screens.add_widget(Start_Sceen(name = 'start'))
        screens.add_widget(Main_Screen(name = 'main_screen'))
        screens.add_widget(Info_Screen(name = 'info'))
        screens.add_widget(Register_Screen(name = 'register'))
        
        
        # register = Register_Screen().all_info
        
        # self.register_sql = MYSQL_Info().register_info(register[0], register[1], register[2])
        
        
        # mysql_info_getter = MYSQL_Info().info_getter()
        # self.main_screen = Main_Screen().user_info_display(mysql_info_getter)
        
        
        return screens
        
        
if __name__ == '__main__':
    System().run()