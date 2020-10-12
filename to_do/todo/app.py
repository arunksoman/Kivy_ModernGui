from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class HomePage(Screen):
    pass
class TodoApp(App):
    sm = ScreenManager()
    def build(self):
        TodoApp.sm.add_widget(HomePage(name ="homescreen"))
        return TodoApp.sm