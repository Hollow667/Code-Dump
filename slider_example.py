from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    orientation: 'vertical'
    Slider:
        id: slider
        min: -1
        max: 1
        step: 0.001
    Label:
        text: str(slider.value)
'''
class SliderApp(App):
    def build(self):
        return Builder.load_string(kv)

SliderApp().run()