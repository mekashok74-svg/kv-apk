from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class LoginScreen(AnchorLayout):
    pass

class LoginApp(App):
    def build(self):
        return LoginScreen()

LoginApp().run()
