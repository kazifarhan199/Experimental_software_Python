from tkinter import *
from functools import partial
import csv_reader
import main_menu

date,name,transition,amount=csv_reader.csv_reader()

editor_event=0

name_Entry=[]
name_buttons=[]

name_dates=[]
name_transitions_names=[]
name_transitions_amounts=[]
name_balancs=[]

def label_and_Editor():
	global	date,name,transition,amount
	date,name,transition,amount=csv_reader.csv_reader()
	global name_Entry,name_buttons,name_labes,name_dates,name_transitions_names,name_transitions_amounts,name_balancs
	
	try:
		for i in range(7):
			name_dates.append(Label(text=date[i]))
			name_transitions_names.append(Label(text=name[i]))
			name_transitions_amounts.append(Label(text=transition[i]))
			name_balancs.append(Label(text=amount[i]))

			name_dates[-1].grid(row=i+2,column=0)
			name_transitions_names[-1].grid(row=i+2,column=1)
			name_transitions_amounts[-1].grid(row=i+2,column=2)
			name_balancs[-1].grid(row=i+2,column=3)

			name_buttons.append(Button(width=15,text="EDIT",command=partial(get_that,i,date,name,transition,amount)))
			name_buttons[-1].grid(row=i+2,column=4)
	
	except:
			print('a')
	
	Label(text='________________________________________________________________________________________________________________________________').grid(row=15,column=0,columnspan=5)
	Label(text=amount[0],fg='green',font=(None,15)).grid(row=16,column=4)
	Add_amount_button=Button(text='ADD TRANSITION',bg='red',font=(None,10),command=lambda:main_menu.take_input())
	Add_amount_button.grid(row=16,column=0)

def get_that(name_object,date,name,transition,amount):
	global editor_event 
	if editor_event==0:	
		editor_event=1

		enter_new_date=Entry(width=17)
		enter_new_date.grid(row=name_object+2,column=0)
		entr_new_anme_of_transition=Entry(width=17)
		entr_new_anme_of_transition.grid(row=name_object+2,column=1)
		enter_new_transition_ammount=Entry(width=17)
		enter_new_transition_ammount.grid(row=name_object+2,column=2)
		enter_new_transition_balance=Entry(width=17)
		enter_new_transition_ammount.grid(row=name_object+2,column=3)

		enter_new_date.insert(0,date[name_object])
		entr_new_anme_of_transition.insert(0,name[name_object])
		enter_new_transition_ammount.insert(0,transition[name_object])
		enter_new_transition_ammount.insert(0,amount[name_object])

		name_buttons[name_object].configure(text='Save',command=lambda:saving(name_object,enter_new_date,entr_new_anme_of_transition,enter_new_transition_ammount))	

	else:
		print('Dont screw this')

def saving(object_name,enter_new_date,entr_new_anme_of_transition,enter_new_transition_ammount):
	global	date,name,transition,amount
	global name_Entry,name_buttons,name_labes,name_dates,name_transitions_names,name_transitions_amounts,name_balancs
	global editor_event 
	print(object_name)

	name_dates[object_name].configure(text=enter_new_date.get())
	name_transitions_names[object_name].configure(text=entr_new_anme_of_transition.get())
	name_transitions_amounts[object_name].configure(text=enter_new_transition_ammount.get())
	#name_balancs[object_name].configure(text='Have SEX')
	
	date[object_name]=enter_new_date.get()
	name[object_name]=entr_new_anme_of_transition.get()
	transition[object_name]=enter_new_transition_ammount.get()

	enter_new_date.destroy()
	entr_new_anme_of_transition.destroy()
	enter_new_transition_ammount.destroy()

	editor_event=0
	name_buttons[object_name].configure(text='Edit',command=partial(get_that,object_name,date,name,transition,amount))

	new_Date=date[::-1]
	new_name=name[::-1]
	new_transition=transition[::-1]
	new_amount=amount[::-1]		
	element_no=object_name
	
	csv_reader.csv_writer(new_Date,new_name,new_transition,new_amount,element_no)


	print(amount[0])

def restart():
	label_and_Editor()	
if __name__ == '__main__':
	root=Tk()
	Label(text='-----Date-----').grid(row=0,column=0)
	Label(text='----transtition-Name-----').grid(row=0,column=1)
	Label(text='-----Ammount------').grid(row=0,column=2)
	Label(text='------Baalnce------').grid(row=0,column=3)
	Label(text='-------Edit-----').grid(row=0,column=4)

	Label(text='_______________________').grid(row=1,column=0)
	Label(text='_______________________').grid(row=1,column=1)
	Label(text='_______________________').grid(row=1,column=2)
	Label(text='_______________________').grid(row=1,column=3)
	Label(text='_______________________').grid(row=1,column=4)



	label_and_Editor()
	main_menu.main(root)
	root.bind("<Control-w>",exit)
	root.mainloop()
