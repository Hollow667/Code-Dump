import kivy
kivy.require('1.8.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class PageList(BoxLayout):
	target_sm = ObjectProperty()

	def switch(self, page):
		self.target_sm.current = page


Builder.load_string('''
<PageList>
	orientation: 'vertical'
	Button:
		text: 'Page 1'
		on_release: root.switch('page1')
	Button:
		text: 'Page 2'
		on_release: root.switch('page2')
<BlankPage@Screen>:
	name: 'blankpage'
<Page1@Screen>:
	name: 'page1'
	Label:
		text: 'Page 1'
<Page2@Screen>:
	name: 'page2'
	Label:
		text: 'Page 2'
''')


root1 = Builder.load_string('''
BoxLayout:
	orientation: 'vertical'

	ScreenManager:
		id: sm
		Screen:
			name: 'pagelist'
			PageList:
				target_sm: sm
		Page1
		Page2

	Button:
		text: 'Back'
		on_release: sm.current = 'pagelist'
		size_hint_y: None
		height: 0 if self.disabled else dp(64)
		opacity: 0 if self.disabled else 1
		disabled: sm.current == 'pagelist'
''')

root2 = Builder.load_string('''
BoxLayout:
	PageList:
		target_sm: sm
	ScreenManager:
		id: sm
		BlankPage
		Page1
		Page2
''')


class Container(FloatLayout):
	def on_size(self, *args):
		if self.width > self.height:
			if root2 not in self.children:
				self.clear_widgets()
				self.add_widget(root2)
		elif root1 not in self.children:
			self.clear_widgets()
			self.add_widget(root1)


class TestApp(App):
	def build(self):
		return Container()


if __name__ == '__main__':
	TestApp().run()