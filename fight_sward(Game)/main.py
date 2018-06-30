#from kivy.config import Config
#Config.set('graphics', 'fullscreen', 1)
# I am not using this just because it is a game and the loading
#  looks better with Window.size for now
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
mute = False
oner = False
##########
ft=0
#########
eni_1 = 'images/en_1.png'
eni_2 = 'images/en_2.png'
eni_count=0
######
h_i_1 = 'images/aaa.png'
h_i_2 = 'images/yayao.png'
py_count=0
#####
back_src ='images/dada3.png'
back_count = 0
###
hea_png='images/health.png'
src_daag="images/daag1.png"
dag_count = 0

e_jump=False
cter=0
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

chimg = False

class Back_ground(Image):
    def __init__(self,**kwargs):
        super(Back_ground, self).__init__(**kwargs)
        self.size = (w_width,w_height)

class coin(Image):
    def __init__(self,**kwargs):
        super(coin ,self).__init__(**kwargs)

    def update(self):
        global coins
        self.x += 25

    def updateb(self):
        global coinsb
        self.x -= 25

class Fighter(Image):
    def __init__(self,**kwargs):
        super(Fighter, self).__init__(**kwargs)
        self.helth=500
        self.left_d=False
        self.riht_d=False
        self.size = (player_width,player_height)
        self._keyboard = Window.request_keyboard(self._on_keyboard_down, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        global jumper,coins,coinsb,cter,chimg

        if keycode == (273, 'up'):
            if(self.y == 80 ):
                jumper = True
                Sound_handler.jum()

        elif keycode == (274, 'down' ):
            jumper = False

        elif keycode == (275, 'right'):
            self.riht_d=True
            self.left_d=False

        elif keycode == (276, 'left'):
            self.riht_d=False
            self.left_d=True

        if keycode == (99, 'c'):
            coins+=1
            Sound_handler.kick()

        if keycode == (120, 'x'):
            coinsb+=1
            Sound_handler.kick()

    def up(self,*ignore):
        global jumper,coins,coinsb,cter,chimg
        if(self.y == 80 ):
            jumper = True
            Sound_handler.jum()
    def down(self,*ign):
        global jumper,coins,coinsb,cter,chimg
        jumper = False

    def right(self,*ign):
        self.riht_d=True
        self.left_d=False

    def left(self,*ign):
        self.left_d=True
        self.riht_d=False

    def c(self,*ign):
        global jumper,coins,coinsb,cter,chimg
        coins+=1
        Sound_handler.kick()
#ffffffffffffffffffffff
    def xf(self,*ign):
        global jumper,coins,coinsb,cter,chimg
        coinsb+=1
        Sound_handler.kick()


    def update(self,other,da1,da2):
        global jumper,coins,coinsb
        global cter,chimg
        global eni_hi
        self.eni = other

        if(self.left_d==True):
            if (self.x >= 10 ):
                self.x += -7
                if (cter==0):
                    if(chimg==True):
                        self.source = h_i_1
                    cter=1
                else:
                    if(chimg==True):
                        self.source = h_i_2
                    cter=0
            else :
                self.right()

        if(self.riht_d==True):
            if(self.x<=w_width-250 ):
                self.x += 7
                if (cter==0):
                    if(chimg==True):
                        self.source = h_i_1
                    cter=1
                else:
                    if(chimg==True):
                        self.source = h_i_2
                    cter=0
            else:
                self.left()

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

        if ((other.x- 50) <= da2.x and (other.x+50) >= da2.x and (other.y + player_height) >= da2.y and (
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
        self.p=0

    def update(self,other,da1,da2,e_dag1,e_dag2):
        global ecount,action_en,e_jump
        global pla_hi
        ecount+=1
        c=True

#        if (ecount == 30 ):
#            self.p+=1
#            if(self.p==9):
#                try:
#                    eni_hi[-1].x=10000
#                    del eni_hi[-1]
#                    self.helth=500
#                    for i in range (0,int(self.helth/50)):
#                        p=i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i
#                        r=w_width-75-p
#                        em_hi = Image(source='images/health.png',y=w_height-110,x=r,size=(50,50))
#                        self.add_widget(em_hi)
#                        eni_hi.append(em_hi)
#
#                except:
#                    pass


        if(e_dag1.x > self.x - 240 and e_dag1.x < self.x +140 ):
            if(self.y<81):
                e_jump=True
                Sound_handler.jum()

        if(e_dag2.x < self.x + 240 and e_dag2.x > self.x - 140 ):
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
                    if(self.source == eni_1):
                        self.source = eni_2
                    elif(self.source == eni_2):
                        self.source = eni_1
                if(random.randrange(0,70)):
                    break

        elif(action_en==1 and self.x <1100):
            for i in range(0,30):
                a=self.x
                self.x+=4

                if(self.x != a ):
                    if(self.source == eni_1):
                        self.source = eni_2
                    elif(self.source == eni_2):
                        self.source = eni_1

                if(random.randrange(0,70)):
                    break

        elif (action_en==2 and self.x > 0):
            for i in range(0,30):
                a=self.x
                self.x-=2
                if(self.x != a ):
                    if(self.source == eni_1):
                        self.source = eni_2
                    elif(self.source == eni_2):
                        self.source = eni_1

        elif(action_en==3 and self.x <1100):
            for i in range(0,30):
                a=self.x
                self.x+=2
                if(self.x != a ):
                    if(self.source == eni_1):
                        self.source = eni_2
                    elif(self.source == eni_2):
                        self.source = eni_1

        if((other.x+player_width-50) >= da2.x and (other.x) <= da2.x and (other.y+player_height) >= da2.y and (other.y) <= da2.y):
            other.helth-=50
            pla_hi[-1].x=100000
            del pla_hi[-1]
            da2.x=-100000

        if((other.x-50) <= da1.x and (other.x) >= da1.x and (other.y+player_height) >= da1.y and (other.y) <= da1.y):
            other.helth-=50
            pla_hi[-1].x=100000
            del pla_hi[-1]
            da1.x=100000

        if ecount == 100 and other.x < self.x:
            da2.x=self.x
            Sound_handler.kick()
            da2.y=self.y+50
            ecount=0

        elif ecount == 100 and other.x > self.x:
            da1.x=self.x
            Sound_handler.kick()
            da1.y=self.y+50
            ecount=0

        elif ecount==120:
            ecount=0

class Sound_handler():
    global mute
    D = SoundLoader.load('sounds/death.wav')
    W = SoundLoader.load('sounds/won.wav')
    J = SoundLoader.load('sounds/jump.ogg')
    C = SoundLoader.load('sounds/kick.ogg')
    S = SoundLoader.load('sounds/str.ogg')
    M = SoundLoader.load('sounds/main.ogg')
    def deth():
        if(mute==False):
            Sound_handler.D.play()
    def win():
        if(mute==False):
            Sound_handler.W.play()
    def jum():
        if(mute==False):
            Sound_handler.J.play()
    def kick():
        if(mute==False):
            Sound_handler.C.play()
    def Str():
        if(mute==False):
            Sound_handler.S.play()
    def ma():
        if(mute==False):
            Sound_handler.M.play()
    def ma_c():
        if(mute==False):
            Sound_handler.M.stop()


class Games(Widget):
    def __init__(self):
        super(Games, self).__init__()

        global oner,eni_hi,pla_hi,back_src

        self.back = Back_ground(source=back_src)
        self.add_widget(self.back)

        self.fighter = Fighter(source=h_i_2,y=80)
        self.add_widget(self.fighter)

        self.coind=coin(source=src_daag,x=10000)
        self.add_widget(self.coind)
        self.coindb=coin(source=src_daag,x=-10000)
        self.add_widget(self.coindb)

        self.coind2 = coin(source=src_daag, x=10000)
        self.add_widget(self.coind2)
        self.coindb2 = coin(source=src_daag, x=-10000)
        self.add_widget(self.coindb2)

        self.enime=Enime(source=eni_1,x=1100,y=80)
        self.add_widget(self.enime)

        self.player_h_l=Label(text=str(self.fighter.helth),x=190,y=650,markup=True,font_size=32)
        self.computer_h_l=Label(text=str(self.enime.helth),x=1246,y=650,markup=True,font_size=32)

        self.starter=Button(text="START",x=w_width/2-400,background_color=(1,1,1,1),y=w_height/2,size=(800,200),font_size=200)

        self.options=Button(text="Options",x=w_width/2-200,background_color=(0,1,1,1),y=w_height/2-200,size=(400,100),font_size=100)

        self.exit_button = Button(text="Exit",size=(100,50),x=0,y=w_height-50,background_color=(1,0,0,1),font_size=30)
        self.exit_button.bind(on_press=self.exiter)
        self.add_widget(self.exit_button)


        self.add_widget(self.starter)
        self.add_widget(self.options)

        self.starter.bind(on_press=self.start)
        self.options.bind(on_press=self.option)

        for i in range (0,int(self.fighter.helth/50)):
            p=i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i+i
            pl_hi = Image(source='images/health.png',y=w_height-110,x=p,size=(50,50))
            self.add_widget(pl_hi)
            pla_hi.append(pl_hi)

            r=w_width-75-p
            em_hi = Image(source='images/health.png',y=w_height-110,x=r,size=(50,50))
            self.add_widget(em_hi)
            eni_hi.append(em_hi)

        Clock.schedule_interval(self.updater,1/75)

    def exiter(self,*ignore):
        main().stop()


    def option(self,*ignore):
        self.remove_widget(self.starter)
        self.remove_widget(self.options)
        try:
            self.remove_widget(self.ex_b)
            self.remove_widget(self.lala)
            self.remove_widget(self.bu)
        except:
            pass

        self.opt_starter = Button(text="Back",x=0,y=0)
        self.opt_starter.bind(on_press=self.opt_str)
        self.add_widget(self.opt_starter)

        self.opt_starter_sta = Button(text="Start",x=w_width-100,y=0)
        self.opt_starter_sta.bind(on_press=self.start)
        self.add_widget(self.opt_starter_sta)

        self.label_wep = Label(text='Weapon ',color=(0,0,0,1),size=(400,200),font_size=100,x=300,y=450)
        self.add_widget(self.label_wep)

        self.wep_image=Image(source=src_daag,x=800,y=500)
        self.add_widget(self.wep_image)

        self.wep_change=Button(text="Change",font_size=25,background_color=(1,0,1,1),size=(100,50),x=900,y=525)
        self.wep_change.bind(on_press=self.change_wep)
        self.add_widget(self.wep_change)
#########################
        self.label_back = Label(text='Background ',color=(0,0,0,1),size=(400,200),font_size=100,x=300,y=15)
        self.add_widget(self.label_back)

        self.back_change=Button(text="Change",font_size=45,background_color=(1,0,1,1),size=(175,75),x=880,y=75)
        self.back_change.bind(on_press=self.change_back)
        self.add_widget(self.back_change)
###########################

        self.muter=Button(text='Muter',x=w_width-100,y=w_height-50,size=(100,50))
        self.muter.bind(on_press=self.mut)
        self.add_widget(self.muter)

        self.label_ene = Label(text='Enemy ',color=(0,0,0,1),size=(400,200),font_size=100,x=300,y=300)
        self.add_widget(self.label_ene)

        self.enimi=Image(source=eni_1,x=800,y=350)
        self.add_widget(self.enimi)

        self.eni_chang=Button(text="Change",font_size=25,background_color=(1,0,0,1),size=(100,50),x=900,y=375)
        self.eni_chang.bind(on_press=self.kaka)
        self.add_widget(self.eni_chang)

        self.label_py = Label(text='You ',color=(0,0,0,1),size=(400,200),font_size=100,x=300,y=150)
        self.add_widget(self.label_py)
        self.pymi=Image(source=h_i_1,x=800,y=210)
        self.add_widget(self.pymi)

        self.py_chang=Button(text="Change",font_size=25,background_color=(1,0,0,1),size=(100,50),x=900,y=230)
        self.py_chang.bind(on_press=self.py_i_chang)
        self.add_widget(self.py_chang)
        try:
            self.add_widget(self.exit_button)
        except:
            pass

    def change_back(self,*ignore):
        global back_src, back_count

        if(back_count==0):
            back_src='images/dada.png'
            self.back.source=back_src
            back_count=1

        elif(back_count==1):
            back_src='images/dada1.png'
            self.back.source=back_src
            back_count=2

        elif(back_count==2):
            back_src='images/dada2.png'
            self.back.source=back_src
            back_count=3

        elif(back_count==3):
            back_src='images/dada3.png'
            self.back.source=back_src
            back_count=0


    def py_i_chang(self,*ignore):
        global h_i_1,h_i_2 ,py_count

        if(py_count==0):
            h_i_1='images/sask.png'
            h_i_2='images/sask2.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=1

        elif(py_count==1):
            h_i_1='images/rabo.png'
            h_i_2='images/rabo2.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=2

        elif(py_count==2):
            h_i_1='images/en_1.png'
            h_i_2='images/en_2.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=3

        elif(py_count==3):
            h_i_1='images/gost_5.png'
            h_i_2='images/gost_5.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=4

        elif(py_count==4):
            h_i_1='images/gost_2.png'
            h_i_2='images/gost_2.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=5

        elif(py_count==5):
            h_i_1='images/gost_1.png'
            h_i_2='images/gost_1.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=6

        elif(py_count==6):
            h_i_1='images/hero_1.png'
            h_i_2='images/hero_1.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=7

        elif(py_count==7):
            h_i_1='images/def_1.png'
            h_i_2='images/def_1.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=8

        elif(py_count==8):
            h_i_1='images/someone_1.png'
            h_i_2='images/someone_1.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=9


        elif(py_count==9):
            h_i_1='images/aaa.png'
            h_i_2='images/yayao.png'
            self.fighter.source=h_i_1
            self.pymi.source=h_i_1
            py_count=0

    def kaka(self,*ignore):
        global eni_1,eni_2 ,eni_count

        if(eni_count==0):
            eni_1="images/rabo.png"
            eni_2="images/rabo2.png"
            self.enime.source=eni_1
            self.enimi.source=eni_1
            eni_count=1

        elif(eni_count==1):
            eni_1='images/aaa.png'
            eni_2='images/yayao.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=2

        elif(eni_count==2):
            eni_1='images/sask.png'
            eni_2='images/sask2.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=3


        elif(eni_count==3):
            eni_1='images/gost_5.png'
            eni_2='images/gost_5.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=4

        elif(eni_count==4):
            eni_1='images/gost_2.png'
            eni_2='images/gost_2.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=5

        elif(eni_count==5):
            eni_1='images/gost_1.png'
            eni_2='images/gost_1.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=6

        elif(eni_count==6):
            eni_1='images/hero_1.png'
            eni_2='images/hero_1.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=7

        elif(eni_count==7):
            eni_1='images/def_1.png'
            eni_2='images/def_1.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=8

        elif(eni_count==8):
            eni_1='images/someone_1.png'
            eni_2='images/someone_1.png'
            self.enime.source=eni_1
            self.enimi.source=eni_1
            eni_count=9

        elif(eni_count==9):
            eni_1='images/en_1.png'
            eni_2='images/en_2.png'
            self.enimi.source=eni_1
            self.enime.source=eni_1
            eni_count=0

    def change_wep(self,*ignore):
        global src_daag ,dag_count


        if(dag_count==0):
            src_daag='images/daag2.png'
            self.wep_image.source=src_daag
            self.coind.source=src_daag
            self.coindb2.source=src_daag
            self.coind2.source=src_daag
            self.coindb.source=src_daag
            dag_count=1

        elif(dag_count==1):
            src_daag='images/daag3.png'
            self.wep_image.source=src_daag
            self.coind.source=src_daag
            self.coindb2.source=src_daag
            self.coind2.source=src_daag
            self.coindb.source=src_daag
            dag_count=2

        elif(dag_count==2):
            src_daag='images/daag.png'
            self.wep_image.source=src_daag
            self.coind.source=src_daag
            self.coindb2.source=src_daag
            self.coind2.source=src_daag
            self.coindb.source=src_daag
            dag_count=3

        elif(dag_count==3):
            src_daag="images/daag1.png"
            self.wep_image.source=src_daag
            self.coind.source=src_daag
            self.coindb2.source=src_daag
            self.coind2.source=src_daag
            self.coindb.source=src_daag
            dag_count=0

    def opt_str(self,*ignore):
        try:
            self.add_widget(self.starter)
        except:
            pass
        try:
            self.add_widget(self.options)
        except:
            pass
        try:
            self.remove_widget(self.opt_starter)
            self.remove_widget(self.opt_starter_sta)
        except:
            pass
        try:
            self.remove_widget(self.muter)
        except:
            pass
        try:
            self.remove_widget(self.unmuter)
        except:
            pass
        self.remove_widget(self.label_wep)
        self.remove_widget(self.label_ene)
        self.remove_widget(self.back_change)
        self.remove_widget(self.label_back)

        self.remove_widget(self.wep_image)
        self.remove_widget(self.wep_change)
        self.remove_widget(self.enimi)
        self.remove_widget(self.eni_chang)
        self.remove_widget(self.py_chang)
        self.remove_widget(self.label_py)
        self.remove_widget(self.pymi)


    def mut(self,*ignore):
        global mute
        mute=True
        self.remove_widget(self.muter)
        self.unmuter=Button(text='Unmuter',x=w_width-100,y=w_height-50,size=(100,50))
        self.unmuter.bind(on_press=self.unmut)
        self.add_widget(self.unmuter)

    def unmut(self,*ignore):
        global mute
        mute=False

        self.remove_widget(self.unmuter)
        self.muter.bind(on_press=self.mut)
        self.add_widget(self.muter)

    def start(self,*ignore):
        global oner,chimg
        chimg = True
        oner = True
        try:
            self.remove_widget(self.opt_starter)
            self.remove_widget(self.opt_starter_sta)
            self.remove_widget(self.label_wep)
            self.remove_widget(self.label_ene)
            self.remove_widget(self.back_change)
            self.remove_widget(self.label_back)

            self.remove_widget(self.wep_image)
            self.remove_widget(self.wep_change)
            self.remove_widget(self.enimi)
            self.remove_widget(self.eni_chang)
            self.remove_widget(self.label_py)
            self.remove_widget(self.py_chang)
            self.remove_widget(self.pymi)

        except:
            pass
        try:
            self.restart()
        except:
            pass
        Sound_handler.Str()
        self.remove_widget(self.starter)
        self.remove_widget(self.options)
        self.remove_widget(self.starter)
        self.remove_widget(self.exit_button)
        try:
            self.remove_widget(self.opt_starter_sta)
            self.remove_widget(self.opt_starter)
        except:
            pass
        try:
            self.remove_widget(self.muter)
        except:
            pass
        try:
            self.remove_widget(self.unmuter)
        except:
            pass

    def updater(self,*ignore):
        if (oner == True):
            self.update()

    def update(self,*ignore):
        global oner,chimg,ft
        side_no=0
        if (self.fighter.x-50 < self.enime.x):
            side_no = 0
        elif(self.fighter.x>self.enime.x):
            side_no = 1
        if (ft==0):
            Sound_handler.ma()
            ft=1

        self.fighter.update(self.enime,self.coind,self.coindb)
        self.enime.update(self.fighter,self.coind2,self.coindb2,self.coind,self.coindb)


        if (self.fighter.helth==0):
            oner = False
            self.enime.source = 'images/en_ya.png'
            self.lala =Label(text='[color=#000000]YOU LOST',x=w_width/2,y=w_height/2+100,markup=True,font_size=200)
            self.add_widget(self.lala)
            Sound_handler.ma_c()
            self.add_widget(self.options)
            self.add_widget(self.exit_button)
            Sound_handler.deth()
            self.bu=Button(text="Restart",x=w_width/2-400,background_color=(1,0,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.bu)
            self.bu.bind(on_press=self.restart)
            self.ex_b=Button(text="Exit",x=w_width/2,background_color=(1,1,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.ex_b)
            self.ex_b.bind(on_press=self.exiter)


        if(self.enime.helth==0):
            global chimg
            oner = False
            self.fighter.source='images/yawin.png'
            chimg=False
            self.lala=Label(text='[color=#000000]YOU WON',x=w_width/2,y=w_height/2+100,markup=True,font_size=200)
            self.add_widget(self.lala)
            self.add_widget(self.options)


            Sound_handler.ma_c()
            Sound_handler.win()

            self.bu=Button(text="Restart",x=w_width/2-400,background_color=(0,1,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.bu)
            self.bu.bind(on_press=self.restart)
            self.ex_b=Button(text="Exit",x=w_width/2,background_color=(1,0,0,1),y=w_height/2-30,size=(400,100),font_size=100)
            self.add_widget(self.ex_b)
            self.ex_b.bind(on_press=self.exiter)

        self.coind2.update()
        self.coindb2.updateb()
        self.coind.update()
        self.coindb.updateb()

        if((self.fighter.x+50 >= self.enime.x and self.fighter.x < self.enime.x+player_width-50) and (self.fighter.y == self.enime.y) ):
            if(side_no == 0):
                if(self.fighter.x<=10):
                    self.enime.x += 20
                elif(self.enime.x>=1100):
                    self.fighter.x -= 20
                else:
                    self.fighter.x -= 20
                    self.enime.x += 20

            if(side_no == 1):
                if(self.fighter.x>=1100):
                    self.enime.x == 20
                elif(self.enime.x<=10):
                    self.fighter.x += 20

                else:
                    self.fighter.x += 20
                    self.enime.x -= 20

    def restart(self,*ignore):
        global jumper,e_jump,ft
        global chimg,oner,pla_hi,eni_hi
        self.fighter.source=h_i_1
        self.enime.source=eni_1
        ft=0
        chimg = True
        oner = True
        jumper=False
        e_jump=False
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

        self.remove_widget(self.options)
        self.remove_widget(self.exit_button)

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
            pl_hi = Image(source=hea_png,y=w_height-110,x=p,size=(50,50))
            self.add_widget(pl_hi)
            pla_hi.append(pl_hi)

            r=w_width-75-p
            em_hi = Image(source=hea_png,y=w_height-110,x=r,size=(50,50))
            self.add_widget(em_hi)
            eni_hi.append(em_hi)


class main(App):
    global w_width,w_height
    def build(self):
        r=Games()
        Window.fullscreen = True
        Window.size = (w_width,w_height)
        return r

main().run()
