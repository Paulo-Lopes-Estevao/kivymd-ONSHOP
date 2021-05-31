from typing import Text
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window


Window.size=(320,600)

class Gerenciador(ScreenManager):
    pass

class Fundo_Login(Screen):
    pass

class Fundo_Register(Screen):
    pass

class TelaLogin(Screen):
    def open_register(self):
        #self.add_widget(Fundo_Register())
        self.remove_widget(Fundo_Login())

class TelaRegister(Screen):
   def open_login(self):
    self.add_widget(Fundo_Login())


class Main(MDApp):
    def build(self):
        return Gerenciador()


Main().run()