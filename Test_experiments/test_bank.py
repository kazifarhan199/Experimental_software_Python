from tkinter import *
from functools import partial


def get_that(name):
	print(name)
	print(a[name].get())

root=Tk()
a=[]
paper=[]

for name in range(3):
	a.append(Entry())
	a[-1].pack()
	paper.append(Button(text='get',command=partial(get_that,name)))
	paper[-1].pack()

print(a)


root.mainloop()
