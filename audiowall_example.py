
'''
Audiowall Page Example
=============
'''

import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty
from glob import glob
from os.path import dirname, join, basename


class AudiowallButton(Button):

    filename = StringProperty(None)
    sound = ObjectProperty(None)
    title = StringProperty(None)

    def update_position(self, *largs):
        remaining = self.time_format(self.sound.length - self.sound.get_pos())
        self.text = "PLAYING\n"+str(remaining)

    def on_filename(self, instance, value):
        if self.sound is None:
            self.sound = SoundLoader.load(value)
            self.title=basename(self.filename[:-4]).replace('_', ' ')
            self.text = self.title+"\n"

    def on_press(self):
        if self.sound.status != 'stop':
            self.sound.stop()
            Clock.unschedule(self.update_position)
            self.text = self.title+"\n"+self.time_format(self.sound.length)
        else:
            self.sound.play()
            Clock.schedule_interval(self.update_position, 1/20.)

    def time_format(self, time):
        return '{0:.2f}'.format(time)


class AudiowallPage(GridLayout):

    def __init__(self, **kwargs):
        super(AudiowallPage, self).__init__(**kwargs)

        for fn in glob(join(dirname(__file__),'*.mp3')):
            btn = AudiowallButton(filename=fn)
            self.add_widget(btn)


class AudiowallApp(App):

    def build(self):
        self.root = root = AudiowallPage(spacing=5, cols=3)
        return root

if __name__ == '__main__':
    AudiowallApp().run()