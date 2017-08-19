from tkinter import *
import data_manager
from functools import partial
from datetime import date

dates_labels=[]
names_labels=[]
amount_labels=[]
balance_labels=[]
edit_buttons=[]
show_balance_label=[]
deleat_buttons=[]
event=0

date_of_transition, name_of_transition, amount_of_transition, amount_of_balance = data_manager.csv_reader()

def display_data():
	global date_of_transition, name_of_transition, amount_of_transition, amount_of_balance 
	for i in range(len(date_of_transition)):
		
		dates_labels.append(Label(frame1,bg='snow',text=date_of_transition[i]))
		dates_labels[i].grid(row=i+2,column=0)
		Label(frame1,text='|',bg='snow').grid(row=i+2,column=1)
		names_labels.append(Label(frame1,bg='snow',text=name_of_transition[i]))
		names_labels[i].grid(row=i+2,column=2)

		amount_labels.append(Label(frame1,bg='snow',text=amount_of_transition[i]))
		amount_labels[i].grid(row=i+2,column=3)
		Label(frame1,text='|',bg='snow').grid(row=i+2,column=4)
		balance_labels.append(Label(frame1,bg='snow',text=amount_of_balance[i]))
		balance_labels[i].grid(row=i+2,column=5)
		Label(frame1,text='|',bg='snow').grid(row=i+2,column=6)
		edit_buttons.append(Button(frame1,text='EDIT',bg='ivory3',width=12,command=partial(edit,i,date_of_transition, name_of_transition, amount_of_transition)))
		edit_buttons[i].grid(row=i+2,column=7)

		deleat_buttons.append(Button(frame1,text='DELEAT',width=12,bg='ivory3',command=partial(terminate,i)))
		deleat_buttons[i].grid(row=i+2,column=8)

	show_balance_label.append(Label(frame2, fg='green',bg='snow',font=(None,17)))
	show_balance_label[0].grid(row=1,column=2)


	try:
		show_balance_label[0].configure(text=amount_of_balance[-1])
	except:
		pass


def edit(i,date_of_transition, name_of_transition, amount_of_transition):
	global event

	if event==0:
		edit_date_containor=Entry(frame1,width=9,bg='snow')
		edit_name_containor=Entry(frame1,width=10,bg='snow')
		edit_amount_containor=Entry(frame1,width=7,bg='snow')
		#edit_balance_containor=Entry(frame1,width=10)	

		edit_date_containor.grid(row=i+2,column=0)
		edit_name_containor.grid(row=i+2,column=1)
		edit_amount_containor.grid(row=i+2,column=2)
		#edit_balance_containor.grid(row=i+2,column=3)

		edit_date_containor.insert(0,date_of_transition[i])
		edit_name_containor.insert(0,name_of_transition[i])
		edit_amount_containor.insert(0,amount_of_transition[i])
		#edit_balance_containor.insert(0,amount_of_balance[i])
	
		edit_buttons[i].configure(text='SAVE',command=lambda:save(i,edit_date_containor,edit_name_containor,edit_amount_containor,date_of_transition, name_of_transition, amount_of_transition))
		event=1		
	else:
		print('First Save the file U are editting')

def save(i,get_date,get_name,get_amount,edit_date_containor,edit_name_containor,edit_amount_containor):
		global event, amount_of_balance
		
		edit_date_containor[i]=get_date.get()
		edit_name_containor[i]=get_name.get()
		edit_amount_containor[i]=get_amount.get()

		new_dates,new_names,new_ammount,new_balances =  data_manager.csv_write(edit_date_containor,edit_name_containor,edit_amount_containor)

		dates_labels[i].configure(text=new_dates[i])
		names_labels[i].configure(text=new_names[i])
		amount_labels[i].configure(text=new_ammount[i])

		edit_buttons[i].configure(text="EDIT",command=partial(edit,i,new_dates,new_names,new_ammount))

		for r in range(len(new_dates)):
			balance_labels[r].configure(text=new_balances[r])

		get_date.destroy()
		get_name.destroy()
		get_amount.destroy()

		show_balance_label[0].configure(text=new_balances[-1])
		
		event=0

def add_transition():
	master=Tk()
	Label(master,bg='snow',text='Enter Transition name : ').grid(row=0,column=0)
	Label(master,bg='snow',text='Enter Transition amount : ').grid(row=1,column=0)
	new_name_to_add=Entry(master,bg='snow')
	new_amount_to_add=Entry(master,bg='snow')
	new_name_to_add.grid(row=0,column=1)
	new_amount_to_add.grid(row=1,column=1)
	Button(master,text='Add',bg='snow',command=lambda:add_transition_main(new_name_to_add.get(),new_amount_to_add.get(),master),width=20).grid(row=2,column=1)
	master.mainloop()

def add_transition_main(name,amount,master):
	global date_of_transition, name_of_transition, amount_of_transition, amount_of_balance
	global dates_labels,names_labels,amount_labels,balance_labels,edit_buttons,show_balance_label

	date_of_transition, name_of_transition, amount_of_transition, amount_of_balance = data_manager.csv_append(date.today(),name,amount)
	for i in range(len(dates_labels)):
		del dates_labels[0]
		del	names_labels[0]
		del	amount_labels[0]
		del	balance_labels[0]
		del	edit_buttons[0]

	del	show_balance_label[0]

	display_data()
	master.destroy()

def terminate(i):
	global date_of_transition, name_of_transition, amount_of_transition, amount_of_balance
	global dates_labels,names_labels,amount_labels,balance_labels,edit_buttons
	print(amount_of_transition)

	del date_of_transition[i] 
	del name_of_transition[i] 
	del amount_of_transition[i] 
	del amount_of_balance[i]	

	print(amount_of_transition)

	date_of_transition, name_of_transition, amount_of_transition, amount_of_balance = data_manager.csv_write(date_of_transition,name_of_transition,amount_of_transition)

	print(amount_of_transition)	

	dates_labels[i].destroy()
	names_labels[i].destroy()
	amount_labels[i].destroy()
	balance_labels[i].destroy()
	edit_buttons[i].destroy()
	deleat_buttons[i].destroy()

	del dates_labels[i]
	del names_labels[i]
	del amount_labels[i]
	del balance_labels[i]
	del edit_buttons[i]
	del deleat_buttons[i]

	show_balance_label[0].configure(text=amount_of_balance[-1])
	
	print(str(i)+'this is i')
	
	for r in range(len(balance_labels)):
		balance_labels[r].configure(text=amount_of_balance[r])
		print(r)

root=Tk()
root.resizable(False,False)	
frame1 = Frame(bg='snow')
frame1.grid(row=0,column=0)


Label(frame1,bg='snow',text='----------------Date------------------Transitin Type-------------Transition Ammount------------------Balance------------------------------------EDIT----------------------------DELEAT-------------').grid(row=0,column=0,columnspan=9)
Label(frame1,bg='snow',text='_______________________________________________________________________________________________________________________________________________________________________________________________________________').grid(row=1,column=0,columnspan=9)

frame2 = Frame(bg='snow')
frame2.grid(row=1,column=0,columnspan=2)


framebin = Frame()

display_data()

Label(frame2,bg='snow',text="________________________________________________________________________________________________________________________________________________________________________________________________________").grid(row=0,column=0,columnspan=5)
Add_transition_button=Button(frame2,font=('Arial CE',13),text='ADD TRANSITION',bg='ivory3',command=lambda:add_transition())
Add_transition_button.grid(row=1,column=0)

root.bind('<Control-w>',exit)
root.mainloop()