from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class HomeScreen(Screen):
    pass
class ProgressbarApp(App):
    sm = ScreenManager()
    def build(self):
        ProgressbarApp.sm.add_widget(HomeScreen(name ="homescreen"))
        return ProgressbarApp.sm

if __name__ == "__main__":
    app = ProgressbarApp()
    app.run()