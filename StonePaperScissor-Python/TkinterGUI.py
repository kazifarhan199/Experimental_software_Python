from tkinter import *
from TerminalMode import main

def guimain(H_C):
    C_C,Result = main(H_C)
    HumanLabel.config(text=H_C)
    CompLabel.config(text=C_C)
    if Result == 'WIN':
        color = 'green'
    elif Result == "LOSS":
        color = "red"
    else:
        color = 'black'
    MainLabel.config(text=Result,fg=color  )

root = Tk()
MainLabel = Label(text="START",font=(None,76))
MainLabel.grid(row=1,column=1,columnspan=3)

HumanLabel = Label(text="YOU",font=(None,45))
HumanLabel.grid(row=2,column=1)
VS = Label(text="  VS  ",font=(None,65))
VS.grid(row=2,column=2)
CompLabel = Label(text="CPU",font=(None,45))
CompLabel.grid(row=2,column=3)

StoneButton = Button(text="STONE",width=10,command=lambda:guimain('STONE'),font=(None,35),bg='#000',fg='#fff')
PeperButton = Button(text="PAPER",width=10,command=lambda:guimain('PAPER'),font=(None,35),bg='#000',fg='#fff')
ScissorButton = Button(text="SCISSOR",width=10,command=lambda:guimain('SCISSOR'),font=(None,35),bg='#000',fg='#fff')
StoneButton.grid(row=3,column=1)
PeperButton.grid(row=3,column=2)
ScissorButton.grid(row=3,column=3)
root.resizable(0,0)
root.mainloop()
