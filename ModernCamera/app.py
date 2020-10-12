from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import Screen, ScreenManager
import cv2

# global texture1
class MyCamera(Screen):
    def open_cam(self):
        self.capture = cv2.VideoCapture('karikku.mp4')
        Clock.schedule_interval(self.update, 1.0/33.0)

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        if ret:
        # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
            #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            app = App.get_running_app()
            self.ids.img1.texture = texture1
        else:
            print("[Info] Check camera index....")
            App.get_running_app().stop()
class CameraApp(App):
    sm = ScreenManager()
    pressed = False
    def build(self):
        CameraApp.sm.add_widget(MyCamera(name ="mycamera"))
        return CameraApp.sm

if __name__ == '__main__':
    CameraApp().run()
    cv2.destroyAllWindows()