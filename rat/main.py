from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.gridlayout import GridLayout
import random


score=0
counter_x=0
counter_y=0

rat_speed_x=2
rat_speed_y=2

game_height=650
game_width=1100

rat_size_x=110  #originall is 109
rat_size_y=110	#originall is 130
chees_size=75	#originall is 100

class original_size(Image):
	def __init__(self,**kwargs):
		super(original_size,self).__init__(**kwargs)
		self.size=self.texture_size
#		self.size=(game_width,game_height)

class cheese(Image):#100x100
	def __inti__(self,**kwargs):
		super(cheese,self).__init__(self)
		self.size=(chees_size,chees_size)
	
	def update(self):
		self.x+=2

	def displace(self):
		global rat_speed_x,rat_speed_y,  score
		x_c=random.randrange(100,game_width-100)
		y_c=random.randrange(100,game_height-100)
		score+=1
		self.x=x_c
		self.y=y_c
		incr=0.2
		if rat_speed_x > 0:
			rat_speed_x+=incr
		else:
			rat_speed_x-=incr

		if rat_speed_y > 0: 	
			rat_speed_y+=incr
		else:
			rat_speed_y-=incr

class rat(Image):#150x150
	def __init__(self,**kwargs):
		super(rat,self).__init__(**kwargs)
		self.size=(rat_size_x,rat_size_y)
		self._keyboard = Window.request_keyboard(self._keyboard_closed,self)
		self._keyboard.bind(on_key_down=self._on_keyboard_down)
		self.start=0

	def _keyboard_closed(self):
		self._keyboard.unbind(_on_keyboard_down=self._on_keyboard_down)
		self._keyboard=None


	def _on_keyboard_down(self,keyboard,keycode,text,modifiers):
		global rat_speed_x,rat_speed_y,counter_x,counter_y
		#(273, 'up')#(276, 'left')#(275, 'right')#(274, 'down')
		if keycode == (273, 'up'):
			counter_y=1
			rat_speed_y=abs(rat_speed_y)

		elif keycode == (274, 'down'):
			counter_y=1
			rat_speed_y=-abs(rat_speed_y)			

		if keycode == (275, 'right'):
			counter_x=1
			rat_speed_x=abs(rat_speed_x)

		elif keycode == (276, 'left'):
			counter_x=1
			rat_speed_x=-abs(rat_speed_x)			

	def update(self):
		global score
		global counter_x,counter_y
		if counter_x == 1 :
			self.x+=rat_speed_x
		if counter_y == 1 :
			self.y+=rat_speed_y

		if (self.x>=game_width- rat_size_x) or (self.x<0) or (self.y>=game_height- rat_size_y) or (self.y<0):

			Window.size=(300,100)

			score_page=ModalView(auto_dismiss=False)
			score_page.add_widget(Label(text='Game over with Score >> [color=#96ff00]'+str(score)+'[/color]',markup=True,font_size=22))
			score_page.open()			
			counter_x=0
			counter_y=0

class game(Widget):
	def __init__(self,background):
		super(game,self).__init__()
		self.add_widget(background)

		self.rat_ing=rat(source='rat.png',x=game_width/2-75.5,y=10) #x=game_width/2-75.5
		self.add_widget(self.rat_ing)

		x_c=random.randrange(100,game_width-100)
		y_c=random.randrange(100,game_height-100)
		self.chees_ing=cheese(source='chees.png',x=x_c,y=y_c)
		self.add_widget(self.chees_ing)

		Clock.schedule_interval(self.update,1.0/60.0)

	def update(self,*ignore):
		self.rat_ing.update()
		if ((self.rat_ing.x+rat_size_x) >= self.chees_ing.x and self.rat_ing.x <= (self.chees_ing.x + chees_size)) and((self.rat_ing.y+rat_size_y) >= self.chees_ing.y and self.rat_ing.y <= (self.chees_ing.y + chees_size)):
			self.chees_ing.displace()

class main(App):
	def build(self):
		background=original_size(source='b.png')
		Game=game(background)
		Window.clearcolor=(1,1,1,1)
		Window.size=(game_width,game_height)     #(900, 650)
		return Game

main().run()