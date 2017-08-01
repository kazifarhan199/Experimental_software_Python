import datetime
import tkinter as tk
from tkinter import ttk 

def button_pressed(event='e'):
	year=ey.get()
	month=em.get()
	day=ed.get()
	
	date_birth=datetime.date(int(year),int(month),int(day))
	date_today=datetime.date.today()

	year_difference=date_today.year-date_birth.year

	if date_today.month < date_birth.month:
		year_difference -= 1

	la.configure(text='You are '+str(year_difference)+' years old')

def close(event):
	root.quit()

root=tk.Tk()
root.title('Age')
root.iconbitmap('C:\\Users\\kazif\\Downloads\\paper.ico')
#could add above line after coping and makng a .ico file and providing path above

root.bind('<Control-w>',close)    #for shoetcut window close
root.bind('<Return>',button_pressed)

ld=ttk.Label(root,text='Day')
lm=ttk.Label(root,text='Month')
ly=ttk.Label(root,text='Year')
ld.grid(row=1,column=1)
lm.grid(row=2,column=1)
ly.grid(row=3,column=1)

ed=ttk.Entry(root)
em=ttk.Entry(root)
ey=ttk.Entry(root)
ed.grid(row=1,column=2)
em.grid(row=2,column=2)
ey.grid(row=3,column=2)

ed.focus()

b=ttk.Button(text='Get',width=10,command=lambda:button_pressed())
b.grid(row=4,column=1)

la=ttk.Label(root)
la.grid(row=4,column=2)

root.mainloop()