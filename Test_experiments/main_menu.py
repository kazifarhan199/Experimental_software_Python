from tkinter import *
from tkinter import ttk
import csv_reader
import main_tester

def take_input():
	master=Tk()
	master.resizable(False,False)
	ttk.Label(master,text='Transition type').grid(row=0,column=0)
	ttk.Label(master,text='Amount').grid(row=1,column=0)
	e_name=Entry(master)
	e_name.grid(row=0,column=1)
	e_transition=Entry(master)
	e_transition.grid(row=1,column=1)
	ttk.Button(master,width=20,text='Set New Transition',command=lambda:transition_button(e_name.get(),e_transition.get(),master)).grid(row=2,column=1)

def transition_button(e_name,e_transition,master):
	master.destroy()
	csv_reader.csv_appender(e_name,e_transition)
	main_tester.restart()

def main(root):
	menu=Menu(root)
	root.configure(menu=menu)

	file=Menu(menu,tearoff=False)
	file.add_command(label='EXIT',command=lambda:exit())
	menu.add_cascade(menu=file,label='EXIT')

	New_transition=Menu(menu,tearoff=False)
	New_transition.add_command(label='Add transition',command=take_input)
	menu.add_cascade(menu=New_transition,label='ADD TRANSITION')