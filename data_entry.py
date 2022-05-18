from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout



class DataApp(App):
    def build(self):
        four_elemrnts = BoxLayout(orientation = 'vertical', padding = [150], spacing = 50)

        four_elemrnts.add_widget(TextInput(text = 'Ваш вес'))
        four_elemrnts.add_widget(TextInput(text = 'Ваш рост'))
        four_elemrnts.add_widget(TextInput(text = 'Ваш возраст'))
        four_elemrnts.add_widget(Button(text = 'START'))

        return four_elemrnts





if __name__ == '__main__':
    DataApp().run()