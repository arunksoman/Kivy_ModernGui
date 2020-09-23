from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
# Config.set('graphics', 'resizable', False)
# Config.set('graphics', 'fullscreen', 'fake')
from hover_behaviour import HoverBehavior, Window
from kivy.factory import Factory
from kivy.utils import get_color_from_hex as hex
Factory.register('HoverBehavior', HoverBehavior)

class HomeScreen(Screen):
    def change_cursor(self, cursor_type):
        Window.set_system_cursor(cursor_type)#000

class Modern_guiApp(App):
    sm = ScreenManager()
    def build(self):
        Modern_guiApp.sm.add_widget(HomeScreen(name ="homescreen"))
        return Modern_guiApp.sm

if __name__ == "__main__":
    Modern_guiApp().run()