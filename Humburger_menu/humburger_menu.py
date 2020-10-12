from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout

class Navbar(FloatLayout):
    def __init__.
class HomeScreen(Screen):
    pass
class HumburgerApp(App):
    sm = ScreenManager()
    def build(self):
        HumburgerApp.sm.add_widget(HomeScreen(name ="homescreen"))
        return HumburgerApp.sm

if __name__ == "__main__":
    app = HumburgerApp()
    app.run()