import tkinter as tk
from tkinter import *
import datetime
from tkinter import ttk

day=''
month=''
year=''

def Q(event='e'):
	root.destroy()

def main(event='e'):
	day,month,year=e1.get(),e2.get(),e3.get()
	datetoday=datetime.date.today()
	birth_day=datetime.datetime(int(year),int(month),int(day))
	Age=datetoday.year - birth_day.year
	if datetoday.month < birth_day.month:
		real_age=Age-1
	elif birth_day.month == datetoday.month:
		if datetoday.day < birth_day.day:
			real_age=Age-1
		else:
			real_age=Age
	elif datetoday.month > birth_day.month:
		real_age=Age
	Real_age='You are '+str(real_age)+" year's Old"
	label.configure(text=Real_age)


root=tk.Tk()
root.title('Age calculator')
image = tk.PhotoImage(file="Age.png")
root.iconbitmap('Age.ico')
limage=Label(image=image,width=225,height=225)
limage.grid(row=0,column=0,columnspan=2)
ld=ttk.Label(root,text='Day ? ')
lm=ttk.Label(root,text='Month ? ')
ly=ttk.Label(root,text='Year ? ')
ld.grid(row=1,column=0)
lm.grid(row=2,column=0)
ly.grid(row=3,column=0)

e1=ttk.Entry(root)
e2=ttk.Entry(root)
e3=ttk.Entry(root)
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)

e1.focus()

alculate=ttk.Button(root,text="Get Age",command=main,width=40)
alculate.grid(row=4,column=0,columnspan=2)
label=ttk.Label(root,text='')
label.grid(row=5,column=0,columnspan=2)

root.bind('<Return>',main)
root.bind('<Control-w>',Q)
root.mainloop()
