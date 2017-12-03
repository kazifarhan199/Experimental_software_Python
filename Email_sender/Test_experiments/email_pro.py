from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
import send

class user_interface(GridLayout):
	def __init__(self,**kwargs):
		super(user_interface,self).__init__(**kwargs)
		red = (2.5, 0, 0, 1.5)   	# use a (r, g, b, a) tuple
		green=(0, 255, 0, 0.6)

		self.cols=2
		self.add_widget(Label(text="Email: "))
		self.username=TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text="Passward: "))
		self.password=TextInput(multiline=False,password=True)
		self.add_widget(self.password)

		self.add_widget(Label(text="Send To: "))
		self.send_to=TextInput(multiline=False)
		self.add_widget(self.send_to)
		self.add_widget(Label(text="Subject: "))
		self.subject=TextInput(multiline=False)
		self.add_widget(self.subject)

		self.add_widget(Label(text="Message: "))
		self.message=TextInput()
		self.add_widget(self.message)

		self.exit=Button(text='Exit',background_color=red)
		self.add_widget(self.exit)
		self.exit.bind(on_press=self.quit)
		self.send_email=Button(text='Send',background_color=green)
		self.add_widget(self.send_email)
		self.send_email.bind(on_press=self.send)

	def send(self,event='True'):
		send.main(
			self.username.text,
			self.password.text,
			self.send_to.text,
			self.subject.text,
			self.message.text
			)

	def quit(self,GridLayout):
		load = ObjectProperty(None)
		cancel = ObjectProperty(None)

class main(App,GridLayout):
	title='Mass_email_sender(Sano version)'
	def build(self):
		return user_interface()

main().run()
