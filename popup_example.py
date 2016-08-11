import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup

root = Builder.load_string('''
Button
''')

class TestApp(App):
    def build(self):
        # doesn't work
        Popup(title='hi').open()
        return root

    def on_start(self):
        # does work
        Popup(title='hi').open()
        return

if __name__ == '__main__':
    TestApp().run()