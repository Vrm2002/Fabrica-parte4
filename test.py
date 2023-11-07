import kivy 
from kivy.app import App
from kivy.uix.label import Label


class Myapp(App):
    def build (self):
        
        lbl = Label(text = "Hello World!")
        
        return lbl 
    
if __name__ == '__main__':
    Myapp().run()