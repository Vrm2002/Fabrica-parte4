from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        # Criando um TextInput
        text_input = TextInput(text='Texto centralizado', multiline=False)

        # Ajustando o padding_y após a criação do TextInput
        text_input.padding_y = (self.height - text_input.line_height) / 2

        # Adicionando o TextInput à caixa
        self.add_widget(text_input)

class MyApp(App):
    def build(self):
        return MyBoxLayout(orientation='vertical', padding=10)

if __name__ == '__main__':
    MyApp().run()