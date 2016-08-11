import kivy
kivy.require('1.8.1')

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: sp(72)



#test list view
#   FileChooserListView
#test icon view
#   FileChooserIconView
#test multi chooser



        Button:
            text: 'Icon View'
            on_press: fc.view_mode = 'icon'
        Button:
            text: 'List View'
            on_press: fc.view_mode = 'list'
    FileChooser:
        id: fc
        on_submit: print 'on_submit', args
        FileChooserIconLayout
        FileChooserListLayout
''')

class TestApp(App):
    def build(self):
        return root

if __name__ == '__main__':
    TestApp().run()