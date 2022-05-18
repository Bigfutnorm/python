from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout



class DataApp(App):
    def build(self):
        box_for_elements = AnchorLayout()
        four_elemrnts = BoxLayout(orientation = 'vertical', size_hint = [.5, .5], spacing = 15)

        four_elemrnts.add_widget(TextInput(text = 'Ваш вес'))
        four_elemrnts.add_widget(TextInput(text = 'Ваш рост'))
        four_elemrnts.add_widget(TextInput(text = 'Ваш возраст'))
        four_elemrnts.add_widget(Button(text = 'START'))

        box_for_elements.add_widget(four_elemrnts)
        return box_for_elements





if __name__ == '__main__':
    DataApp().run()