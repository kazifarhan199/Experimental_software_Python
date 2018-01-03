from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from random import randrange
from time import sleep

main_start = False

class Main_win(GridLayout):
    def __init__(self):
        super(Main_win,self).__init__()
        self.cols=1
        self.butt = Button(text='Start')
        self.butt.bind(on_press=self.main_w)
        self.add_widget(self.butt)

    def main_w(self,*ignore):
        self.remove_widget(self.butt)

        self.cols = 3
        self.b1=Button(text='')
        self.add_widget(self.b1)
        self.b2=Button(text='')
        self.add_widget(self.b2)
        self.b3=Button(text='')
        self.add_widget(self.b3)
        self.b4=Button(text='')
        self.add_widget(self.b4)
        self.b5=Button(text='')
        self.add_widget(self.b5)
        self.b6=Button(text='')
        self.add_widget(self.b6)
        self.b7=Button(text='')
        self.add_widget(self.b7)
        self.b8=Button(text='')
        self.add_widget(self.b8)
        self.b9=Button(text='')
        self.add_widget(self.b9)
        self.b1.bind(on_press=self.Cross_maker)
        self.b2.bind(on_press=self.Cross_maker)
        self.b3.bind(on_press=self.Cross_maker)
        self.b4.bind(on_press=self.Cross_maker)
        self.b5.bind(on_press=self.Cross_maker)
        self.b6.bind(on_press=self.Cross_maker)
        self.b7.bind(on_press=self.Cross_maker)
        self.b8.bind(on_press=self.Cross_maker)
        self.b9.bind(on_press=self.Cross_maker)
        self.o=[]
        self.x_l=[]
        self.list=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]

    def Cross_maker(self,a):
        if a.text=='':
            a.text='X'
            self.x_l.append(a)
            self.list.remove(a)
            #print(a.x) lllllllllllllllllllllllllllllllllllll
            e=self.check(self.x_l)
            if e == 1:
                self.end(e)
            else:
                self.circle()

    def circle(self):
        if len(self.list)!=0 :
            b = randrange(len(self.list))
            d = self.list[b]
            d.text = 'O'
            self.o.append(d)
            self.list.remove(d)
            print(d.x)
            t = self.check(self.o)
            if t == 1:
                self.end(2)

    def check(self,li):
        lf = {}
        ln = 0
        g = 0
        for i in li:
            if (i.x not in lf):
                lf[i.x]=1
            else:
                lf[i.x]+=1

        for i in lf :
            if (lf[i]==3):
                g = 1

        liy={}
        for i in li:
            if (i.y not in liy):
                liy[i.y]=1
            else:
                liy[i.y]+=1

        for i in liy :
            if (liy[i]==3):
                g = 1


        for j in range(len(li)):
            if (int(li[j].x) == 266 )and(int(li[j].y) == 200):
                for z in range(len(li)):
                    for f in range(len(li)):
                        if (int(li[z].x) == 0 )and(int(li[z].y) == 0)and (int(li[f].x) == 533 )and((int(li[f].y) == 400)):
                            g = 1
                        if (int(li[z].x) == 533 )and(int(li[z].y) == 0)and (int(li[f].x) == 0 )and((int(li[f].y) == 400)):
                            g = 1



        return g

    def end(self,e):
        for i in self.list:
            self.remove_widget(i)
        for i in self.x_l:
            self.remove_widget(i)
        for i in self.o:
            self.remove_widget(i)

        if e == 1 :
            b = Label(text='WON',size=(100,40))
            self.add_widget(b)
        else:
            b = Label(text='LOSS',size=(100,40))
            self.add_widget(b)

         #mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

class Main(App):
    def build(self):
        re=Main_win()
        return re

Main().run()
