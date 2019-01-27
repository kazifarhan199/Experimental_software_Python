from tkinter import *
from random import randrange

def main(h_c):
    c_c=randrange(0,3)
    a = {0:'Stone',1:'Paper',2:'Scissors'}
    lh.configure(text=a[c_c])
    lc.configure(text=a[h_c])
    if(h_c==c_c):
        l1.configure(text="Tie")

    elif((h_c == 1 and c_c == 0 )or(h_c == 2 and c_c == 1)or(h_c == 0and c_c == 2)):
        l1.configure(text='Wone')

    elif((h_c == 1 and c_c == 0 )or(h_c == 2 and c_c == 1)or(h_c == 0and c_c == 2)):
        l1.configure(text='Loss')


root=Tk()
l1=Label(text="Fight",font=(None , 100))
lc=Label(text="comp",font=(None , 25))
lv=Label(text="Vs",font=(None , 25))
lh=Label(text="You",font=(None , 25))

l1.grid(row=0,column=0,columnspan=3)
lc.grid(row=1,column=0)
lv.grid(row=1,column=1)
lh.grid(row=1,column=2)

b1=Button(text='stone',command=lambda:main(0),height=2,width=25,bg='green')
b1.grid(row=2,column=0)
b2=Button(text='papaer',command=lambda:main(1),height=2,width=25,bg='green')
b2.grid(row=2,column=1)
b3=Button(text='scissors',command=lambda:main(2),height=2,width=25,bg='green')
b3.grid(row=2,column=2)
root.resizable(0,0)
root.mainloop()
