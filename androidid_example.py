__version__ = '1.0'


from kivy.app import App
from kivy.uix.label import Label
from plyer import uniqueid

class TestAndroidID(App):
	def build(self):
		return Label(text=str(uniqueid.id))

TestAndroidID().run()