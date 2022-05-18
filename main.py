from tkinter import Button

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


class MyApp(App):
    def build(self):
        box_for_button = AnchorLayout()
        two_button = BoxLayout(orientation = 'vertical', size_hint = [.5, .5], spacing = 50)
        
        two_button.add_widget(Button(text='MAN'))
        two_button.add_widget(Button(text='WOMAN'))

        box_for_button.add_widget(two_button)
        return box_for_button


    




    
if __name__ == '__main__':
    MyApp().run()






    # def man():

    #     weight = int(input("Введите ваш вес: "))
    #     high = int(input("Введите ваш рост: "))
    #     age = int(input("Введите ваш возраст: "))

    #     normal = high - 100

    #     if normal - 2.5 <= weight <= normal + 1.5 and 12 <= age <= 25:
    #         print("Ваш вес в норме!")

    #     elif weight < normal - 2.51 and 12 <= age <= 25:
    #         print("У вас недостоток веса!")

    #     elif normal - 1.5 <= weight <= normal + 2.5 and 26 <= age <= 40:
    #         print("Ваш вес в норме!")

    #     elif weight < normal - 1.51 and 26 <= age <= 40:
    #         print("У вас недостоток веса!")

    #     elif normal <= weight <= normal + 3.5 and 41 <= age <= 60:
    #         print("Ваш вес в норме!")

    #     elif weight < normal and 41 <= age <= 60:
    #         print("У вас недостоток веса!")

    #     elif normal + 1 <= weight <= normal + 4.5 and 61 <= age <= 105:
    #         print("Ваш вес в норме!")

    #     elif weight < normal + 1 and 61 <= age <= 105:
    #         print("У вас недостоток веса!")

    #     elif 106 <= age:
    #         print("Серьезно?! Вам так много лет?! Мы поздравляем вас! Вы настоящий долгожитель!")

    #     elif 5 <= age <= 11:
    #         print("Друг, у тебя еще все впереди! Сейчас не стоит переживать из-за веса :)")

    #     elif 1 <= age <= 4:
    #         print("Похоже, у нас тут юный гений!!!")

    #     elif age <= 0:
    #         print("Да-да, так мы тебе и поверили, маленький врунишка! :)")

    #     else:
    #         print("У вас избыточный вес!")


    # def woman():

    #     weight = int(input("Введите ваш вес: "))
    #     high = int(input("Введите ваш рост: "))
    #     age = int(input("Введите ваш возраст: "))
        
    #     normalw = high - 108
        
    #     if normalw - 2.5 <= weight <= normalw + 1.5 and 12 <= age <= 25:
    #         print("Ваш вес в норме!")

    #     elif weight < normalw - 2.51 and 12 <= age <= 25:
    #         print("У вас недостоток веса!")

    #     elif normalw - 1.5 <= weight <= normalw + 2.5 and 26 <= age <= 40:
    #         print("Ваш вес в норме!")

    #     elif weight < normalw - 1.51 and 26 <= age <= 40:
    #         print("У вас недостоток веса!")

    #     elif normalw <= weight <= normalw + 3.5 and 41 <= age <= 60:
    #         print("Ваш вес в норме!")

    #     elif weight < normalw and 41 <= age <= 60:
    #         print("У вас недостоток веса!")

    #     elif normalw + 1 <= weight <= normalw + 4.5 and 61 <= age <= 105:
    #         print("Ваш вес в норме!")

    #     elif weight < normalw + 1 and 61 <= age <= 105:
    #         print("У вас недостоток веса!")

    #     elif 106 <= age:
    #         print("Серьезно?! Вам так много лет?! Мы поздравляем вас! Вы настоящий долгожитель!")

    #     elif 5 <= age <= 11:
    #         print("Эх, девочки, девочки! В таком возрасте рано думать о диетах :)")

    #     elif 1 <= age <= 4:
    #         print("Похоже, у нас тут юный гений!!!")

    #     elif age <= 0:
    #         print("Да-да, так мы тебе и поверили, маленькая врунишка! :)")
            
    #     else:
    #         print("У вас избыточный вес!")