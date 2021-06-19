from typing import Text
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window


Window.size=(320,600)

class TelaLogin(Screen):
    pass
class TelaRegister(Screen):
    pass


class Main(MDApp):
    def build(self):
        return super().build()


Main().run()