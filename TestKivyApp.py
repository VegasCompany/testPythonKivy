from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
	def build(self):
		bl = BoxLayout(orientation = 'vertical')

		for i in range(20):
			bl.add_widget(Button(text= 'test' + str(i), on_press= self.changeOrientation ))
		return bl
	def changeOrientation(self, instance):
		print(instance.text)
		self.build().add_widget(Button(text='newbutton'))


if __name__ == '__main__':
	MyApp().run()