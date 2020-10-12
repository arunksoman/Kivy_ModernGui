from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
# Config.set('graphics', 'desktop', 1)
Config.set('graphics', 'borderless', True)
# Config.set('graphics', 'window_state', 'maximized')
from hover_behaviour import HoverBehavior, Window
from kivy.factory import Factory
from kivy.utils import get_color_from_hex as hex
Factory.register('HoverBehavior', HoverBehavior)

class HomeScreen(Screen):
    pass

class Modern_guiApp(App):
    sm = ScreenManager()
    maximized = False
    def min_max(self, maximized):
        app = App.get_running_app()
        app.maximized = maximized
        if maximized:
            Window.maximize()
        else:
            Window.restore()
    def change_cursor(self, cursor_type):
        Window.set_system_cursor(cursor_type)
    def build(self):
        Modern_guiApp.sm.add_widget(HomeScreen(name ="homescreen"))
        return Modern_guiApp.sm

if __name__ == "__main__":
    Window.size = (780, 580)
    # Window.borderless = True
    Modern_guiApp().run()