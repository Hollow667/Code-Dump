
import kivy
kivy.require('1.8.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.clock import Clock
from random import random

root = '''
GridLayout:
    cols: 2
    Label:
        text: app.values[(0, 0)]
    Label:
        text: app.values[(1, 0)]
    Label:
        text: app.values[(0, 1)]
    Label:
        text: app.values[(1, 1)]
'''

class TestApp(App):
    values = DictProperty({})

    def build(self):
        self.update()
        Clock.schedule_interval(self.update, 1)
        return Builder.load_string(root)

    def update(self, *args):
        for i in range(2):
            for j in range(2):
                self.values[(i, j)] = str(random())

if __name__ == '__main__':
    TestApp().run()