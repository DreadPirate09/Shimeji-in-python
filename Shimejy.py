import kivy
from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
	def build(self):
		img = Image(source='samp1.png')
		return img


MainApp().run()