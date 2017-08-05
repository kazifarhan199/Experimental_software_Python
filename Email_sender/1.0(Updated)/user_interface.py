from tkinter import *
import send
from tkinter import filedialog

name='email_list.csv'
send_mode=0

def main_sender():
	global name
	global send_mode
	if send_mode == 0:
		send_to = to_email_entry.get()

	elif send_mode == 1:
		import csvreader
		send_to = csvreader.csv_soter(name)

	sender_email       =sender_email_entry.get()
	sender_passwardard =sender_passward_entry.get()
	subject            =subject_email_entry.get()
	message_body       =body_email_entry.get('0.0',END)

	send.main(
		sender_email,
		sender_passwardard,
		send_to,
		subject,
		message_body
		)
	sender_email_entry.grid(row=1,column=1)

def file_taker():
	global name
	fileName = filedialog.askopenfilename(filetypes=(('howCode file'
		,'*.csv'),('Allfiles','*.*')))
	name = fileName
	mass_mode(str(fileName))


def mass_mode(a=0):
	global send_mode
	send_mode=1
	to_list_label=Label(text=name,width=90,height=1)
	to_list_label.config(font=(None,'8'))
	to_list_label.grid(row=3,column=0,columnspan=2)
	file_button.config(text='File',bg='blue',command=file_taker)
	if a!=0:
		to_list_label.configure(text=a)				

def single_mode():
	global send_mode
	send_mode=0
	to_email_label=Label(text='     Send to :')
	to_email_label.grid(row=3,column=0)
	to_email_entry=Entry(width=66)
	to_email_entry.grid(row=3,column=1)
	file_button.config(text='Exit',bg='red',command=Quit)


def Quit():
	exit()


root=Tk()
file_name=StringVar()

menu=Menu(root)
root.configure(menu=menu)

file=Menu(menu,tearoff=False)
file.add_command(label='Quit',command=Quit)
menu.add_cascade(label='File',menu=file)

mode=Menu(menu,tearoff=False)
mode.add_command(label='Mass sennder mode',command=mass_mode)
mode.add_command(label='Single sennder mode',command=single_mode)
menu.add_cascade(label='Mode',menu=mode)

sender_email_label=Label(text="     e-mail :")
sender_email_label.grid(row=1,column=0)
sender_email_entry=Entry(width=66)
sender_email_entry.grid(row=1,column=1)

sender_passward_label=Label(text="Passwardard :")
sender_passward_label.grid(row=2,column=0)
sender_passward_entry=Entry(width=66)
sender_passward_entry.grid(row=2,column=1)


to_email_label=Label(text='     Send to :')
to_email_label.grid(row=3,column=0)
to_email_entry=Entry(width=66)
to_email_entry.grid(row=3,column=1)

subject_email_label=Label(text='     Subject :')
subject_email_label.grid(row=4,column=0)
subject_email_entry=Entry(width=66)
subject_email_entry.grid(row=4,column=1)

body_email_label=Label(text="Email :")
body_email_label.grid(row=5,column=0)
body_email_entry=Text(width=50)
body_email_entry.grid(row=5,column=1)

sender_email_label.config(font=('Courier',12))
sender_passward_label.config(font=('Courier',12))
to_email_label.config(font=('Courier',12))
subject_email_label.config(font=('Courier',12))
body_email_label.config(font=('Courier',12))

send_button=Button(text='Send',command=main_sender,width=57,
	bg='green')
send_button.grid(row=6,column=1)

file_button=Button(text='Exit',width=20,bg='red',command=Quit)
file_button.grid(row=6,column=0)

root.bind('Control-w',Quit)
root.iconbitmap('email.ico')

root.mainloop()
