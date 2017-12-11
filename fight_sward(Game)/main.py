from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
import random

##########
oner = False
chimg=False
#########
e_jump=False
cter =0
w_width = 1366
w_height = 768
player_width = 229
player_height = 240

eni_hi=[]
pla_hi=[]

jumper=False
coins=0
coinsb=0
ecount=0
action_en=10

class Back_ground(Image):
    def __init__(self,**kwargs):
        super(Back_ground, self).__init__(**kwargs)
        self.size = (w_width,w_height)

class coin(Image):
    def __init__(self,**kwargs):
        super(coin ,self).__init__(**kwargs)

    def update(self):
        global coins
        self.x += 15

    def updateb(self):
        global coinsb
        self.x -= 15

class Fighter(Image):
    def __init__(self,**kwargs):
        super(Fighter, self).__init__(**kwargs)
        self.helth=500
        self.size = (player_width,player_height)
        self._keyboard = Window.request_keyboard(self._on_keyboard_down, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        global jumper,coins,coinsb

        if keycode == (273, 'up'):
            if(self.y == 80 ):
                jumper = True
                Sound_handler.jum()

        elif keycode == (274, 'down' ):
            jumper = False

        elif keycode == (275, 'right'):
            if(self.x<=w_width-250):
                self.x += 30
            global cter,chimg
            if (cter==0):
                if(chimg==True):
                    self.source = 'aaa.png'
                cter=1
            else:
                if(chimg==True):
                    self.source = 'yayao.png'
                cter=0


        elif keycode == (276, 'left'):
            if (self.x >= 10 ):
                self.x += -30
            if (cter==0):
                if(chimg==True):
                    self.image = 'aaa.png'
                cter=1
            else:
                if(chimg==True):
                    self.source = 'yayao.png'
                cter=0

        if keycode == (99, 'c'):
            coins+=1
            Sound_handler.kick()

        if keycode == (120, 'x'):
            coinsb+=1
            Sound_handler.kick()

    def update(self,other,da1,da2):
        global jumper,coins,coinsb
        global eni_hi
        if(coins >0):
            da1.x=self.x+100
            da1.y=self.y/2+120
            coins=0

        if coinsb>0:
            da2.x=self.x
            da2.y=self.y/2+120
            coinsb=0

        if (jumper == True):
            self.y += 10
            if (self.y >= 400):
                jumper = False

        elif(self.y>80):
            self.y-=10

        if ((other.x + player_width - 50) >= da1.x and (other.x) <= da1.x and (other.y + player_height) >= da1.y and (
        other.y) <= da1.y):
            other.helth -= 50
            da1.x = 10000
            eni_hi[-1].x=10000
            del eni_hi[-1]

        if ((other.x- 50) <= da2.x and (other.x) >= da2.x and (other.y + player_height) >= da2.y and (
        other.y) <= da2.y):
            other.helth -= 50
            da2.x = -10000
            eni_hi[-1].x=10000
            del eni_hi[-1]

class Enime(Image):
    def __init__(self, **kwargs):
        super(Enime, self).__init__(**kwargs)
        self.size = (player_width, player_height)
        self.helth = 500

    def update(self,other,da1,da2,e_dag1,e_dag2):
        global ecount,action_en,e_jump
        global pla_hi
        ecount+=1
        c=True

        if(e_dag1.x > self.x - 150 and e_dag1.x < self.x +50 ):
            if(self.y<81):
                e_jump=True
                Sound_handler.jum()

        if(e_dag2.x < self.x + 150 and e_dag2.x > self.x - 70 ):
            if(self.y<81):
                e_jump=True
                Sound_handler.jum()

        if (e_jump == True):
            self.y += 10
            if (self.y >= 400):
                e_jump = False

        elif(self.y>80):
            self.y-=10


        if(ecount==40):
            action_en = random.randrange(0,4)


        if (action_en==0 and self.x > 0):
            for i in range(0,30):
                a=self.x
                self.x-=4
                if(self.x != a ):
                    if(self.source == 'en_1.png'):
                        self.source = 'en_2.png'
                    elif(self.source == 'en_2.png'):
                        self.source = 'en_1.png'
                if(random.randrange(0,70)):
                    break

        elif(action_en==1 and self.x <1100):
            for i in range(0,30):
                a=self.x
                self.x+=4

                if(self.x != a ):
                    if(self.source == 'en_1.png'):
                        self.source = 'en_2.png'
                    elif(self.source == 'en_2.png'):
                        self.source = 'en_1.png'

                if(random.randrange(0,70)):
                    break

        elif (action_en==2 and self.x > 0):
            for i in range(0,30):
                a=self.x
                self.x-=2
                if(self.x != a ):
                    if(self.source == 'en_1.png'):
                        self.source = 'en_2.png'
                    elif(self.source == 'en_2.png'):
                        self.source = 'en_1.png'

        elif(action_en==3 and self.x <1100):
            for i in range(0,30):
                a=self.x
                self.x+=2
                if(self.x != a ):
                    if(self.source == 'en_1.png'):
                        self.source = 'en_2.png'
                    elif(self.source == 'en_2.png'):
                        self.source = 'en_1.png'

        if((other.x+player_width-50) >= da2.x and (other.x) <= da2.x and (other.y+player_height) >= da2.y and (other.y) <= da2.y):
            other.helth-=50
            pla_hi[-1].x=10000
            del pla_hi[-1]
            da2.x=10000

        if((other.x-50) <= da1.x and (other.x) >= da1.x and (other.y+player_height) >= da1.y and (other.y) <= da1.y):
            other.helth-=50
            pla_hi[-1].x=10000
            del pla_hi[-1]
            da1.x=-10000

        if ecount == 120 and other.x < self.x:
            da2.x=self.x
            Sound_handler.kick()
            da2.y=self.y+50
            ecount=0

        elif ecount == 120 and other.x > self.x:
            da1.x=self.x
            Sound_handler.kick()
            da1.y=self.y+50
            ecount=0

        elif ecount==120:
            ecount=0

class Sound_handler():
    D = SoundLoader.load('death.wav')
    W = SoundLoader.load('won.wav')
    J = SoundLoader.load('jump.ogg')
    C = SoundLoader.load('kick.ogg')
    S = SoundLoader.load('str.ogg')
    M = SoundLoader.load('main.ogg')
    def deth():
        Sound_handler.D.play()
    def win():
        Sound_handler.W.play()
    def jum():
        Sound_handler.J.play()
    def kick():
        Sound_handler.C.play()
    def Str():
        Sound_handler.S.play()
    def ma():
        Sound_handler.M.play()
    def ma_c():
        Sound_handler.M.stop()


class Games(Widget):
    def __init__(self):
        super(Games, self).__init__()

        global oner,eni_hi,pla_hi


        back = Back_ground(source='dada.jpg')
        self.add_widget(back)

        self.fighter = Fighter(source='yayao.png',y=80)

        self.add_widget(self.fighter)

        self.coind=coin(source='daag.png',x=10000)
        self.add_widget(self.coind)
        self.coindb=coin(source='daag.png',x=-10000)
        self.add_widget(self.coindb)

        self.coind2 = coin(source='daag.png', x=10000)
        self.add_widget(self.coind2)
        self.coindb2 = coin(source='daag.png', x=-10000)
        self.add_widget(self.coindb2)

        self.enime=Enime(source='en_1.png',x=1100,y=80)
        self.add_widget(self.enime)

        #self.add_widget(Label(text='Your health is : ',x=60,y=650,markup=True,font_size=32))
        #self.add_widget(Label(text='His health is : ',x=1116,y=650,markup=True,font_size=32))

        self.player_h_l=Label(text=str(self.fighter.helth),x=190,y=650,markup=True,font_size=32)
        self.computer_h_l=Label(text=str(self.enime.helth),x=1246,y=650,markup=True,font_size=32)

        #self.add_widget(self.player_h_l)
        #self.add_widget(self.computer_h_l)

        self.starter=Button(text="START",x=w_width/2-400,background_color=(1,1,1,1),y=w_height/2,size=(800,200),font_size=200)
        self.add_widget(self.starter)
        self.starter.bind(on_press=self.start)

        for i in range (0,int(self.fighter.helth/50)):
            p=i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i
            pl_hi = Image(source='health.png',y=w_height-110,x=p,size=(50,50))
            self.add_widget(pl_hi)
            pla_hi.append(pl_hi)

            r=w_width-75-p
            em_hi = Image(source='health.png',y=w_height-110,x=r,size=(50,50))
            self.add_widget(em_hi)
            eni_hi.append(em_hi)

        Clock.schedule_interval(self.updater,1/65)

    def start(self,*ignore):
        global oner,chimg
        chimg = True
        oner = True
        Sound_handler.Str()
        self.remove_widget(self.starter)


    def updater(self,*ignore):
        if (oner == True):
            self.update()

    def update(self,*ignore):
        global oner,chimg
        Sound_handler.ma()
        self.fighter.update(self.enime,self.coind,self.coindb)
        self.enime.update(self.fighter,self.coind2,self.coindb2,self.coind,self.coindb)

        #self.player_h_l.text = str(self.fighter.helth)
        #self.computer_h_l.text = str(self.enime.helth)

        if (self.fighter.helth==0):
            oner = False
            self.enime.source = 'en_ya.png'
            self.lala =Label(text='[color=#000000]YOU LOSS',x=w_width/2,y=w_height/2+100,markup=True,font_size=200)
            self.add_widget(self.lala)
            Sound_handler.ma_c()
            Sound_handler.deth()

            self.bu=Button(text="Restart",x=w_width/2-400,background_color=(1,0,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.bu)
            self.bu.bind(on_press=self.restart)
            self.ex_b=Button(text="Exit",x=w_width/2,background_color=(1,1,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.ex_b)
            self.ex_b.bind(on_press=exit)

        if(self.enime.helth==0):
            global chimg
            oner = False
            self.fighter.source='yawin.png'
            chimg=False
            self.lala=Label(text='[color=#000000]YOU WONE',x=w_width/2,y=w_height/2+100,markup=True,font_size=200)
            self.add_widget(self.lala)
            Sound_handler.ma_c()
            Sound_handler.win()

            self.bu=Button(text="Restart",x=w_width/2-400,background_color=(0,1,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.bu)
            self.bu.bind(on_press=self.restart)
            self.ex_b=Button(text="Exit",x=w_width/2,background_color=(1,0,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.ex_b)
            self.ex_b.bind(on_press=exit)

        self.coind2.update()
        self.coindb2.updateb()
        self.coind.update()
        self.coindb.updateb()

    def restart(self,*ignore):
        global chimg,oner,pla_hi,eni_hi
        self.fighter.source='aaa.png'
        self.enime.source='en_1.png'
        chimg = True
        oner = True
        self.fighter.helth=500
        self.enime.helth=500
        self.fighter.x=0
        self.fighter.y=80

        self.enime.x=1100
        self.enime.y=80

        self.coind.x=10000
        self.coindb.x=-10000
        self.coind2.x=10000
        self.coindb2.x=-10000

        self.remove_widget(self.ex_b)
        self.remove_widget(self.lala)
        self.remove_widget(self.bu)

        for i in range (0,int(self.fighter.helth/50)):
            try:
                pla_hi[-1].x=10000
                del pla_hi[-1]
            except:
                pass
            try:
                eni_hi[-1].x=10000
                del eni_hi[-1]
            except:
                pass

        for i in range (0,int(self.fighter.helth/50)):
            p=i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i
            pl_hi = Image(source='health.png',y=w_height-110,x=p,size=(50,50))
            self.add_widget(pl_hi)
            pla_hi.append(pl_hi)

            r=w_width-75-p
            em_hi = Image(source='health.png',y=w_height-110,x=r,size=(50,50))
            self.add_widget(em_hi)
            eni_hi.append(em_hi)


class main(App):
    global w_width,w_height
    def build(self):
        r=Games()
        Window.size = (w_width,w_height)
        return r

main().run()
